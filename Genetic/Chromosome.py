import random
from The_Bin_Packing_Problem.Genetic.Bin import Bin
from The_Bin_Packing_Problem.Genetic.Item import Item

class Chromosome:

    # Initialization
    # capacity of bin, list of bins, max_bins, *chromosome
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
            self.binAdjustment()
            self.setFitness()

        # TODO Used for intitializing a child chromosome
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


    def emptyBinGenerator(n, c):
        listOfEmptyBins = list()
        for i in range (n):
            listOfEmptyBins.append(Bin(i,c,0));
        return listOfEmptyBins

    def binAdjustment(self):
        temp_items = []
        print("Bin state before adjsutment")
        print(self.bins)
        for bin in self.bins:
            if (bin.fill > bin.capacity):
                while (bin.fill>bin.capacity):
                    temp_items.append(bin.removeElement())
        print("Bin state after taking out items")
        print(self.bins)
        if(temp_items):
            self.FFD(temp_items)
            self.chromosomeAdjustment()

    def chromosomeAdjustment(self):
        for bin in self.bins:
            if(bin.getContents()):
                for item in bin.getContents():
                    self.chromosome[item.getId()] = bin.getId()


    def FFD(self, items):
        sorted_items = sorted(items, key=lambda x: x.getValue(), reverse=True)
        for my_item in sorted_items:
            found_a_bin = False
            item_size = my_item.getValue()
            for my_bin in self.bins:
                if(item_size < (my_bin.getCapacity() - my_bin.getFill())):
                    my_bin.addElement(my_item)
                    print("ADDING ELEMENT TO BIN")
                    found_a_bin = True
                    break
            if found_a_bin == False:
                # it shouldn't come to this, and if it does something is really wrong
                print("Error!!!!")



b1 = Bin(0, 5, 0)
b2 = Bin(1, 5, 0)
b3 = Bin(2, 5, 0)
b4 = Bin(3, 5, 0)
b5 = Bin(4, 5, 0)

# Ovo cemo citati iz filea
items = [Item(0,5),Item(1,1), Item(2,3), Item(3,2), Item(4,4)]



for i in range (25):
    a = Chromosome(5, Bin.emptyBinGenerator(5,5), 5, items)
    print(a)
# Random redoslijed popunjavanja kanti
# a.setChromosome()
# Popunjavanje kanti po random redoslijedu
# a.fillBoxes()
# Odredivanje fitness funkcija chromosoma
# a.setFitness()





