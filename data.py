import file_parsing
import node
import os
import re

def make_list_all_source_files():
    list_of_files = []
    root_dir = '.'

    for r, d, f in os.walk(root_dir):
        for file in f:
            if re.search("\.py$", file):
                 list_of_files.append(os.path.join(r,file))

    return list_of_files

def prepare_data_to_visualisation():
    files_to_check = make_list_all_source_files()
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

##just to visualize output, to remove in final version
    for n in nodes:
        print("node: " + str(n.ID) + " name: " + n.name + " size: " + str(n.size) + " bytes"+ "\n" + "internal dependencies:\n" + str(n.internal_dependencies) + "\nexternal dependencies:\n" + str(n.external_dependencies))
        print("\n\n")

    return nodes

prepare_data_to_visualisation()