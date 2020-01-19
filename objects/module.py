import os
import objects.file

class Module:

    ID = 0

    def __init__(self, path, project):
        self.name = os.path.basename(os.path.normpath(path))
        self.path = path
        self.project = project
        self.ID = Module.ID
        self.files = []
        self.pars_for_files()
        Module.ID += 1

    def add_file(self, file_path):
        self.files.append(objects.file.File(file_path, self))

    def pars_for_files(self):

        if self.path != 'global_scope':
            for entry in os.listdir(self.path):
                if entry.endswith('.py') and entry != '__init__.py':
                    self.add_file(os.path.join(self.path, entry))
