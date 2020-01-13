import parsing.file_parsing
import os


class File:
    ID = 0

    def __init__(self, name, module_name):
        self.name = name
        if module_name == 'global_scope':
            module_name = '.'
        self.size = os.stat(os.path.join(module_name, name)).st_size
        self.ID = File.ID
        if name not in ['diagram.png', 'diagram.uxf']:
            self.imports = parsing.file_parsing.get_imports(os.path.join(module_name, name))
            self.functions_def = parsing.file_parsing.get_function_def(os.path.join(module_name, name))
            self.functions_calls = parsing.file_parsing.get_function_calls(os.path.join(module_name, name))

        File.ID += 1
