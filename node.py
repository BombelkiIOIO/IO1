class Node:

    ID = 0

    def __init__(self, name, internal_dependencies, external_dependencies):
        self.name = name
        self.internal_dependencies = internal_dependencies
        self.external_dependencies = external_dependencies
        self.ID = Node.ID
        Node.ID += 1
        
        #dictionary
        #list files from directory