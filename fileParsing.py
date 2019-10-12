import pandas as pd
import re
import numpy as np
import os


def pars(file_name):
    line = []
    names_of_files = []
    if os.path.isfile(file_name):
        with open(file_name) as file:
            for x in file:
                if x.startswith('import') | x.startswith('from'):
                    line.append(x)
        for l in line:
            if re.search("from (.*) import", l) is not None:
                names_of_files.append(re.search("from (.*) import", l).group(1))

        return np.array(np.unique(names_of_files, return_counts=True))

