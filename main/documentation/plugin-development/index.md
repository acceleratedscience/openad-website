<!--
TODO:
When creating your own plugin documentation, make sure to follow the same desciption patterns as other OpenAD commands.
- We have a number of readymade grammar definitions that can be imported as building blocks. You can check this out here:
-->

# Plugin Developer Guide

Creating your own plugins is easy if you have a basic understanding of Python. With only a few steps you can expose your own projects (or your favorite tools) to access OpenAD's powerful visualisation capabilities and more.

!!! info
	For a detailed start-to-finish example, check out our [How to Build a Plugin for OpenAD](https://openad.accelerate.science/blog/2025/04/02/how-to-build-a-plugin-for-openad) tutorial

## Tl;dr

Clone the [Demo plugin](https://github.com/acceleratedscience/openad-plugin-demo), then `pip install -e .` and let the in-file instructions guid you.
  
## Step-by-Step Guide

### 1. Clone the Demo Plugin Scaffold

```shell
git clone --no-remote git@github.com:acceleratedscience/openad-plugin-demo.git
```

### 2. Name your Plugin

- Change the parent directory from `openad-plugin-demo` to `openad-plugin-<plugin-name>`
- Change the plugin directory from `openad_plugin_demo` to `openad_plugin_<plugin_name>`
- Update the `name` field in `pyproject.toml` to `openad_plugin_<plugin_name>`

### 3. Install the Plugin

Install the downloaded plugin with the `--editable` flag, so you can edit the plugin code:

```shell
cd openad-plugin-<plugin-name>
```
```shell
pip install -e .
```

### 4. Set Plugin Parameters

!!! note
	Your plugin namespace will be prepended to all your commands, and will also be how your users request your plugin documentation. Keep it concise and uniqe, ideally 2-3 characters.

- [pyproject.toml]  
This is your installation file, replace placeholder content.

- [plugin_metadata.yml]  
Set your plugin name, namespace, etc.

- [plugin_description.txt]  
Replace with your own plugin description, or delete this file and use the `description` fields in [plugin_metadata.yml] instead.

### 5. Orientation

- [/commands]  
This is where your commands live. There's a few examples to learn from, delete them when you no longer need them.
- [plugin_grammar_def.py]  
Place your PyParsing grammer definitions here, so they can be reused across commands.
- [plugin_params.py]  
Remove everything under `# --- Edit below this line --- #` and replace with any variables you'll share between commands.


### 4. Create Your First Command

- Duplicate the [commands/hello_world] directory as a scaffold for your first command.
- Look for `# <-- UPDATE` and update the import statements to `openad_plugin_<plugin_name>`
- Look for `# <-- EDIT` and edit, the comments will guide you.
- Look for `# Command definition` and compose your command definition. Some tips:
    - Get up to speed with our [PyParsing 101]
    - Save time with our readymade PyParsing definitions: [openad_tools.grammar_def.py](https://github.com/acceleratedscience/openad-tools/blob/main/openad_tools/grammar_def.py)
- Put your command logic inside `def exec_command()`.  
Check our [Knowledge Base](knowledge-base.md) to learn about how to return data, use our display tools and more.

Repeat for every command.
  
### 5. 🎉 That's It

Relaunch openad every time you want to see an edit you made.

```shell
exit
```
```shell
openad
```

[pyproject.toml]: https://github.com/acceleratedscience/openad-plugin-demo/blob/main/pyproject.toml
[plugin_metadata.yml]: https://github.com/acceleratedscience/openad-plugin-demo/blob/main/openad_plugin_demo/plugin_metadata.yaml
[plugin_grammar_def.py]: https://github.com/acceleratedscience/openad-plugin-demo/blob/main/openad_plugin_demo/plugin_grammar_def.py
[plugin_params.py]: https://github.com/acceleratedscience/openad-plugin-demo/blob/main/openad_plugin_demo/plugin_params.py
[plugin_description.txt]: https://github.com/acceleratedscience/openad-plugin-demo/blob/main/openad_plugin_demo/plugin_description.txt
[/commands]: https://github.com/acceleratedscience/openad-plugin-demo/blob/main/openad_plugin_demo/commands
[commands/hello_world]: https://github.com/acceleratedscience/openad-plugin-demo/blob/main/openad_plugin_demo/commands/hello_world
[XXXXX]: https://github.com/acceleratedscience/openad-plugin-demo/blob/main/openad_plugin_demo/XXXXXX
[PyParsing 101]: pyparsing-101.md