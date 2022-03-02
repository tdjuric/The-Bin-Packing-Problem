import random
path = "C:\\Users\\Anel\\Desktop\\Faks\\3. Godina\\Operaciona Istraživanja\\Projekat\\The_Bin_Packing_Problem\\Pulp\\"
f = open(path + "instance.txt", "w+")
f.write("100\n")
f.write("500\n")
for j in range(500):
    f.write(str(random.randint(1, 100)) + "\n")