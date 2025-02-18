import argparse

import impl


def main():
    # Parse arguments from terminal call
    parser = argparse.ArgumentParser()
    parser.add_argument("--action", type=str, required=True, help="Specify the action: 'g' to generate or 'b' to build.")
    parser.add_argument("--json", type=str, required=True, help="Path to the JSON file")
    args = parser.parse_args()
    
    # Call function based on choice and pass the corresponding json data
    if args.action == 'g':
        impl.generate_cmakelists(args.json)
    elif args.action == 'b':
        impl.build_project(args.json)
    else:
        print("Invalid action! Please use 'g' to generate or 'b' to build.")


if __name__ == "__main__":
    main()

