import os
import subprocess
import sys

from json_checker import *

__all__ = ["build_cmake_project"]


_EXPECTED_BUILD_DATA_JSON_STRUCTURE = {
    "project_path": str,
    "cmake_generator": str,
    "c_compiler_path": str,
    "cxx_compiler_path": str
}


def _run_command(command: str) -> None:
    """Helper function to run a command in the shell."""
    try:
        print(f"Running command: {command}")
        subprocess.check_call(command, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
        sys.exit(1)


def build_cmake_project(json_data_dict: dict) -> None:
    """Configure and build a CMake project."""

    if not validate_json_data_structure(json_data_dict, _EXPECTED_BUILD_DATA_JSON_STRUCTURE):
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