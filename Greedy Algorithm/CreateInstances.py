import random

path = "C:\\Users\\PC\\Desktop\\OI projekat\\PythonFirstFitD\\"
for i in range(15):
    f = open(path + "instance1\\instance" + str(i) + ".txt", "w+")
    f.write("100\n")
    f.write("10000\n")
    for j in range(10000):
        f.write(str(random.randint(1, 100)) + "\n")

for i in range(15):
    f = open(path + "instance2\\instance" + str(i) + ".txt", "w+")
    f.write("100\n")
    f.write("500000\n")
    for j in range(500000):
        f.write(str(random.randint(1, 100)) + "\n")

for i in range(15):
    f = open(path + "instance3\\instance" + str(i) + ".txt", "w+")
    f.write("100\n")
    f.write("1000000\n")
    for j in range(1000000):
        f.write(str(random.randint(1, 100)) + "\n")
