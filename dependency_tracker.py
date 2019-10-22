import data
import sys
from GUI import Application
import node
import tkinter as tk

def main(args):
    if args == []:
        args.append(".")
           
    nodes = data.prepare_data_to_visualisation(args[0])
    root = tk.Tk()
    app = Application(nodes, master=root)
    root.title("Dependency Tracker")
    root.geometry("800x600+300+300")
    
    app.mainloop()
    root.destroy()

if __name__ == "__main__":
    main(sys.argv[1:])
