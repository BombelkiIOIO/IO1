import re
import os

def pars(file_name):
    line = []
    line1 = []
    names_of_files = []
    if os.path.isfile(file_name):
        # Open file and get dependency
        with open(file_name) as file:
            for x in file:
                if x.startswith('import') | x.startswith('from'):
                    line.append(x)

        for l in line:
            if re.search("as (.*)\n", l) is not None:
                names_of_files.append(re.search("as (.*)\n", l).group(1))
            elif re.search("import (.*)", l) is not None:
                names_of_files.append(re.search("import (.*)\n", l).group(1))
        # Create dictionary of a dependencies
        unique_set = list(set(names_of_files))
        dictionary = dict((k, 0) for k in unique_set)
        # Count occurrence of dependencies
        with open(file_name) as file:
            for x in file:
                line1.append(re.findall(r"[\w]+", x))
            for x in line1:
                for y in x:
                    if y in dictionary:
                        dictionary[y] = dictionary[y] + 1
        # Convert dictionary to list of tuples
        final_result = [(k, v) for k, v in dictionary.items()]
        return final_result
    else:
        print("File does not exist!")
        return None