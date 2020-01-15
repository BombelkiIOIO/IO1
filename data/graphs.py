from matplotlib import pyplot as plt
from objects import project
import networkx as nx
from matplotlib import style
style.use('dark_background')

def draw_modules_graph(proj: project.Project):
    fig, ax = plt.subplots()
    graph = nx.DiGraph()
    for module in proj.modules:
        graph.add_node(module.name)
    nx.draw(graph, ax=ax, with_labels=True)
    return fig


def draw_files_graph(proj: project.Project):
    fig, ax = plt.subplots()
    graph = nx.DiGraph()
    for module in proj.modules:
       print("Module: " + module.name)
       print(module.files)
       for file in module.files:
           print("file: " + file.name)
           graph.add_node(file.name)
    nx.draw(graph, ax=ax, with_labels=True)
    return fig
