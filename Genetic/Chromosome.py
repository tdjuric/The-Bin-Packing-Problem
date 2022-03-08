import random
class Chromosome:

    # Initialization
    def __init__(self, *args):
        self.capacity = args[0]
        self.quota = args[1]
        self.bins = args[2]
        self.chromosome = []
        if len(args) == 3:
            print("hi")
            #fillChromosome()
            #setChromosome()

        # Used for intitializing a child chromosome
        else:
            self.chromosome = args[3]
            #setFitness()

    '''
    def __init__(self, capacity, quota, bins, chromosome):
        self.capacity = capacity
        self.quota = quota
        self.bins = bins
        self.chromosome = chromosome
        #setFitness()
    '''

    # Fills the chromosome with 0
    def fillChromosome(self):
        for i in range(len(self.bins)):
            self.chromosome.append(0)

    def getChromosome(self):
        return self.chromosome

    # Randomly populating chromosome List with 1 and 0
    def setChromosome(self):
        n = self.randomNumberOfBoxes()
        while (n==0):
            n = self.randomNumberOfBoxes()

        for i in range(n):
            self.chromosome.insert(i, 1)
        random.shuffle(self.chromosome)
        self.setFitness

    def randomNumberOfBoxes(self):
        return random.randint(len(self.bins)+1)


    #Fitness function
    def setFitness(self):
        k = 2
        n = len(self.bins)
        sum = 0
        for i, el in enumerate (self.bins):
            fill = el.getFill()
            capacity = el.getCapacity()

            value = (fill / capacity) ^ k
            sum += value

        return sum / n



    def __repr__(self):
        s = "Capacity: " + str(self.capacity) + "\nQuota: " + str(self.quota) + "\nBins: " + str(self.bins) + "\nChromosome list: " + str(self.chromosome)
        return s

a = Chromosome(5,5,[1,2,3,4,5,6], [])
print(a)
a.fillChromosome()
print(a)





