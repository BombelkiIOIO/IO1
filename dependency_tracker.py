import data
import sys
import GUI
import node

def main(args):
    if args == []:
        args.append(".")
           
    nodes = data.prepare_data_to_visualisation(args[0])
    GUI.print_graph(nodes)


if __name__ == "__main__":
    main(sys.argv[1:])
