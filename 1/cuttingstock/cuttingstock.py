from gurobipy import *


def solve(lengths, demands, types, m, roll_lengths):
    # The number of orders
    n = len(demands)

    # The number of roll types
    t = len(roll_lengths)

    model = Model('Сutting stock')

    # Add the necessary attributes to the variables defined below. DO NOT RENAME these variables
    # x[i,j,k] depicts the number of items cut for the order i from the roll j of type k
    x = model.addVars(n, m, t, vtype=GRB.INTEGER, name='x')

    # y[j,k] defines whether the roll j of type k has been used  
    y = model.addVars(m, t, vtype=GRB.BINARY, name='y', obj=1)

    # If necessary, add further variables below

    # If necessary, define the objective function below

    # If necessary, add constraints to the model below
    for i in range(0,n):
        model.addConstr(quicksum(x[i,j,types[i]] for j in range(0,m)) >= demands[i])

    for j in range(0,m):
        for k in range(0,t):
            model.addConstr(quicksum(lengths[i] * x[i,j,k] for i in range(0,n)) <= roll_lengths[k] * y[j,k])

    model.update()
    model.optimize()

    # Do not modify the code below this line
    return model
