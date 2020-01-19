from matplotlib import pyplot as plt
from objects import project
import networkx as nx


def draw_modules_graph(proj: project.Project):
    fig, ax = plt.subplots()
    graph = nx.DiGraph()
    for module in proj.modules:
        graph.add_node(module.name)
    for module in proj.modules:
        for file in module.files:
            pass




    nx.draw(graph, ax=ax, with_labels=True)
    return fig


def draw_files_graph(proj: project.Project):
    fig, ax = plt.subplots()
    graph = nx.DiGraph()
    for module in proj.modules:
        for file in module.files:
            if module.name == "global_scope":
                graph.add_node(file.name)
            else:
                graph.add_node("%s.%s" % (module.name, file.name))

    nx.draw(graph, ax=ax, with_labels=True)
    return fig

def draw_function_graph(proj: project.Project):
    fig, ax = plt.subplots()
    graph = nx.DiGraph()
    for module in proj.modules:
        for file in module.files:
            if module.name == "global_scope":
                graph.add_node(file.name)
            else:
                graph.add_node("%s.%s" % (module.name, file.name))

    nx.draw(graph, ax=ax, with_labels=True)
    return fig
