"""
Generate/update documentation markdown files based on source files.

Usage:
    python3 generator/generate_docs.py

"""

from openad.helpers.output import output_text, output_warning
from openad.helpers.general import confirm_prompt

# Scripts
from methods.oad_update_readme import oad_update_readme
from methods.oad_generate_concepts import oad_generate_concepts
from methods.update_plugins_md import update_plugins_md
from methods.update_base_concepts_md import update_base_concepts_md
from methods.generate_commands_md import generate_commands_md
from methods.generate_commands_csv import generate_commands_csv
from methods.generate_model_docs import generate_model_docs
from generator.methods.distribute_output import update_docs, update_openad


if __name__ == "__main__":
    oad_generate_concepts()

    # # STEP 1
    # # ------------------------
    # # Generate/update files, store to _output

    # # For openad-toolkit repo
    # oad_update_readme()
    # oad_generate_concepts()

    # # Documentation files
    # update_plugins_md()
    # update_base_concepts_md()
    # generate_commands_md()
    # generate_model_docs()

    # # Other files
    # generate_commands_csv()

    # Step 2
    # ------------------------
    # Copy files to final destination
