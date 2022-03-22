import random
class Generation:

    k = 25 # For k tournament selection
    crossover_prob = 85
    mutation_prob = 10
    def __init__(self):


    def generateNextGen(self):
        #volim
    def getCrossOverPoint(self):
        return random.randint(0, self.genes.size())

    def crossOverMutationRate(self, probability):
        chance = random.randint(0,100)
        if (probability >= chance):
            return True
        else:
            return False