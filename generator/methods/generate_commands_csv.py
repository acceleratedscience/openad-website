import pyperclip
from openad.helpers.output import output_text, output_success
from openad.app.main import RUNCMD as cmd_pointer
from openad.core.help import organize_commands
from openad.helpers.output_msgs import msg

# from openad.app.global_var_lib import _all_toolkits
# from openad.toolkit.toolkit_main import load_toolkit

from .shared import write_output_file


def generate_commands_csv(filename="commands.csv", delimiter=";"):
    """
    Create a CSV with all OpenAD commands.

    This is not used for anything in particular, other than
    to have a list of all commands in a file which can be annotated.

    - Loop through all toolkit commands and compile CSV
    - Store CSV in _output/other/commands.csv
    """

    output_text(
        "<h1>Generating <yellow>commands.csv</yellow> from help</h1>", pad_top=2
    )
    output = [["Command", "Category"]]

    # Parse main commands
    cmds_main = cmd_pointer.current_help.help_current
    cmds_organized = organize_commands(cmds_main)

    # # Parse tookit commands
    # for toolkit_name in _all_toolkits:
    #     success, toolkit = load_toolkit(toolkit_name, from_repo=True)
    #     if success:
    #         toolkit_cmds = toolkit.methods_help
    #         toolkit_cmds_organized = organize_commands(toolkit_cmds)
    #         cmds_organized.update(toolkit_cmds_organized)

    # Add a row per command
    for category, cmds in cmds_organized.items():
        for cmd in cmds:
            output.append([cmd[0], category])

    # Convert to CSV string
    output_str = "\n".join([f"{delimiter}".join(row) for row in output])

    # Convert to clipboard CSV string
    output_clipboard = "\n".join([f"\t".join(row) for row in output])
    pyperclip.copy(output_clipboard)

    # Write to output file
    write_output_file("other/" + filename, output_str)
    output_success(msg("csv_to_clipboard"), pad=0)
