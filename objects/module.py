import os
import objects.file

class Module:

    ID = 0

    def __init__(self, name):
        self.name = name
        self.ID = Module.ID
        self.files = []
        self.list_files = pars_for_files(name)
        for f in self.list_files:
            self.files.append(objects.file.File(f))
        Module.ID += 1

def pars_for_files(dir):
    list_of_files = []

    if dir == 'global_scope':
        for r, d, f in os.walk("."):
            print(d)
         #   for fl in f:
        #        print(fl)
  #              list_of_files.append(fl)
    else:
        for r, d, f in os.walk(dir):
            for fl in f:
 #               print(fl)
                list_of_files.append(fl)

    return list_of_files