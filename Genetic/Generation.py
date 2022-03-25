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
from The_Bin_Packing_Problem.Genetic.Chromosome import Chromosome
import math
import time

class Generation:



    # Inicijalizacija
    # genes, capacity
    def __init__(self, *args):
        #in progress
       return

    def generateNextGen(self):
        # in progress 
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

