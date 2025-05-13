"""
Generate/update documentation markdown files based on source files.

Usage:

    # Activate your openad virtual environment, unless you have openad installed globally
    source ../openad/.venv/bin/activate

    # Generate the docs
    python3 generator/generate_docs.py

    # Dispatch the newly generated docs to the correct locations
    python3 generator/generate_docs.py --dispatch

    # Generate the docs and dispatch them all at once
    python3 generator/generate_docs.py --dispatch-after

"""

import sys

# Scripts
from methods.oad_update_readme import oad_update_readme
from methods.oad_generate_concepts import oad_generate_concepts
from methods.update_plugins_md import update_plugins_md
from methods.update_base_concepts_md import update_base_concepts_md
from methods.generate_commands_md import generate_commands_md
from methods.generate_commands_csv import generate_commands_csv
from methods.generate_model_docs import generate_model_docs
from update_docs import distribute


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--dispatch" in args:
        distribute()
        sys.exit()

    # For openad-toolkit repo
    oad_update_readme()
    oad_generate_concepts()

    # Documentation files
    update_plugins_md()
    update_base_concepts_md()
    generate_commands_md()
    generate_model_docs()

    # Other files
    generate_commands_csv()

    if "--dispatch-after" in args:
        print("\n\n\n\n")
        distribute()
