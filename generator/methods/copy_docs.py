"""
Script to copy generated markdown files to the website repository.

The two repositories should be placed in the same parent folder for this to work:
/my-repos
    /openad-toolkit # <-- this repository
    /openad-website # <-- website repository

"""

import os
import shutil
from openad.helpers.output import (
    output_error,
    output_warning,
    output_text,
    output_success,
)
from .shared import FLAG_ERROR, openad_toolkit_dir, output_dir, docs_dir


FLAG_COPIED = f"<on_green> COPIED </on_green>"
DIR_STRUCTURE = [
    "/my-repos",
    "  /openad-website",
    "    /generator",
    "      /output",
    "        /openad-toolkit  <-- Source",
    "  /openad-toolkit        <-- Destination",
]


#
#


def update_docs():
    src_dir = os.path.join(output_dir, "docs")
    dest_dir = docs_dir
    _move_files(src_dir, dest_dir)


def update_openad():
    src_dir = os.path.join(output_dir, "openad-toolkit")
    dest_dir = openad_toolkit_dir
    # os.path.normpath("../openad-toolkit")
    success = _move_files(src_dir, dest_dir)

    if not success:
        output_text(
            [
                "<reset>To have the output files copied automatically, make sure to place the openad-docs repo adjacent to this repo:</reset>",
                "\n".join(DIR_STRUCTURE),
            ],
            pad_btm=1,
        )


#
#

# fmt: off

def _move_files(src_dir, dest_dir):
    # Title
    output_text("\n<h1>Overwriting website files with new markdown files</h1>")

    # Source folder not found
    if not os.path.exists(src_dir):
        output_error([FLAG_ERROR + f" The source folder was not found, no files have been copied.", src_dir], pad_btm=1)
        return False

    # Destination folder not found
    if not os.path.exists(dest_dir):
        output_error([FLAG_ERROR + " The destination director repository was not found, no files have been copied", dest_dir], pad_btm=1)
        return False

    # Assemble list of files to copy
    for filename in os.listdir(src_dir):
        # Construct full file path
        source_file = os.path.join(src_dir, filename)
        dest_file = os.path.join(dest_dir, filename)

        if not os.path.exists(source_file):
            output_text(FLAG_ERROR + f" <red>{filename}</red> could not be found at <yellow>{source_file}</yellow>.", pad_btm=1)
            return False

        # Copy the file
        shutil.copy2(source_file, dest_file)
        output_text(FLAG_COPIED + f" <yellow>{filename}</yellow> to <soft>{dest_dir}</soft>", pad_btm=1)

        # Remove source file
        os.remove(source_file)

    return True
