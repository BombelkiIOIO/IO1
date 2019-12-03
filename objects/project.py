import data.data
import parsing.file_parsing
import objects.module
import os


class Project:
    def __init__(self, name, root_dir):
        self.name = name
        self.modules = []
        self.list_modules = pars_for_modules(root_dir)
        for m in self.list_modules:
            self.modules.append(objects.module.Module(m))

def pars_for_modules(root_dir):
    list_of_modules = ['global_scope']

    for r, d, f in os.walk(root_dir):
        if '.git' not in r:
            if 'venv' not in r:
                for mod in d:
                    if '.git' not in mod:
                        if 'venv' not in mod:
                            if '__pycache__' not in mod:
                                if '.idea' not in mod:
                                    list_of_modules.append(mod)

    return list_of_modules