from gurobipy import *
import cuttingstock


# item demands for each order
demands = [4, 1, 3, 2, 2]

# item lengths for each order
lengths = [6, 8, 5, 5, 9]

# the type of items in each order
types = [1, 0, 1, 1, 0]

# length of rolls of each type
roll_lengths = [22, 20]

# number of available rolls of each type
m = 4

assert(len(demands) == len(lengths) == len(types))
assert(max(types) == len(roll_lengths) - 1)
model = cuttingstock.solve(lengths, demands, types, m, roll_lengths)

print("Obj:", model.objVal)
for v in model.getVars():
	print(f"{v.varName}：{round(v.x,3)}")
