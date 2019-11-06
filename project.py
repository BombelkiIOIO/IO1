import data
import file_parsing


class Project:
    def __init__(self, name):
        self.name = name
        self.functions = []
        self.files = data.prepare_data_to_visualisation(name)    #temporary solution, now listing only .py files
        self.add_functions_to_files()

    def add_functions_to_files(self):
        for fl in self.files:
            self.functions += file_parsing.get_list_of_defined_functions(fl)
