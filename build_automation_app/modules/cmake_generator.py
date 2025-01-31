import os
from json_checker import *

__all__ = ["generate_cmake_files_in_project"]


_EXPECTED_GENERATOR_DATA_JSON_STRUCTURE = {
    "cmake_minimum_required_version":
                                    {
                                        "major": int,
                                        "minor": int,
                                        "patch": int
                                    },

    "project_path": str,
    "project_name": str,
    "project_verison":
                    {
                        "major": int,
                        "minor": int,
                        "patch": int
                    },

    "c_standard": int,
    "c_standard_required": bool,
    "c_extensions": bool,

    "cxx_standard": int,
    "cxx_standard_required": bool,
    "cxx_extensions": bool,
    
    "app_directory": str,
    "code_directory": str
}

def _list_folder_contents(directory, indent=0):
    try:
        with os.scandir(directory) as entries:
            for entry in entries:
                if entry.is_file():
                    name, ext = os.path.splitext(entry.name)
                    print("  " * indent + f"File: {name} (Extension: {ext})")
                elif entry.is_dir():
                    print("  " * indent + f"Folder: {entry.name}")
                    _list_folder_contents(entry.path, indent + 1)
                else:
                    print("  " * indent + f"Unknown: {entry.name}")
    except PermissionError:
        print("  " * indent + "[Permission Denied]")

# folder_path = input("Enter folder path: ")
# if os.path.isdir(folder_path):
#     list_folder_contents(folder_path)
# else:
#     print("Invalid folder path.")

def generate_cmake_files_in_project(json_data_dict: dict) -> None:

    validate_json_data_structure(json_data_dict, _EXPECTED_GENERATOR_DATA_JSON_STRUCTURE)


