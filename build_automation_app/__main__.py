import os
import subprocess
import argparse
import platform
import json

from modules.cmake_builder import *
from modules.cmake_generator import *


def main():
    parser = argparse.ArgumentParser(description="Parse a JSON file")
    parser.add_argument("json_file", help="Path to the JSON file")
    args = parser.parse_args()

    try:
        with open(args.json_file, "r") as file:
            data = json.load(file)
            build_cmake_project(data["project_path"])
    except FileNotFoundError:
        print(f"Error: File '{args.json_file}' not found.")
    except json.JSONDecodeError:
        print(f"Error: File '{args.json_file}' is not a valid JSON file.")



if __name__ == "__main__":
    main()

