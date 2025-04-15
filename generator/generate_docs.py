"""
Generate/update documentation markdown files based on source files.

Usage:
    python3 generator/generate_docs.py

"""

from openad.helpers.output import output_text, output_warning
from openad.helpers.general import confirm_prompt

# Scripts
from methods.update_gh_readme import update_gh_readme
from methods.update_plugins_md import update_plugins_md
from methods.update_base_concepts_md import update_base_concepts_md
from methods.generate_commands_md import generate_commands_md
from methods.generate_commands_csv import generate_commands_csv
from methods.generate_model_docs import generate_model_docs
from methods.copy_docs import update_docs, update_openad


if __name__ == "__main__":
    # update_gh_readme()
    # update_plugins_md()
    # update_base_concepts_md()
    # generate_commands_md()
    # generate_commands_csv()
    generate_model_docs()
    print("\n")

    # fmt: off

    # Update website docs
    output_warning("<yellow>Do you want to update the docs with the generated markdown files?</yellow>")
    ok = confirm_prompt("Continue?")
    if ok:
        update_docs()
    else:
        output_warning([ "No files were moved", "You can still find them in the /output/docs directory"], pad_btm=1)
    

    # Update openad README
    output_warning((
        "Do you want to copy the generated <reset>README.md</reset> to the <reset>openad-toolkit</reset> repo?\n"
        "<on_yellow>WARNING: THIS WILL MODIFY FILES OUTSIDE THIS REPOSITORY</on_yellow>"
    ))
    ok = confirm_prompt("Continue?")
    if ok:
        update_openad()
    else:
        output_warning([ "No files were moved", "You can still find them in the /output/openad-toolkit directory"], pad_btm=1)
