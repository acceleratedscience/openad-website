import os
import re
from openad.helpers.output import output_text
from openad.app.main import RUNCMD as cmd_pointer
from openad.core.help import organize_commands
from .shared import DO_NOT_EDIT, read_input_file, write_output_file


def generate_commands_md(filename="commands.md"):
    """
    Generate the commands.md page for the documentation.

    - Start from the _input/commands.md template
    - Loop through all OpenAD commands & generate markdown
    - Store result in _output/docs/commands.md
    """

    output_text(f"<h1>Generating <yellow>{filename}</yellow></h1>", pad_top=2)

    toc = []  # Table of content
    md_output = []  # Markdown

    # Parse main commands
    # - - -
    # For now, plugin commands are not included, but once we bring
    # them back, we'll want to organize the commands in sections.
    # - - -
    # md_output.append("\n\n## Main Commands\n")
    # toc.append(_toc_link("Main Commands"))
    cmds = cmd_pointer.current_help.help_current
    cmds_organized = organize_commands(cmds)
    parsed = _parse_section(cmds_organized)
    md_output += parsed["output"]
    toc += parsed["toc"]

    # Compile table of contents
    toc = "## Table of Contents\n" + "\n".join(toc) + "\n"

    # Compile commands
    md_output = "\n".join(md_output)

    #
    #

    # Read commands.md input content
    commands_md = read_input_file(filename)

    # Insert sections
    # fmt: off
    commands_md = re.sub(r"{{DO_NOT_EDIT}}", DO_NOT_EDIT, commands_md, flags=re.DOTALL) # Insert DO NOT EDIT comment
    commands_md = re.sub(r"{{TOC}}", toc, commands_md, flags=re.DOTALL) # Insert table of contents
    commands_md = re.sub(r"{{COMMANDS}}", md_output, commands_md, flags=re.DOTALL) # Insert commands
    # fmt: on

    # Write to output file
    write_output_file("docs/" + filename, commands_md)


# Compile all commands of a single section.
def _parse_section(cmds_organized):
    output = []
    toc = []
    for category in cmds_organized:
        output.append(f"### {category}\n")
        toc.append(_toc_link(category, 1))
        for cmd_str, cmd_description in cmds_organized[category]:
            # Break up inline descriptions (For `? ...` and `... ?`)
            if " --> " in cmd_str:
                split = cmd_str.split(" --> ")
                cmd_str = split[0]
                cmd_description = split[1]

            # Replace < and > with &lt; and &gt; so they don't get parsed as HTML tags
            cmd_str = cmd_str.replace("<", "&lt;").replace(">", "&gt;")

            # Compile markdown
            cmd_output = "\n".join(
                [
                    "<details markdown code>",
                    "<summary markdown>",
                    cmd_str.strip(),
                    "</summary>",
                    _parse_description(cmd_description),
                    "</details>\n",
                ]
            )
            output.append(cmd_output)

    return {
        "output": output,
        "toc": toc,
    }


