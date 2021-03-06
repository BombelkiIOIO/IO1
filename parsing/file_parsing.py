import ast


class Analyzer(ast.NodeVisitor):
    def __init__(self):
        self.imports = []
        self.import_from = []
        self.func_def_names = []
        self.func_calls = []

    def visit_Import(self, node):
        for alias in node.names:
            self.imports.append(alias.name)
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        module = node.module
        for alias in node.names:
            name = alias.name
        self.import_from.append(module + "." + name)
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        self.func_def_names.append(node.name)

    def visit_Name(self, node):
        self.func_calls.append(node.id)

    def visit_Attribute(self, node):
        self.func_calls.append(node.attr)


# function returns: all imports
def get_imports(file_name):
    try:
        file = open(file_name)
        t = ast.parse(file.read())
        an = Analyzer()
        an.visit(t)
        all_imports = an.import_from + an.imports
        file.close()
        return all_imports
    except IOError:
        print("Error: file does not appear to exist.")


# function return: all definition in current file
def get_function_def(file_name):
    try:
        file = open(file_name)
        t = ast.parse(file.read())
        an = Analyzer()
        an.visit(t)
        file.close()
        return an.func_def_names
    except IOError:
        print("Error: file does not appear to exist.")


# function returns:
# if func_name = None, returns all function calls
# else it returns function calls in given function
def get_function_calls(file_name, func_name=None):
    try:
        file = open(file_name)
        t = ast.parse(file.read())
        an = Analyzer()
        if func_name is not None:
            for node in ast.walk(t):
                if isinstance(node, ast.FunctionDef) and node.name == func_name:
                    for x in ast.walk(node):
                        if isinstance(x, ast.Call):
                            an.visit(x.func)
        else:
            for node in ast.walk(t):
                if isinstance(node, ast.Call):
                    an.visit(node.func)
        file.close()
        return an.func_calls
    except IOError:
        print("Error: file does not appear to exist.")