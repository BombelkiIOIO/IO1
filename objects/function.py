class Function:

    ID = 0

    def __init__(self, name, file, internal_dependencies, external_dependencies):
        self.name = name
        self.file = file
        self.internal_dependencies = internal_dependencies
        self.external_dependencies = external_dependencies
        self.ID = Function.ID
        Function.ID += 1