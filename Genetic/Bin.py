#This needs to be changed
class Bin:
    def __init__(self, id, capacity, contents):
        self.id = id
        self.capacity = capacity
        self.contents = contents

    def getId(self):
        return self.id

    def getCapacity(self):
        return self.capacity

    def getContents(self):
        return self.contents