from openad.helpers.output import output_warning, output_text, output_error
from openad.helpers.general import confirm_prompt
from methods.distribute_output import update_docs, update_openad

# fmt: off
def distribute():
    # Update website docs
    ok = confirm_prompt("Update the docs with the generated markdown files?")
    if ok:
        update_docs()
    else:
        output_error([ "No files were moved", "You can still find them in the /_output/docs directory"], pad_btm=1)

    # Update openad-toolkit repo
    ok = confirm_prompt((
        "<on_yellow> WARNING: NEXT STEP WILL MODIFY FILES OUTSIDE THIS REPOSITORY </on_yellow>\n\n"
        "Update the openad-toolkit repo with the udpated files?\n"
        "<reset>"
        "- README.md\n"
        "- openad/helpers/concept.py"
        "</reset>"
    ))
    if ok:
        update_openad()
    else:
        output_error([ "No files were moved", "You can still find them in the /output/openad-toolkit directory"], pad_btm=1)



if __name__ == "__main__":
    distribute()
