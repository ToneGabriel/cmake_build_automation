import os
import subprocess
import argparse
import platform
import json

from modules.cmake_builder import *
from modules.cmake_generator import *


def main():
    build_cmake_project("C:/Personal/C++/CompressionTool")

if __name__ == "__main__":
    main()