# Prepare the command description for proper rendering.
def _parse_description(description):
    split = description.split("<h1>Examples</h1>")
    if len(split) == 1:
        split = description.split("Examples:")
    if len(split) == 1:
        split = description.split("Example:")
    description_only = split[0]
    examples = split[1] if len(split) > 1 else None

    # Format description:
    lines = description_only.splitlines()
    lines_formatted = []
    for line in lines:
        # Replace <h1> with fake #### h4 so it doesn't show up in the TOC
        line = re.sub(r"^<h1>(.+?)</h1>$", r"**\1**{.fake-h4}", line)
        # Replace style tags
        line = _tags_to_markdown(line)
        lines_formatted.append(line)
    description_only = "\n".join(lines_formatted)

    # Format examples:
    if examples:
        lines = examples.splitlines()
        lines_formatted = []
        for line in lines:
            line = line.strip()
            # Remove leading dash
            line = re.sub(r"^- ", "", line)
            # Wrap commands in code block
            line = re.sub(r"^<cmd>(.+?)</cmd>$", r"```shell\n\1\n```", line)
            # Replace style tags
            line = _tags_to_markdown(line)
            # Replace < and > with &lt; and &gt; so they don't get parsed as HTML tags
            if "```shell" not in line:
                line = line.replace("<", "&lt;").replace(">", "&gt;")
            lines_formatted.append(line)
        examples = "\n".join(lines_formatted)

        # Add title
        # Fake #### h4 so it doesn't show up in the TOC
        description = f"{description_only}\n**Examples**{{ .fake-h4 }}\n{examples}"

    # Format total
    description = _tags_to_markdown(description)

    # Convert to markdown
    # description = tags_to_markdown(description)
    # description = description.replace("Examples:", "#### Examples")

    # # Style notes as blockquotes, and ensure they're always
    # # followed by an empty line, to avoid the next lines to
    # # be treated as part of the blockquote.
    # description = re.sub(
    #     r"(\*\*Note:\*\*.+?)(\n{1,})",
    #     lambda match: (
    #         f"  > {match.group(1)}\n\n" if len(match.group(2)) == 1 else f"  > {match.group(1)}{match.group(2)}"
    #     ),
    #     description,
    #     flags=re.MULTILINE,
    # )

    # description = description.splitlines()
    # description = "\n".join([line.strip() for line in description])
    return description.strip()


# Convert a title to a markdown
# link for the table of contents.
# Foo Bar --> #foo-bar
def _toc_link(title, level=0):
    dash = "  " * level + "- "
    return f"{dash}[{title}](#{title.replace(' ', '-').lower()})"


def _tags_to_markdown(text):
    """
    Convert XML tags to markdown.

    This is forked from style parser, which was designed for Jupyter output
    and has some nuances that interfer with our usecase for MkDocs.
    We'll need to revisit the style parser at some point to be able to handle
    proper HTML output for a GUI terminal, after which this function can be replaced.
    """
    text = re.sub(r"<h1>(.*?)<\/h1>", r"## \1", text)
    text = re.sub(r"<h2>(.*?)<\/h2>", r"### \1", text)
    text = re.sub(r"<link>(.*?)<\/link>", r"[\1](\1)", text)  # Diff
    text = re.sub(r"<bold>(.*?)<\/bold>", r"**\1**", text)
    text = re.sub(r"<cmd>(.*?)<\/cmd>", r"`\1`", text)
    text = re.sub(r"<red>(.*?)<\/red>", r'<span style="color: #d00">\1</span>', text)
    text = re.sub(
        r"<green>(.*?)<\/green>", r'<span style="color: #090">\1</span>', text
    )
    text = re.sub(
        r"<yellow>(.*?)<\/yellow>", r'<span style="color: #dc0">\1</span>', text
    )
    text = re.sub(r"<blue>(.*?)<\/blue>", r'<span style="color: #00d">\1</span>', text)
    text = re.sub(
        r"<magenta>(.*?)<\/magenta>", r'<span style="color: #d07">\1</span>', text
    )
    text = re.sub(r"<cyan>(.*?)<\/cyan>", r'<span style="color: #0cc">\1</span>', text)
    text = re.sub(
        r"<on_red>(.*?)<\/on_red>",
        r'<span style="background: #d00; color: #fff">\1</span>',
        text,
    )
    text = re.sub(
        r"<on_green>(.*?)<\/on_green>",
        r'<span style="background: #090; color: #fff">\1</span>',
        text,
    )
    text = re.sub(
        r"<on_yellow>(.*?)<\/on_yellow>",
        r'<span style="background: #dc0; color: #fff">\1</span>',
        text,
    )
    text = re.sub(
        r"<on_blue>(.*?)<\/on_blue>",
        r'<span style="background: #00d; color: #fff">\1</span>',
        text,
    )
    text = re.sub(
        r"<on_magenta>(.*?)<\/on_magenta>",
        r'<span style="background: #d07; color: #fff">\1</span>',
        text,
    )
    text = re.sub(
        r"<on_cyan>(.*?)<\/on_cyan>",
        r'<span style="background: #0cc; color: #fff">\1</span>',
        text,
    )
    return text
