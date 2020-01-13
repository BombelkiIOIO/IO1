import parsing.file_parsing
import objects.file
import objects.function
import os
import re

"""def make_list_all_source_files(root_dir):
    list_of_files = []

    for r, d, f in os.walk(root_dir):
        if '.git' not in r:
            if 'venv' not in r:
                for file in f:
                    if re.search("\.py$", file):
                        list_of_files.append(file)

    return list_of_files
"""

def prepare_data_to_visualisation(root_dir):
    files_to_check = make_list_all_source_files(root_dir)
    files = []

    for f in files_to_check:
        dependencies = parsing.file_parsing.pars(f)
        internal_dependencies = []
        external_dependencies = []
        for a in dependencies:
            if any(a[0] in n for n in files_to_check):
                internal_dependencies.append(a)
            else:
                external_dependencies.append(a)
        new_file = objects.file.File(f, internal_dependencies, external_dependencies, os.path.getsize(f))
        files.append(new_file)

    return files

def prepare_functions_data_to_visualisation(root_dir):
    files_to_check = make_list_all_source_files(root_dir)
    functions = []

    for fl in files_to_check:
        functions_to_check = parsing.file_parsing.get_list_of_defined_functions(fl)
        for fnctn in functions_to_check:
            dependencies = parsing.file_parsing.pars_for_functions(fl, fnctn)
            internal_functions_dependencies = []
            external_functions_dependencies = []
            for a in dependencies:
                if any(a[0] == n for n in functions_to_check):
                    internal_functions_dependencies.append(a)
                else:
                    external_functions_dependencies.append(a)
            new_function = objects.function.Function(fnctn, fl, internal_functions_dependencies, external_functions_dependencies)
            functions.append(new_function)

    return functions