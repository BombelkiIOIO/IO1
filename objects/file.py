class File:

    ID = 0

    def __init__(self, name, internal_dependencies, external_dependencies, size):
        self.name = name
        self.internal_dependencies = internal_dependencies
        self.external_dependencies = external_dependencies
        self.size = size
        self.ID = File.ID
        File.ID += 1
