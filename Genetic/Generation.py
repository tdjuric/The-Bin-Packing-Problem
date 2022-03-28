'''
0. Pocetna generacija se generise nasumicno nakon cega se FFD primjenjuje na jedinke koje imaju greske (prepunjenost) u binovima
    0.1. Item se vadi iz bina (stack) koji je prepunjen i stavlja u stack koji cemo s FFD rasporediti u skup binova
1. Dio prolazi selekcijom npr 30% ukupne pocetne generacije (30 jedinki pocetno)
2. Ostali dio se salje u crossover i vrti dok se ne dobiju validne jedinke (od dva nasumicna roditelja nastaju dvije nove jedinke) dok se ne dobije trazeni broj jedinki
3. Nakon sto se dobije validna jedinka Provjeravamo da li dolazi do mutacije te validne jednike
4. Ponovno sve
'''



import random
from The_Bin_Packing_Problem.Genetic.Bin import Bin
from The_Bin_Packing_Problem.Genetic.Item import Item
from The_Bin_Packing_Problem.Genetic.Individual import Individual
import math
import time

class Generation:

    genes = list()          # Tuple  Bin and Item objekata kao element gen u lsiti genes
    arrayPop = list()       # Populacija je pohranjena u nizu za brzi pristup po indeksu
    population = dict()     # HashSet za izbjegavanje duplikata u populaciji

    k = 25                  # Za k turnirsku selekciju
    crossover_prob = 85     # 0.85 cross-over vjerovatnoca, 85% sanse
    mutation_prob = 10      # 0.1 mutation vjerovatnoca, 10% sanse

    capacity = int()        # kapacitet
    genNumber = int()       # beoj generacija
    popSize = int()         # velicina populacije
    bestFit = Individual()  # Hromozom sa najboljom prilagodjenosti u populaciji

    # Inicijalizacija
    # genes, capacity
    def __init__(self, *args):
        self.genes = args[0]
        self.capacity = args[1]
        self.popSize = int(math.pow(2, len(self.genes)) / int(math.pow(2, len(self.genes)) - 5))
        self.arrayPop = [Individual() for i in range(self.popSize)]


        index = 0
        chromo = Individual(self.capacity, self.genes)
        bestFit = chromo
        while (self.popSize != len(self.population)):
            chromo = Individual(self.capacity, self.genes)
            while (not (self.population.put(chromo))):
              chromo = Individual(self.capacity, self.genes)

            self.arrayPop.add(index, chromo);

            if (bestFit.compareTo(chromo) == -1):
                bestFit = chromo

            index += 1

        self.genNumber = 1;


    def generateNextGen(self):
        parents = list() # Može odabrati isti hromosom više puta za reprodukciju
        # Odabir roditelja nasumično po K-tom turniru

        while (parents.size() != self.popSize):
            index = (int)(math.random() * self.popSize);
            fittestChromosome = (Individual) (self.arrayPop.get(index))
            for i in range(0, self.k - 1):
                index = (int)(math.random() * self.popSize);
                if (fittestChromosome.compareTo(self.arrayPop.get(index)) == -1):
                    fittestChromosome = self.arrayPop.get(index)

            parents.add(fittestChromosome);

        seed = time.time_ns();
        new_random = random(seed)
        random.shuffle(parents, new_random);

        self.population.clear();
        self.arrayPop.clear();




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

