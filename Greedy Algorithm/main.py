import firstFitDecreasing as firstFitDecreasing
import timeit

path = "C:\\Users\\Tanja\\PycharmProjects\\The Bin Packing Problem\\"
bin_size, number_of_instances, dict = firstFitDecreasing.readInInstances(path + "instance3\instance0.txt")
print("Bin size: " + str(bin_size))
print("Number of Instances: " + str(number_of_instances))
#print("Instances: " + str(dict))

#print(len(firstFitDecreasing.first_fit_decreasing_algorithm(dict, bin_size, return_sizes=True)))


def f1(dict,bin_size):
    firstFitDecreasing.first_fit_decreasing_algorithm(dict, bin_size, return_sizes=False)

for i in range (1):
    bin_size, number_of_instances, dict = firstFitDecreasing.readInInstances(path + "instance3\instance" +str(i)+ ".txt")
    print(len(firstFitDecreasing.first_fit_decreasing_algorithm(dict, bin_size, return_sizes=True)))
    t = timeit.Timer(lambda: f1(dict, bin_size))
    print(t.timeit(number=1))
