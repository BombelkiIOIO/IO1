import os
import objects.file

class Module:

    ID = 0

    def __init__(self, name, project):
        self.name = name
        self.project_name = project
        self.ID = Module.ID
        self.files = []
        self.list_files = pars_for_files(name)
        for f in self.list_files:
            self.files.append(objects.file.File(f, self))
        Module.ID += 1

def pars_for_files(dir):
    list_of_files = []

    if dir == 'global_scope':
        i = 0
        for r, d, f in os.walk("."):
            if i == 0:
                for fl in f:
                    if fl == 'Application.py':    #temp solution, won't works for other app
                        list_of_files.append(fl)
            i += 1
    else:
        for r, d, f in os.walk(dir):
            if 'docs' in r or 'test' in r or '__pycache__' in d:
                list_of_files += f

    return list_of_files
