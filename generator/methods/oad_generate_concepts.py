from openad.helpers.output import output_text
from .shared import read_template_file, read_source_file, write_output_file


def oad_generate_concepts(filename="openad~helpers~concepts.py"):
    """
    Generate the concept.py file for the openad-toolkit repo.

    - Start from the _templates/openad~helpers~concepts.py template
    - Fill in all descriptions from the _source directory
    - Store result in _output/openad-toolkit/openad~helpers~concepts.py

    Note: The copy_docs script will interpret the ~ in the filename to know
    the path in the openad-toolkit repo where to copy the file to.
    """

    output_text(f"<h1>Generating <yellow>{filename}</yellow></h1>", pad_top=2)

    # Read concepts.py template content
    concepts_py = read_template_file(filename)

    # Read source file content
    description_txt = read_source_file("description.txt")
    if not description_txt:
        return
    about_mws_txt = read_source_file("about_mws.txt")
    if not about_mws_txt:
        return
    about_workspace_txt = read_source_file("about_workspace.txt")
    if not about_workspace_txt:
        return
    about_plugin_txt = read_source_file("about_plugin.txt")
    if not about_plugin_txt:
        return
    about_run_txt = read_source_file("about_run.txt")
    if not about_run_txt:
        return

    # fmt: off
    # Insert description
    concepts_py = concepts_py.replace('description = INSERT_HERE', f'description = """{description_txt}"""')
    concepts_py = concepts_py.replace('about_mws = INSERT_HERE', f'about_mws = """{about_mws_txt}"""')
    concepts_py = concepts_py.replace('about_workspace = INSERT_HERE', f'about_workspace = """{about_workspace_txt}"""')
    concepts_py = concepts_py.replace('about_plugin = INSERT_HERE', f'about_plugin = """{about_plugin_txt}"""')
    concepts_py = concepts_py.replace('about_run = INSERT_HERE', f'about_run = """{about_run_txt}"""')

    # Write to output file
    write_output_file("openad-toolkit/" + filename, concepts_py)
