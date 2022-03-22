import random
#path = "C:\\Users\\Tanja\\Desktop\\Projekat iz OI\\The_Bin_Packing_Problem\\Instances\\"
path = "C:\\Users\\Anel\\Desktop\\Faks\\3. Godina\\Operaciona Istraživanja\\Projekat\\The_Bin_Packing_Problem\\Instances\\"
#path = "C:\\Users\\PC\\Desktop\\OI projekat\\ProjectPython\\The_Bin_Packing_Problem\\Instances\\"
for i in range(15):
    f = open(path + "small\\instance" + str(i) + ".txt", "w+")
    f.write("200\n")
    f.write("500\n")
    for j in range(500):
        f.write(str(random.randint(1, 200)) + "\n")

for i in range(15):
    f = open(path + "medium\\instance" + str(i) + ".txt", "w+")
    f.write("200\n")
    f.write("1500\n")
    for j in range(1500):
        f.write(str(random.randint(1, 200)) + "\n")

for i in range(15):
    f = open(path + "large\\instance" + str(i) + ".txt", "w+")
    f.write("200\n")
    f.write("4500\n")
    for j in range(4500):
        f.write(str(random.randint(1, 200)) + "\n")
