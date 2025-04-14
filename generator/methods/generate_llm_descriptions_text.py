# -- NO LONGER IN USE --
# Todo: strategy on how to integrate LLM training for plugins

import os
import re
from shared import FLAG_ERROR, FLAG_SUCCESS
from openad.helpers.files import open_file, write_file
from openad.helpers.output import output_error, output_text
from openad.core.help import organize_commands
from openad.app.global_var_lib import _all_toolkits
from openad.toolkit.toolkit_main import load_toolkit
from openad.helpers.output_msgs import msg
from openad.plugins.style_parser import tags_to_markdown

# Find the path for the openad-website docs folder
dir = os.path.dirname(os.path.abspath(__file__))
website_repo_docs = os.path.normpath(
    os.path.join(dir, "../../openad-website/main/docs")
)


# Update commands in the llm_description.txt file per toolkit.
# Used as training data by the LLM for the "tell me" command.
# - - -
# Note: llm_description.txt needs to be set up with the toolkit
# LLM briefing set up and the following line will define where
# the commands are to be inserted - any text after this line
# will be overwritten:
# "The following commands are available for this toolkit:"
def generate_llm_description_txt(filename="llm_description.txt"):
    output_text(
        "<h1>Updating commands in <yellow>llm_description.txt</yellow> for all toolkits</h1>",
        pad_top=2,
    )

    # Loop through all toolkits
    for toolkit_name in _all_toolkits:
        flag_toolkit = f"<on_white><black> {toolkit_name} </black></on_white>"
        # Load toolkit
        success, toolkit = load_toolkit(toolkit_name, from_repo=True)
        if not success:
            err_msg = toolkit
            output_text(flag_toolkit + FLAG_ERROR)
            output_error(msg("err_load_toolkit", toolkit_name), pad=0)
            continue

        toolkit_cmds = toolkit.methods_help
        toolkit_cmds_organized = organize_commands(toolkit_cmds)
        output = _compile_commands(toolkit_cmds_organized)

        # Load llm_description.txt
        file_path = f"openad/user_toolkits/{toolkit_name}/{filename}"
        description_txt, err_msg = open_file(file_path, return_err=True)
        if not description_txt:
            output_text(flag_toolkit + FLAG_ERROR)
            # output_error(msg("err_load_toolkit_description", toolkit_name), pad=0) # Maybe overkill
            output_error(err_msg, pad_btm=1)
            continue

        # Insert commands into llm_description.txt
        splitter = "The following commands are available for this toolkit:"
        if splitter not in description_txt:
            output_text(flag_toolkit + FLAG_ERROR)
            output_error(
                msg("err_invalid_description_txt", toolkit_name, splitter), pad_btm=1
            )
            continue
        description_txt = description_txt.split(splitter)[0] + splitter + "\n\n"
        description_txt += "\n".join(output)
        description_txt = description_txt.strip()

        # print(("----" * 50) + "\n" + description_txt + "\n" + ("----" * 50))

        # Write to file
        success, err_msg = write_file(file_path, description_txt, return_err=True)
        if success:
            output_text(flag_toolkit + FLAG_SUCCESS)
            output_text(
                f"<soft>Updated in</soft> <reset>/docs/openad/user_toolkits/{toolkit_name}/{filename}</reset>",
                pad_btm=1,
            )
        else:
            output_text(flag_toolkit + FLAG_ERROR)
            output_error(err_msg, pad_btm=1)

    output_text("", pad_btm=2)


# Compile all commands for a single toolkit's llm_description.txt.
def _compile_commands(cmds_organized):
    output = []
    for category in cmds_organized:
        output.append(category + ":")
        for cmd_str, cmd_description in cmds_organized[category]:
            # Add command
            output.append(f"\t`{cmd_str.strip()}`")

            # Add command description
            cmd_description = tags_to_markdown(cmd_description).strip()
            cmd_description = cmd_description.replace("<br>", "")
            cmd_description = cmd_description.splitlines()
            cmd_description = "\n\t\t".join([line.strip() for line in cmd_description])
        output.append("")

    return output
