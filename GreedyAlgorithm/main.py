import GreedyAlgorithm.firstFitDecreasing as firstFitDecreasing
import timeit

path = "C:\\Users\\Anel\\Desktop\\Faks\\3. Godina\\Operaciona Istraživanja\\Projekat\\The-Bin-Packing-Problem\\Instances\\"


##temp test
'''
bin_size, number_of_instances, dict = firstFitDecreasing.readInInstances(path + "small\instance0.txt")
print("Bin size: " + str(bin_size))
print("Number of Instances: " + str(number_of_instances))
#print("Instances: " + str(dict))
#print(len(firstFitDecreasing.first_fit_decreasing_algorithm(dict, bin_size, return_sizes=True)))
'''


##main timer function implementation

def f1(dict,bin_size):
    firstFitDecreasing.first_fit_decreasing_algorithm(dict, bin_size, return_sizes=False)

for i in range (15):
    bin_size, number_of_instances, dict = firstFitDecreasing.readInInstances(path + "small\instance" +str(i)+ ".txt")
    #print(len(firstFitDecreasing.first_fit_decreasing_algorithm(dict, bin_size, return_sizes=True)))
    t = timeit.Timer(lambda: f1(dict, bin_size))
    print("Time to solve instance" + str(i) + ": " + str(t.timeit(number=1)))
