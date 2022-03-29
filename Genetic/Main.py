from Item import Item
from Individual import Individual
from GenerationNew import GenerationNew
import The_Bin_Packing_Problem.FileManipulation.ReadInInstances as ReadInInstances

# items = [Item(0, 5), Item(1, 1), Item(2, 3), Item(3, 2), Item(4, 4)]

path = "C:\\Users\\Tanja\\Desktop\\Projekat iz OI\\The_Bin_Packing_Problem\\Instances\\"
#path = "C:\\Users\\PC\\Desktop\\OI projekat\\ProjectPython\\The_Bin_Packing_Problem\\Instances\\"

bin_capacity, item_count, dict = ReadInInstances.readInInstances(path + "instance.txt")
print("Bin cap", bin_capacity)
print("Item count ", item_count)
items = []

for i in range (item_count):
    items.append(Item(i,dict["item" + str(i+1)]))



initial_individuals = []
for i in range(GenerationNew.population_count):
    initial_individuals.append(Individual(bin_capacity, item_count, items))

#print(initial_individuals)

#print("We are in main")
GenerationNew.population = initial_individuals
g = GenerationNew(items, bin_capacity, item_count)
#print(g.getPopulation())
for GenerationNew.gen_count in range (100):
    g = GenerationNew(items, bin_capacity, item_count)

print(g.population[0].getFullBinCount())
 #  print(g)