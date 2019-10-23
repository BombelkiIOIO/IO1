import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import tkinter as tk

class Application(tk.Frame):
    def say_hi(self):
        print("hi there, everyone!")

    def createWidgets(self):

        self.phisycal_btn = tk.Button(self)
        self.phisycal_btn["text"] = "Phisycal",
        self.phisycal_btn["command"] = self.draw_phisycal_graph
        self.phisycal_btn.pack({"side": "left"})
        self.logical_btn = tk.Button(self)
        self.logical_btn["text"] = "Logical",
        self.logical_btn["command"] = self.draw_logial_graph
        self.logical_btn.pack({"side": "right"})

    def draw_phisycal_graph(self):
        if self.canvas:
            self.canvas.get_tk_widget().destroy()

        f = plt.figure(figsize=(5, 4))
        plt.axis('off')
        G = nx.DiGraph()

        i = 1
        for n in self.phisycal_nodes:
            node_name = n.name.replace(".py", "")
            G.add_node(node_name, pos=(i, (-1)**i))
            i = i+1

        for e in self.phisycal_nodes:
            node_name = e.name.replace(".py", "")
            for a in e.internal_dependencies:
                G.add_edge(node_name, a[0], weight=a[1])

        pos = nx.spring_layout(G)
        labels = nx.get_edge_attributes(G, 'weight')

        nx.draw(G, pos, with_labels=True, font_weight='bold')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

        self.canvas = FigureCanvasTkAgg(f, master=self.root)
        self.canvas.get_tk_widget().pack(side='bottom', fill='both', expand=1)
    
    # new graph should be processed here... now it is just the old one  so change it
    def draw_logial_graph(self):
        if self.canvas:
            self.canvas.get_tk_widget().destroy()

        f = plt.figure(figsize=(5, 4))
        plt.axis('off')
        G = nx.DiGraph()
        i = 1
        for n in self.logical_nodes:
            node_name = n.name
            G.add_node(node_name, pos=(i, (-1)**i))
            i = i+1

        for e in self.logical_nodes:
            node_name = e.name
            for a in e.internal_dependencies:
                G.add_edge(node_name, a[0], weight=a[1])

        pos = nx.spring_layout(G)
        labels = nx.get_edge_attributes(G, 'weight')

        nx.draw(G, pos, with_labels=True, font_weight='bold')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

        self.canvas = FigureCanvasTkAgg(f, master=self.root)
        self.canvas.get_tk_widget().pack(side='bottom', fill='both', expand=1)
    
    
    def ask_quit(self):
        self.root.quit()

    def __init__(self, phisycal_nodes, logical_nodes, master=None):
        tk.Frame.__init__(self, master)
        self.canvas = False
        self.phisycal_nodes = phisycal_nodes
        self.logical_nodes = logical_nodes
        self.root = master
        self.root.protocol("WM_DELETE_WINDOW", self.ask_quit)
        self.pack()
        self.createWidgets()
