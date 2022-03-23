import random
from The_Bin_Packing_Problem.Genetic.Bin import Bin
from The_Bin_Packing_Problem.Genetic.Item import Item
from The_Bin_Packing_Problem.Genetic.Chromosome import Chromosome
import math

class Generation:

    genes = list()          #Tuple of Bin and Item objects like gen(element) in genes(list)
    arrayPop = list()       #Population stored in array for quick access by index
    population = dict()     #HashSet to avoid duplicates in population

    k = 25                  # For k tournament selection
    crossover_prob = 85     # 0.85 cross-over probability, 85% chance
    mutation_prob = 10      # 0.1 mutation probability, 10% chance

    capacity = int()        # capacity
    genNumber = int()       # number og genes
    popSize = int()         # population size
    bestFit = Chromosome()  #Fittest chromosome in the population

    # Initialization
    # genes, capacity
    def __init__(self, *args):
        self.genes = args[0]
        self.capacity = args[1]
        self.popSize = int(math.pow(2, len(self.genes)) / int(math.pow(2, len(self.genes)) - 5))
        self.arrayPop = [Chromosome() for i in range(self.popSize)]

        index = 0
        chromo = Chromosome(self.capacity, self.genes)
        bestFit = chromo
        while (self.popSize != len(self.population)):
            chromo = Chromosome(self.capacity, self.genes)
            while (not (self.population.put(chromo))):
              chromo = Chromosome(self.capacity, self.genes)

            self.arrayPop.add(index, chromo);

            if (bestFit.compareTo(chromo) == -1):
                bestFit = chromo

            index += 1

        genNumber = 1;


    def generateNextGen(self):
        parents = list() # Can pick the same chromosome multiple times for reproduction(usually be the best fitness)
        #Selection of parents randomly by K-Way tournament

        while (parents.size() != self.popSize):
            index = (int)(math.random() * self.popSize);
            fittestChromosome = (Chromosome) (self.arrayPop.get(index))
            for i in range(0, self.k - 1):
                index = (int)(math.random() * self.popSize);
                if (fittestChromosome.compareTo(self.arrayPop.get(index)) == -1):
                    fittestChromosome = self.arrayPop.get(index)

            parents.add(fittestChromosome);



        return

    def getCrossOverPoint(self):
        return random.randint(0, self.genes.size())

    def crossOverMutationRate(self, probability):
        chance = random.randint(0,100)
        if (probability >= chance):
            return True
        else:
            return False

    def getGenNumber(self):
        return self.genes

    def getBestFit(self):
        return self.bestFit

