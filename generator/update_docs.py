from openad.helpers.output import output_warning
from openad.helpers.general import confirm_prompt
from generator.methods.distribute_output import update_docs, update_openad

# fmt: off
if __name__ == "__main__":
    # Update website docs
    output_warning("<yellow>Do you want to update the docs with the generated markdown files?</yellow>")
    ok = confirm_prompt("Continue?")
    if ok:
        update_docs()
    else:
        output_warning([ "No files were moved", "You can still find them in the /output/docs directory"], pad_btm=1)

    # Update openad-toolkit repo
    output_warning((
        "Do you want to copy the generated <reset>README.md</reset> to the <reset>openad-toolkit</reset> repo?\n"
        "<on_yellow>WARNING: THIS WILL MODIFY FILES OUTSIDE THIS REPOSITORY</on_yellow>"
    ))
    ok = confirm_prompt("Continue?")
    if ok:
        update_openad()
    else:
        output_warning([ "No files were moved", "You can still find them in the /output/openad-toolkit directory"], pad_btm=1)
