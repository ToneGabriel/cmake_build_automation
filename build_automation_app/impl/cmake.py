import os
import sys
import subprocess

from . import json_checker


__all__ = ["build_project", "generate_cmakelists"]


_EXPECTED_BUILD_JSON_STRUCTURE = {
    "project_path": str,
    "cmake_generator": str,
    "c_compiler_path": str,
    "cxx_compiler_path": str
}   # END _EXPECTED_BUILD_JSON_STRUCTURE

_EXPECTED_GENERATOR_JSON_STRUCTURE = {
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
}   # END _EXPECTED_GENERATOR_JSON_STRUCTURE



def _run_command(command: str) -> None:
    """Helper function to run a command in the shell."""
    try:
        print(f"Running command: {command}")
        subprocess.check_call(command, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
        sys.exit(1)


def build_project(json_path: str) -> None:
    """Configure and build a CMake project."""

    json_data_dict = json_checker.get_json_data(json_path, _EXPECTED_BUILD_JSON_STRUCTURE)

    if not json_data_dict:
        return
    else:   # data OK
        project_path = json_data_dict["project_path"]
        cmake_generator = json_data_dict["cmake_generator"]
        c_compiler_path = json_data_dict["c_compiler_path"]
        cxx_compiler_path = json_data_dict["cxx_compiler_path"]

        if not os.path.exists(project_path):
            print("Project path does not exist.")
            return
        else:
            build_path = project_path + "/build"

            # Create build directory if not present
            if not os.path.exists(build_path):
                print(f"Creating build directory: {build_path}")
                os.makedirs(build_path)

            # Navigate to the build directory
            os.chdir(build_path)

            # Run CMake to configure the project
            if not c_compiler_path or not cxx_compiler_path:
                _run_command(f"cmake -G \"{cmake_generator}\" ..")
            else:
                _run_command(f"cmake -G \"{cmake_generator}\" -DCMAKE_C_COMPILER=\"{c_compiler_path}\" -DCMAKE_CXX_COMPILER=\"{cxx_compiler_path}\" ..")

            # Build the project
            _run_command("cmake --build .")



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

def generate_cmakelists(json_data_dict: dict) -> None:
    json_checker.validate_json_data_structure(json_data_dict, _EXPECTED_GENERATOR_JSON_STRUCTURE)
