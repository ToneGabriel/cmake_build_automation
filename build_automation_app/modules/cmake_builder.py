import os
import subprocess
import sys

__all__ = ["build_cmake_project"]


def _run_command(command):
    """Helper function to run a command in the shell."""
    try:
        print(f"Running command: {command}")
        subprocess.check_call(command, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
        sys.exit(1)

def build_cmake_project(source_dir):
    """Configure and build a CMake project."""

    build_dir = source_dir + "/build"

    if not os.path.exists(build_dir):
        print(f"Creating build directory: {build_dir}")
        os.makedirs(build_dir)

    # Navigate to the build directory
    os.chdir(build_dir)

    # Run CMake to configure the project
    _run_command(f"cmake -G \"Ninja\" ..")

    # Build the project
    _run_command("cmake --build .")