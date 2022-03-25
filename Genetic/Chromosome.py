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
            place = random.randint(0, self.max_bins-1)
            self.chromosome.insert(i, place)
        random.shuffle(self.chromosome)

    # Filling bins with items according to the random chromosome list
    def fillBins(self):
        for i, el in enumerate (self.chromosome):
            self.bins[el-1].addElement(items[i])
            #self.bins[el-1].setFill((self.bins[el-1].getFill()) + (items[i]))


    #Fitness function
    def setFitness(self):
        k = 4
        n = 0
        for bin in self.bins:
            if (len(bin.contents) != 0):
                n+=1

        sum = 0
        for i, el in enumerate(self.bins):
            fill = el.getFill()
            capacity = el.getCapacity()

            value = (fill / capacity) **k
            sum += value
        self.fitness = sum / n

    def binAdjustment(self):
        temp_items = []
        print(self.bins)
        for bin in self.bins:
            if (bin.fill > bin.capacity):
                while (bin.fill>bin.capacity):
                    temp_items.append(bin.removeElement())
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
                    found_a_bin = True
                    break
            if found_a_bin == False:
                # it shouldn't come to this, and if it does something is really wrong
                print("Error!!!!")

    def __repr__(self):
        s = "Capacity: " + str(self.capacity) + "\nBins: " + str(self.bins) + "\nChromosome list: " + str(
            self.chromosome) + "\nFitness: " + str(self.fitness) + "\n"
        return s


# Ovo cemo citati iz filea
items = [Item(0,5),Item(1,1), Item(2,3), Item(3,2), Item(4,4)]

for i in range (30):
    a = Chromosome(5, Bin.emptyBinGenerator(5,5), 5, items)
    print(a)





