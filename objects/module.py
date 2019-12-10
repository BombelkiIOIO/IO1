import os
import objects.file

class Module:

    ID = 0

    def __init__(self, name):
        self.name = name
        self.ID = Module.ID
        self.list_files = pars_for_files(name)
#        for f in self.list_files:
#            self.files.append(objects.file.File(f))
        Module.ID += 1

def pars_for_files(dir):
    list_of_files = []

    if dir == 'global_scope':
        i = 0
        for r, d, f in os.walk("."):
            if i == 0:
                j = 0
                for fl in f:
                    if j == 0:
                        print(fl)
                    j += 1
#list_of_files.append(fl)
            i += 1
    else:
        for r, d, f in os.walk(dir):
            pass#print(dir)
            for fl in f:
                pass
              #  print(r)
             #   list_of_files.append(fl)

    return list_of_files