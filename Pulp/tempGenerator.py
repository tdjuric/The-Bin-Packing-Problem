import random
path = "C:\\Users\\Anel\\Desktop\\Faks\\3. Godina\\Operaciona Istraživanja\\Projekat\\The_Bin_Packing_Problem\\Pulp\\"
f = open(path + "instance.txt", "w+")
f.write("50\n")
f.write("100\n")
for j in range(100):
    f.write(str(random.randint(1, 50)) + "\n")