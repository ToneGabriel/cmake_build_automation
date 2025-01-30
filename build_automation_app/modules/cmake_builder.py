import os
import subprocess
import sys
import json

__all__ = ["build_cmake_project"]


def _run_command(command: str) -> None:
    """Helper function to run a command in the shell."""
    try:
        print(f"Running command: {command}")
        subprocess.check_call(command, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
        sys.exit(1)

def build_cmake_project(json_build_data_path: str = None) -> None:
    """Configure and build a CMake project."""

    json_data = None

    try:
        with open(json_build_data_path, "r") as file:
            json_data = json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{json_build_data_path}' not found.")
    except json.JSONDecodeError:
        print(f"Error: File '{json_build_data_path}' is not a valid JSON file.")

    if not json_data:
        return
    else:        
        project_path = json_data["project_path"]
        cmake_generator = json_data["cmake_generator"]
        c_compiler_path = json_data["c_compiler_path"]
        cxx_compiler_path = json_data["cxx_compiler_path"]

        if not os.path.exists(project_path):
            print("Project path does not exist.")
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