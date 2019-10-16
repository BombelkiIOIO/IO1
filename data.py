import file_parsing
import node
import os
import re

def make_list_all_source_files(root_dir):
    list_of_files = []

    for r, d, f in os.walk(root_dir):
        for file in f:
            if re.search("\.py$", file):
                 list_of_files.append(os.path.join(r,file))

    return list_of_files

def prepare_data_to_visualisation(root_dir):
    files_to_check = make_list_all_source_files(root_dir)
    nodes = []

    for f in files_to_check:
        dependencies = file_parsing.pars(f)
        internal_dependencies = []
        external_dependencies = []
        for a in dependencies:
            if any(a[0] in n for n in files_to_check):
                internal_dependencies.append(a)
            else:
                external_dependencies.append(a)
        newNode = node.Node(f, internal_dependencies, external_dependencies, os.path.getsize(f))
        nodes.append(newNode)

    return nodes
