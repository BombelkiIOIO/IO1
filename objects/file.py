import sys
class File:

    ID = 0

    def __init__(self, name):
        self.name = name
        self.size = 0    #todo
        self.ID = File.ID
        File.ID += 1