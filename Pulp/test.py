<<<<<<< HEAD
import pulp
pulp.pulpTestAll()
=======



import pulp
maxBins = 32


items = [("a", 5),
         ("b", 6),
         ("c", 7),
         ("d", 32),
         ("e", 2),
         ("f", 32),
         ("g", 5),
         ("h", 7),
         ("i", 9),
         ("k", 12),
         ("l", 11),
         ("m", 1),
         ("n", 2)]


y = pulp.LpVariable.dicts('BinUsed', range(maxBins),
                            lowBound = 0,
                            upBound = 1,
                            cat = pulp.LpInteger)

print(y)
# An indicator variable that is assigned 1 when item is placed into binNum
possible_ItemInBin = [(itemTuple[0], binNum) for itemTuple in items
                                            for binNum in range(maxBins)]


x = pulp.LpVariable.dicts('itemInBin', possible_ItemInBin,
                            lowBound = 0,
                            upBound = 1,
                            cat = pulp.LpInteger)

print(x)
>>>>>>> e8616f8b367f044bc2edf019bfa4325c4aacba60
