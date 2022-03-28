'''
0. Pocetna generacija se generise nasumicno nakon cega se FFD primjenjuje na jedinke koje imaju greske (prepunjenost) u binovima
    0.1. Item se vadi iz bina (stack) koji je prepunjen i stavlja u stack koji cemo s FFD rasporediti u skup binova
1. Dio prolazi selekcijom npr 30% ukupne pocetne generacije (30 jedinki pocetno)
2. Ostali dio se salje u crossover i vrti dok se ne dobiju validne jedinke (od dva nasumicna roditelja nastaju dvije nove jedinke) dok se ne dobije trazeni broj jedinki
3. Nakon sto se dobije validna jedinka Provjeravamo da li dolazi do mutacije te validne jednike
4. Ponovno sve
'''
import random

from The_Bin_Packing_Problem.Genetic.Individual import Individual


class GenerationNew:

    population_count = 30
    gen_count = 0
    population = []

    # TODO needs a constructor class that takes in Individuals list i.e. Individuals of a generation as argument

    def __init__(self, items, bin_capacity, item_count):
        self.items = items
        self.bin_capacity = bin_capacity
        self.item_count = item_count
        GenerationNew.gen_count += 1
        print("Generation number: " + str(GenerationNew.gen_count))
        self.doGeneration()
        print("Best fitness: ")


        i = GenerationNew.population[0].getFitness()
        for el in GenerationNew.population:
            print("EL fitness: ", el.getFitness())
            if (el.getFitness()>i):
                i = el.getFitness()
        print(i)

    def getPopulation(self):
        return GenerationNew.population

    def doGeneration(self):

        offspring_list = []
        # While our offspring are less than our current population count, create new offspring
        while (len(offspring_list) < self.population_count):

            # get parents
            mother = self.getParent()
            father = self.getParent()

            while (mother == father):
                father = self.getParent()

            # perform crossover

            offspring_a, offspring_b = self.generateOffspring(mother, father)

            offspring_list.append(offspring_a)
            offspring_list.append(offspring_b)

            # mutate

        # improving on the algorithm by mixing newly created gen with parents and selecting the best #population_count

        #self.population.extend(offspring_list)
        GenerationNew.population = offspring_list

        #self.population = sorted(self.population, key=lambda x: x.getFitness(), reverse=False)[:self.population_count]

        #print("Duzina: ", len(self.population))



    def generateOffspring(self, individual_a, individual_b):
        crossover_position = random.randint(1, len(individual_a.genes) - 1)
        offspring_a = self.doCrossover(individual_a, individual_b, crossover_position)
        offspring_b = self.doCrossover(individual_b, individual_a, crossover_position)

        return offspring_a, offspring_b

    def doCrossover(self, individual_a, individual_b, crossover_position):
        offspring_gene_sequence = individual_a.getGenes()[:crossover_position]
        offspring_gene_sequence.extend(individual_b.getGenes()[crossover_position:])

        return Individual(self.bin_capacity, self.item_count, self.items, offspring_gene_sequence)

    def getParent(self):

        return self.tournamentSelection()

    def tournamentSelection(self):

        candidate_1 = GenerationNew.population[random.randint(0, self.population_count - 1)]
        candidate_2 = GenerationNew.population[random.randint(0, self.population_count - 1)]

        while (candidate_1 == candidate_2):
            candidate_2 = GenerationNew.population[random.randint(0, self.population_count - 1)]

        if (candidate_1.getFitness() > candidate_2.getFitness()):
            return candidate_1
        else:
            return candidate_2

    def getGenCount(self):
        return GenerationNew.gen_count
