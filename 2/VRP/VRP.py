from gurobipy import *

def solve(V, A, a, b, c, d, m):
    # The number of customers
    n = len(V)

    model = Model('VRP')

    # DO NOT RENAME these variables
    # t[i,k] depicts the time of arrival of the vehicle k at the customer i or the depot (i = 0)
    t = model.addVars(n, m, vtype=GRB.CONTINUOUS, name='t')
    z = dict()
    x = dict()

    for k in range(m):
        for i,j in A:
            # x[i,j,k] determines whether the edge (i,j) has been used by the vehicle k or not
            x[i,j,k] = model.addVar(vtype=GRB.BINARY, name=f'x[{i},{j},{k}]')

        for i in V[1:]:
            # z[i,k] depicts whether the customer i has been visited by the vehicle k
            z[i,k] = model.addVar(vtype=GRB.BINARY, name=f'z[{i},{k}]')

    # If necessary, add further variables below

    Max_value = 99999

    # If necessary, define the objective function below
    model.setObjective(
        quicksum(c[i, j] * x[i, j, k] for k in range(m) for i, j in A)
    )

    # If necessary, add constraints to the model below

    for k in range(m):
        for v in V[1:]:
            model.addConstr(quicksum(x[i,j,k] for i,j in A if i == v) == z[i,k])

    for k in range(m):
        for v in V[1:]:
            model.addConstr(quicksum(x[i,j,k] for i,j in A if j == v) == z[j,k])

    for i in range(1,n):
        model.addConstr(quicksum(z[i,k] for k in range(m)) == 1)

    for i in range(1,n):
        for k in range(m):
            model.addConstr(a[i] <= t[i,k])
            model.addConstr(t[i,k] <= b[i])

    for i,j in A:
        for k in range(m):
            if (j != 0 ):
                model.addConstr((t[i, k] + d[i,j]) <= (t[j, k] + Max_value * (1 - x[i,j,k])))

    model.update()
    model.optimize()

    return model