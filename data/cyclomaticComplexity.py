import lizard

def file_complexity(filename):
    i = lizard.analyze_file(filename)
    print(i.CCN)
    return i.CCN

def function_complexity(filename):
    t=9
    i=lizard.analyze_file(filename)
    for x in range(0,9):
        print(i.__dict__)
        print(i.function_list[x].name, i.function_list[x].cyclomatic_complexity)
