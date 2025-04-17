"""
Copy generated files to their final destinartion.

For files to be copied over to the openad-toolkit repo,
the two repositories should be placed in the same parent folder:
/my-repos
    /openad-toolkit
    /openad-website

"""

import os
import shutil
from openad.helpers.output import (
    output_error,
    output_text,
)
from .shared import FLAG_ERROR, openad_toolkit_dir, output_dir, docs_dir


FLAG_COPIED = f"<on_green> COPIED </on_green>"
DIR_STRUCTURE = [
    "/my-repos",
    "  /openad-website",
    "    /generator",
    "      /_output",
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
        # Slice off any path information from the filename
        # and add it to the destination directory's path.
        # We can't use / in a filename, so we use ~ instead.
        # Example:
        #   dest_dir = "/main/docs"
        #   og_filename = "model-service~available-models.md"
        #   dest_path = "model-service"
        #   filename = "available-models.md"
        #   --> File is written to: /main/docs/model-service/available-models.md
        og_filename = filename
        dest_path = ''
        if "~" in filename:
            filename = filename.replace("~", "/")
            dest_path = os.path.dirname(filename)
            filename = os.path.basename(filename)
        
        # Construct full file path
        source_file = os.path.join(src_dir, og_filename)
        dest_file = os.path.join(dest_dir, dest_path, filename)

        if not os.path.exists(source_file):
            output_text(FLAG_ERROR + f" <red>{og_filename}</red> could not be found at <yellow>{source_file}</yellow>", pad_btm=1)
            return False

        # Copy the file
        shutil.copy2(source_file, dest_file)
        output_text(FLAG_COPIED + f" <yellow>{filename}</yellow> to <soft>{dest_dir}</soft>", pad_btm=1)

        # Remove source file
        os.remove(source_file)

    return True
