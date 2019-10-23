import re
import os
import itertools as iter


def pars(file_name):
    if os.path.isfile(file_name):
        line = []
        line1 = []
        names_of_files = []
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


def get_list_of_defined_functions(file_name):
    if os.path.isfile(file_name):
        all_functions = []
        with open(file_name) as file:
            for x in file:
                if re.search("[ *]def", x) is not None:
                    all_functions.append(re.search("def (.*)[(]", x).group(1))
                elif x.startswith('def'):
                    all_functions.append(re.search("def (.*)[(]", x).group(1))
        return all_functions
    else:
        print("File does not exist!")
        return None


def find_and_read_function(file_name, function_name):
    lines = []
    if os.path.isfile(file_name):
        with open(file_name) as file:
            for x, line in enumerate(file):
                if re.search("def (.*)[(]", line) is not None and re.search("def (.*)[(]", line).group(
                        1) == function_name:
                    break
        with open(file_name) as file:
            skipped = iter.islice(file, x + 1, None)
            for i, line in enumerate(skipped, x + 1):
                if line.startswith('def'):
                    break
                lines.append(line)
        return lines
    else:
        print("File does not exist!")
        return None


def pars_for_functions(file_name, function_name):
    if os.path.isfile(file_name):
        line = []
        functions = []
        functions1 = []
        file = find_and_read_function(file_name, function_name)
        for x in file:
            if re.search("[.](.*)[(]", x) or re.search("(.*)[(].*[)]", x):
                line.append(x)
        for x in line:
            split1 = re.split("[.)=]", x)
            for y in split1:
                if re.search("(\w*)[(]", y) is not None:
                    functions.append(re.search("(\w*)[(]", y).group(1))
        for z in functions:
            if re.search("(\w*)[(]", z) is not None:
                functions1.append(re.search("(\w*)[(]", z).group(1))
            else:
                functions1.append(z)
        str_list = list(filter(None, functions1))
        unique_set = list(set(str_list))
        dictionary = dict((k, 0) for k in unique_set)

        for x in str_list:
            if x in dictionary:
                dictionary[x] = dictionary[x] + 1
        final_result = [(k, v) for k, v in dictionary.items()]

        return final_result
