import objects.function
import parsing.file_parsing
import os


class File:
    ID = 0

    def __init__(self, path, module):
        self.path = path
        self.name = os.path.basename(path)
        self.module = module
        self.size = os.stat(self.path).st_size
        self.ID = File.ID
        self.imports = parsing.file_parsing.get_imports(path)
        self.functions_calls = parsing.file_parsing.get_function_calls(path)
        self.functions = [objects.function.Function(x, self) for x in parsing.file_parsing.get_function_def(path)]
        File.ID += 1

    def get_internal_dependencies(self):
        modules_names = [x.name for x in self.module.project.modules]
        return [x for x in self.imports if x.split('.')[0] in modules_names]
