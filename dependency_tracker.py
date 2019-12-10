import data.data
import sys
from GUI.GUI import Application
import objects.file
import tkinter as tk
import objects.project
import os

def main(args):
    if args == []:
        args.append(".")

    prjct = objects.project.Project(os.path.splitext(os.path.basename(sys.argv[0]))[0], args[0])
"""    files_nodes = data.data.prepare_data_to_visualisation(args[0])
    function_nodes = data.data.prepare_functions_data_to_visualisation(args[0])
    root = tk.Tk()
    app = Application(files_nodes, function_nodes, master=root)
    root.title("Dependency Tracker")
    root.geometry("800x600+300+300")
    
    app.mainloop()
    root.destroy()
"""
if __name__ == "__main__":
    main(sys.argv[1:])
