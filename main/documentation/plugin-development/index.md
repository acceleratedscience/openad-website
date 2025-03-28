# Plugin Developer Guide <!-- omit in toc -->

Creating your own plugins is easy if you have a basic understanding of Python. With only a few steps you can expose your own projects (or your favorite tools) to access OpenAD's powerful visualisation capabilities and more.

## Tl;dr <!-- omit in toc -->

Clone the [Demo plugin](https://github.com/acceleratedscience/openad-plugin-demo), install with `-e` and figure it out based on the instructions in the file.

<!-- ### Table of Contents
- [Step-by-Step Guide](#step-by-step-guide)
	- [1. Download the Demo Plugin Scaffold](#1-download-the-demo-plugin-scaffold)
	- [2. Set Plugin Parameters](#2-set-plugin-parameters)
	- [3. Clean Up](#3-clean-up)
	- [4. Create Your First Command](#4-create-your-first-command)
	- [5. Test Your Code](#5-test-your-code) -->
  
## Step-by-Step Guide

### 1. Download the Demo Plugin Scaffold

<div class="padded-list-next"></div>

- Clone the plugin repo

	```shell
	git clone --no-remote git@github.com:acceleratedscience/openad-plugin-demo.git
	```

- Install the downloaded plugin with the `--editable` flag, so you can edit the plugin code:

	```shell
	cd openad-plugin-demo
	```
	```shell
	pip install -e .
	```

### 2. Set Plugin Parameters

!!! note
	Your plugin namespace will be prepended to all your commands, and will also be how your users request your plugin documentation. Keep it concise and uniqe, ideally 2-3 characters.

<div class="tight-list-next"></div>

- [plugin_metadata.yml]  
Set your plugin name, namespace, etc.

- [plugin_description.txt]  
Replace with your own plugin description, or delete this file and use the `description` fields in [plugin_metadata.yml] instead.

### 3. Orientation

- [/commands]  
This is where your commands live. There's a few examples to learn from, delete them when you no longer need them.
- [plugin_grammar_def.py]  
Place your PyParsing grammer definitions here, so they can be reused across commands.
- [plugin_params.py]  
Remove everything under `# --- Edit below this line --- #` and replace with any variables you'll share between commands.


### 4. Create Your First Command

- Duplicate the [commands/hello_world] directory as a scaffold for your first command. Edit all parts where you see `# <-- EDIT`, the comments will guide you.
- Create your command definition underneath the `# Command definition` comment.  
Get up to speed with our [PyParsing 101](pyparsing-101.md).
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

[plugin_metadata.yml]: https://github.com/acceleratedscience/openad-plugin-demo/blob/main/openad_plugin_demo/plugin_metadata.yaml
[plugin_grammar_def.py]: https://github.com/acceleratedscience/openad-plugin-demo/blob/main/openad_plugin_demo/plugin_grammar_def.py
[plugin_params.py]: https://github.com/acceleratedscience/openad-plugin-demo/blob/main/openad_plugin_demo/plugin_params.py
[plugin_description.txt]: https://github.com/acceleratedscience/openad-plugin-demo/blob/main/openad_plugin_demo/plugin_description.txt
[/commands]: https://github.com/acceleratedscience/openad-plugin-demo/blob/main/openad_plugin_demo/commands
[commands/hello_world]: https://github.com/acceleratedscience/openad-plugin-demo/blob/main/openad_plugin_demo/commands/hello_world
[XXXXX]: https://github.com/acceleratedscience/openad-plugin-demo/blob/main/openad_plugin_demo/XXXXXX