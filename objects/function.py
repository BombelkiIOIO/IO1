import parsing.file_parsing


class Function:

    ID = 0

    def __init__(self, name, file):
        self.name = name
        self.file = file
        self.function_calls = parsing.file_parsing.get_function_calls(file.path, name)
        self.ID = Function.ID
        Function.ID += 1

    def get_internal_dependencies(self):
        return [fun for fun in self.function_calls if fun in [x.name for x in self.file.module.project.get_functions()]]


