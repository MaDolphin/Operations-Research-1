from gurobipy import *
import cuttingstock


# item demands for each order
demands = [2, 4, 3, 2, 3, 3, 6, 6, 6, 5, 7, 2, 1, 5, 4, 7, 1, 6, 1, 4, 4, 7, 2, 2, 5, 4, 3, 4, 3, 4, 5, 4, 5, 5, 5, 1, 5, 2, 4, 2, 6, 3, 3, 4, 7, 4, 3, 5, 2, 1]

# item lengths for each order
lengths = [5, 6, 5, 7, 9, 6, 8, 7, 5, 6, 5, 9, 5, 8, 7, 7, 9, 7, 6, 6, 6, 8, 5, 5, 5, 9, 6, 7, 9, 5, 6, 9, 6, 6, 9, 8, 7, 7, 5, 9, 8, 7, 8, 6, 5, 7, 5, 5, 7, 6]

# the type of items in each order
types = [1, 0, 2, 2, 1, 1, 0, 2, 2, 1, 1, 0, 2, 2, 1, 1, 0, 2, 2, 1, 1, 0, 2, 2, 1, 1, 0, 2, 2, 1, 1, 0, 2, 2, 1, 1, 0, 2, 2, 1, 1, 0, 2, 2, 1, 1, 0, 2, 2, 1]

# length of rolls of each type
roll_lengths = [60, 40, 30]

# number of available rolls of each type
m = 30

assert(len(demands) == len(lengths) == len(types))
assert(max(types) == len(roll_lengths) - 1)
model = cuttingstock.solve(lengths, demands, types, m, roll_lengths)

print("Obj:", model.objVal)
for v in model.getVars():
	print(f"{v.varName}：{round(v.x,3)}")
