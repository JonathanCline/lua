# Helper script that moves specific lua headers from the src/ directory into the include/ directory

import argparse
from pathlib import Path
import shutil

MOVE_FILE_NAMES = [
    "lauxlib.h",
    "lua.h",
    "lua.hpp",
    "luaconf.h",
    "lualib.h"
]

# Create the argument parser, we don't actually need any arguments so just provide info
parser = argparse.ArgumentParser("move_headers", description="Moves specific lua headers from the src/ directory into the include/ directory")
args = parser.parse_args()

# Create the source and target directory paths
source_directory_path = Path.cwd().joinpath("src")
target_directory_path = Path.cwd().joinpath("include", "lua")

# Move found source files into target directory 
for name in MOVE_FILE_NAMES:
    source_file = source_directory_path.joinpath(name)
    if source_file.exists():
        target_file = target_directory_path.joinpath(name)
        shutil.move(source_file, target_file)
