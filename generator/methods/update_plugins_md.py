from .shared import (
    read_source_file,
    read_docs_file,
    update_autogenerated_section,
    write_output_file,
)
from openad.helpers.output import output_text


# Update the docs/plugins.md file with the about_plugin description
def update_plugins_md(filename="plugins.md"):
    """
    Update the plugins.md file with the latest plugin description for the documentation.

    - Copy the content of the current version of the page in /docs
    - Update the page with the latest plugin description from the _source/about_plugin.txt file
    - Store result in _output/docs/plugins.md
    """

    output_text(
        f"<h1>Updating <yellow>{filename}</yellow> with about_plugin description</h1>",
        pad_top=2,
    )

    # Read base file content
    readme_plugin_md = read_docs_file(filename)
    if not readme_plugin_md:
        return

    # Read source file content
    about_plugin_txt = read_source_file("about_plugin.txt")
    if not about_plugin_txt:
        return

    # Insert description
    readme_plugin_md = update_autogenerated_section(
        readme_plugin_md, "plugins", about_plugin_txt
    )
    if not readme_plugin_md:
        return

    # Write to output file
    write_output_file("docs/" + filename, readme_plugin_md)
