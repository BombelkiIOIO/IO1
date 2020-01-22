from matplotlib import pyplot as plt
from objects import project
import networkx as nx


def draw_modules_graph(proj: project.Project):
    fig, ax = plt.subplots()
    graph = nx.DiGraph()
    for module in proj.modules:
        graph.add_node(module.name)
    for module in proj.modules:
        for dependency in module.get_internal_dependencies():
            graph.add_edge(module.name, dependency)

    nx.draw(graph, ax=ax, with_labels=True)
    return fig


def draw_files_graph(proj: project.Project):
    fig, ax = plt.subplots()
    graph = nx.DiGraph()
    for file in proj.get_files():
        graph.add_node(file.name)
    for file in proj.get_files():
        for dependency in file.get_internal_dependencies():
            graph.add_edge(file.name, f'{dependency.split(".")[-1]}.py')
    nx.draw(graph, ax=ax, with_labels=True)
    return fig

def draw_function_graph(proj: project.Project):
    fig, ax = plt.subplots()
    graph = nx.DiGraph()
    for fun in proj.get_functions():
        if fun.name != "__init__":
            graph.add_node(fun.name)
    for fun in proj.get_functions():
        if fun.name != "__init__":
            for dependency in fun.get_internal_dependencies():
                graph.add_edge(fun.name, dependency)

    nx.draw(graph, ax=ax, with_labels=True)
    return fig
