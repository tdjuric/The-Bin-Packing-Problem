import random

path = "C:\\Users\\Tanja\\PycharmProjects\\The Bin Packing Problem\\"
for i in range(15):
    f = open(path + "instance1\\instance" + str(i) + ".txt", "w+")
    f.write("100\n")
    f.write("5000\n")
    for j in range(5000):
        f.write(str(random.randint(1, 100)) + "\n")

for i in range(15):
    f = open(path + "instance2\\instance" + str(i) + ".txt", "w+")
    f.write("100\n")
    f.write("25000\n")
    for j in range(25000):
        f.write(str(random.randint(1, 100)) + "\n")

for i in range(15):
    f = open(path + "instance3\\instance" + str(i) + ".txt", "w+")
    f.write("100\n")
    f.write("500000\n")
    for j in range(500000):
        f.write(str(random.randint(1, 100)) + "\n")
