from argparse import ArgumentParser

from modules.cmake_generator import *
from modules.cmake_builder import *



def main():
    parser = ArgumentParser()
    parser.add_argument("--action", type=str, required=True, help="Specify the action: 'g' to generate or 'b' to build.")
    parser.add_argument("--json", type=str, required=True, help="Path to the JSON file")
    args = parser.parse_args()

    if args.action == 'g':
        pass
    elif args.action == 'b':
        build_cmake_project(args.json)
    else:
        print("Invalid action! Please use 'g' to generate or 'b' to build.")




if __name__ == "__main__":
    main()

