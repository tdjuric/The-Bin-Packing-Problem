import pulpSolver as pulpSolver

path = "C:\\Users\\Tanja\\Desktop\\Projekat iz OI\\The_Bin_Packing_Problem\\"
import timeit

#pulpSolver.run("C:\\Users\\Tanja\\Desktop\\Projekat iz OI\\The_Bin_Packing_Problem\\")

print("Solving small instances...")
for i in range(15):

    print(pulpSolver.run(path, "Instances\\small\\instance" + str(i) + ".txt"))
   # t = pulpSolver.run(path, "Instances\\small\\instance" + str(i) + ".txt")
   # print("Time to solve instance" + str(i) + ": " + str(t.time))

print("Solving medium instances...")
for i in range(15):
        pulpSolver.run(path, "Instances\\medium\\instance" + str(i) + ".txt")
       # t = pulpSolver.run(path, "Instances\\medium\\instance" + str(i) + ".txt")
       # print("Time to solve instance" + str(i) + ": " + str(t.timeit(number=1)))

print("Solving large instances...")
for i in range(15):
        pulpSolver.run(path, "Instances\\large\\instance" + str(i) + ".txt")
       # t = pulpSolver.run(path, "Instances\\large\\instance" + str(i) + ".txt")
       # print("Time to solve instance" + str(i) + ": " + str(t.time))











