import parsing.file_parsing
import os


class File:
    ID = 0

    def __init__(self, name):
        self.name = name
        self.size = os.stat(name).st_size
        self.ID = File.ID
        self.imports = parsing.file_parsing.get_imports(name)
        self.functions_def = parsing.file_parsing.get_function_def(name)
        self.functions_calls = parsing.file_parsing.get_function_calls(name)

        File.ID += 1
