#This needs to be changed
class Bin:
    def __init__(self, id, capacity, fill):
        self.id = id
        self.capacity = capacity
        self.fill = fill
        self.contents = []

    def getId(self):
        return self.id

    def getFill(self):
        return self.fill

    def setFill(self, fill):
        self.fill = fill

    def getCapacity(self):
        return self.capacity

    def getContents(self):
        return self.contents

    def addElement(self, element):
        self.contents.append(element)

    def __repr__(self):
        s = "Id: " + str(self.id) + ", Capacity: " + str(self.capacity) + ", Contents: " + str(self.contents)
        return s