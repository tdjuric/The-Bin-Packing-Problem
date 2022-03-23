import random
from The_Bin_Packing_Problem.Genetic.Bin import Bin
from The_Bin_Packing_Problem.Genetic.Item import Item

class Chromosome:

    # Initialization
    # capacity, list of bins, max_bins, *chromosome
    def __init__(self, *args):
        self.capacity = args[0]
        self.bins = args[1]
        self.max_bins = args[2]
        self.items = args[3]
        self.chromosome = []
        self.fitness = 0
        if len(args) == 4:
            print("Not a child chromosome")
            self.setChromosome()
            self.fillBins()
            self.setFitness()

        # Used for intitializing a child chromosome
        else:
            self.chromosome = args[4]
            #setFitness()


    def getChromosome(self):
        return self.chromosome

    # Fills the chromosome with 0
    def fillChromosome(self):
        for i in range(self.max_bins):
            self.chromosome.append(0)




    # Randomly populating chromosome List with the index of a bin they will be placed in
    def setChromosome(self):
        n = self.max_bins

        for i in range(n):
            place = random.randint(1, self.max_bins)
            self.chromosome.insert(i, place)
        random.shuffle(self.chromosome)

    # Filling bins with items according to the random chromosome list
    def fillBins(self):
        for i, el in enumerate (self.chromosome):
            self.bins[el-1].addElement(items[i])
            #self.bins[el-1].setFill((self.bins[el-1].getFill()) + (items[i]))


    #Fitness function
    def setFitness(self):
        k = 2
        n = 0
        for bin in self.bins:
            if (len(bin.contents) != 0):
                n+=1

        sum = 0
        for i, el in enumerate(self.bins):
            fill = el.getFill()
            capacity = el.getCapacity()

            value = (fill / capacity) **4
            sum += value
        print(n)
        self.fitness = sum / n



    def __repr__(self):
        s = "Capacity: " + str(self.capacity) + "\nBins: " + str(self.bins) + "\nChromosome list: " + str(self.chromosome) + "\n Fitness: " + str(self.fitness)
        return s


    def emptyBinGenerator(n):
        listOfEmptyBins = list()
        for i in range (n):
            listOfEmptyBins.append(Bin(i,0,0));
        return listOfEmptyBins

b1 = Bin(1, 5, 0)
b2 = Bin(2, 5, 0)
b3 = Bin(3, 5, 0)
b4 = Bin(4, 5, 0)
b5 = Bin(5, 5, 0)

# Ovo cemo citati iz filea
items = [Item(1,5),Item(2,1), Item(3,3), Item(4,2), Item(5,4)]

a = Chromosome(5, [b1, b2, b3, b4, b5], 5, items)


print(a)
# Random redoslijed popunjavanja kanti
# a.setChromosome()
# Popunjavanje kanti po random redoslijedu
# a.fillBoxes()
# Odredivanje fitness funkcija chromosoma
# a.setFitness()





