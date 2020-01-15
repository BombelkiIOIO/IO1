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
        for alias in node.names:
            self.import_from.append(alias.name)
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        self.func_def_names.append(node.name)

    def visit_Name(self, node):
        self.func_calls.append(node.id)

    def visit_Attribute(self, node):
        self.func_calls.append(node.attr)


# function returns: all imports
def get_imports(file_name):
    t = ast.parse(open(file_name).read())
    an = Analyzer()
    an.visit(t)
    all_imports = an.import_from + an.imports
    return all_imports

# function return: all definition in current file
def get_function_def(file_name):
    t = ast.parse(open(file_name).read())
    an = Analyzer()
    an.visit(t)
    return an.func_def_names


# function returns:
# if func_name = None, returns all function calls
# else it returns function calls in given function
def get_function_calls(file_name, func_name=None):
    t = ast.parse(open(file_name).read())
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

    return an.func_calls
