import pulp

solver_list = pulp.listSolvers(onlyAvailable=True)
print(solver_list)