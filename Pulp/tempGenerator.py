import random
#path = "C:\\Users\\Anel\\Desktop\\Faks\\3. Godina\\Operaciona Istraživanja\\Projekat\\The_Bin_Packing_Problem\\Pulp\\"
path = "C:\\Users\\PC\\Desktop\\OI projekat\\ProjectPython\\The_Bin_Packing_Problem\\Pulp\\"
f = open(path + "instance.txt", "w+")
f.write("10\n")
f.write("30\n")
for j in range(30):
    f.write(str(random.randint(1, 10)) + "\n")