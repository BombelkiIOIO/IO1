import networkx as nx
import matplotlib.pyplot as plt


def print_graph(nodes):
    G = nx.DiGraph()

    i = 1
    for n in nodes:
        node_name = n.name.replace(".py", "")
        node_name = node_name.replace(".\\", "")
        G.add_node(node_name, pos=(i, (-1)**i))
        i = i+1

    for e in nodes:
        node_name = e.name.replace(".py", "")
        node_name = node_name.replace(".\\", "")
        for a in e.internal_dependencies:
            G.add_edge(node_name, a[0], weight=a[1])

    pos = nx.spring_layout(G)
    #pos = nx.get_node_attributes(G, 'pos')
    labels = nx.get_edge_attributes(G, 'weight')

    nx.draw(G, pos, with_labels=True, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.show()