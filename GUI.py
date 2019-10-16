import networkx as nx
import matplotlib.pyplot as plt
import data as d


def print_graph(nodes):
    G = nx.Graph()

    i = 1
    for n in nodes:
        G.add_node(n.name + "\n" + str(n.size) + "bytes", pos=(i, i*i))
        i = i+1

    for e in nodes:
        for a in nodes.internal_dependencies:
            G.add_edge(e.name, a, weight=2)

    #G.add_node(1, pos=(1, 1))
    #G.add_node(2, pos=(1, 2))
    #G.add_node("spam", pos=(2, 1))        # adds node "spam"
    #G.add_edge(1, 2, weight=5)
    #G.add_edge(1, "spam", weight=3)
    #pos = nx.kamada_kawai_layout(G)
    pos = nx.get_node_attributes(G, 'pos')
    labels = nx.get_edge_attributes(G, 'weight')

    nx.draw(G, pos, with_labels=True, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    #plt.subplot(122)

    #nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')

    plt.show()

print_graph(d.prepare_data_to_visualisation())