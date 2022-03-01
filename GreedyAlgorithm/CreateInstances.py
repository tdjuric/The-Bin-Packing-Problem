import random

path = "C:\\Users\\Anel\\Desktop\\Faks\\3. Godina\\Operaciona Istraživanja\\Projekat\\The-Bin-Packing-Problem\\Instances\\"
for i in range(15):
    f = open(path + "small\\instance" + str(i) + ".txt", "w+")
    f.write("100\n")
    f.write("5000\n")
    for j in range(5000):
        f.write(str(random.randint(1, 100)) + "\n")

for i in range(15):
    f = open(path + "medium\\instance" + str(i) + ".txt", "w+")
    f.write("100\n")
    f.write("15000\n")
    for j in range(15000):
        f.write(str(random.randint(1, 100)) + "\n")

for i in range(15):
    f = open(path + "large\\instance" + str(i) + ".txt", "w+")
    f.write("100\n")
    f.write("45000\n")
    for j in range(45000):
        f.write(str(random.randint(1, 100)) + "\n")
