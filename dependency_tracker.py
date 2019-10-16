import data
import sys

def main(args):
    if args == []:
        args.append(".")
           
    nodes = data.prepare_data_to_visualisation(args[0])

    print(nodes)

if __name__ == "__main__":
    main(sys.argv[1:])