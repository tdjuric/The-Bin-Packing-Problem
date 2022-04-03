import math

def devijacija(srednja_vrijednost, broj_instanci, list_of_values):
    temp = 0
    for el in list_of_values:
        temp += ((el - srednja_vrijednost) ** 2)

    under = temp / (broj_instanci-1)
    return round(math.sqrt(under),3)
f = open("C:\\Users\\Anel\\Desktop\\Faks\\3. Godina\\Operaciona Istraživanja\\Projekat\\The_Bin_Packing_Problem\\GeneticResults\\GeneticTestResults0.txt")
print((f.readline()))
list_of_lists = []
for i in range (10):
    small = []
    medium = []
    large = []
    f = open(
        "C:\\Users\\Anel\\Desktop\\Faks\\3. Godina\\Operaciona Istraživanja\\Projekat\\The_Bin_Packing_Problem\\GeneticResults\\GeneticTestResults" + str(i) + ".txt")
    f.readline()
    # small
    for i in range (15):
        a,b,c = f.readline().split()
        temp = (a,b,c)
        small.append(temp)
    f.readline()
    # medium
    for i in range (15):
        a,b,c = f.readline().split()
        temp = (a,b,c)
        medium.append(temp)
    f.readline()
    # large
    for i in range (15):
        a,b,c = f.readline().split()
        temp = (a,b,c)
        large.append(temp)

    temp_list= [small, medium, large]
    list_of_lists.append(temp_list)

print(list_of_lists)

list = []
average_result = 0
average_time = 0
best_result = 2500
for i in range (10):
    f = open(
        "C:\\Users\\Anel\\Desktop\\Faks\\3. Godina\\Operaciona Istraživanja\\Projekat\\The_Bin_Packing_Problem\\GeneticResults\\GeneticTestResults" + str(
            i) + ".txt")
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()

    a,b,c = f.readline().split()
    print(b)
    if int(b) < int(best_result):
        best_result = int(b)
    average_result += int(b)
    average_time += float(c)
    list.append(int(b))
print("\n")
print("\n")
print("\n")
print("\n")

final_result = average_result / 10
final_time = average_time / 10
print("Best: ", best_result)
print("Average: ", final_result)
print("Devijacija", devijacija(final_result,10,list))
print("Time: ", round(final_time,3))
#print(list)
