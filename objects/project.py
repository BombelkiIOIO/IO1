import objects.module
import os


class Project:
    def __init__(self, name, root_dir):
        self.name = name
        self.path = root_dir
        self.modules = []
        self.pars_for_modules()

    def pars_for_modules(self):
        self.modules.append(objects.module.Module('global_scope', self))

        for root, dirs, files in os.walk(self.path):
            if not os.path.basename(os.path.normpath(root)) == '.':
                files = [f for f in files if not f[0] == '.']
                dirs[:] = [d for d in dirs if not d[0] == '.']
                if "__init__.py" in files:
                    self.modules.append(objects.module.Module(root, self))
                else:
                    for file in files:
                        if file.endswith(".py"):
                            self.modules[0].add_file(os.path.join(root, file))

    def get_functions(self):
        return [fun for module in self.modules for file in module.files for fun in file.functions]

    def get_files(self):
        return [file for module in self.modules for file in module.files]
