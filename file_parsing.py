import pandas as pd
import re
import numpy as np
import os


def edit_array(arr, rows):
    matrix = [[0 for x in range(2)] for y in range(rows)]
    i = 0
    while i < rows:
        j = 0
        while j < 2:
            matrix[i][j] = arr[j][i]
            j += 1
        i += 1
    return matrix


def pars(file_name):
    line = []
    names_of_files = []
    final_result = []
    if os.path.isfile(file_name):
        with open(file_name) as file:
            for x in file:
                if x.startswith('import') | x.startswith('from'):
                    line.append(x)
        # print(line)
        for l in line:
            if re.search("from (.*) import", l) is not None:
                names_of_files.append(re.search("from (.*) import", l).group(1))
            elif re.search("import (.*)", l) is not None:
                names_of_files.append(re.search("import (.*)\n", l).group(1))

        final_result = np.array(np.unique(names_of_files, return_counts=True))

        return edit_array(final_result, len(final_result[0]))

