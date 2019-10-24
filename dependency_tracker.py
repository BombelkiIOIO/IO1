import data
import sys
from GUI import Application
import file
import tkinter as tk
import project

def main(args):
    if args == []:
        args.append(".")

#    prjct = project.Project(args[0])    #prepared for future organisation structure
    files_nodes = data.prepare_data_to_visualisation(args[0])
    function_nodes = data.prepare_functions_data_to_visualisation(args[0])
    root = tk.Tk()
    app = Application(files_nodes, function_nodes, master=root)
    root.title("Dependency Tracker")
    root.geometry("800x600+300+300")
    
    app.mainloop()
    root.destroy()

if __name__ == "__main__":
    main(sys.argv[1:])
