# Plugin Developer Guide <!-- omit in toc -->

Creating your own plugins is easy if you have a basic understanding of Python. With only a few steps you can expose your own projects (or your favorite tools) to access OpenAD's powerful visualisation capabilities and more.

## Tl;dr <!-- omit in toc -->

Clone the [Demo plugin](https://github.com/acceleratedscience/openad-plugin-demo), install with `-e` and figure it out based on the instructions in the file.

### Table of Contents
- [Step-by-Step Guide](#step-by-step-guide)
	- [1. Download the Demo Plugin Scaffold](#1-download-the-demo-plugin-scaffold)
	- [2. Set Plugin Parameters](#2-set-plugin-parameters)
	- [3. Clean Up](#3-clean-up)
	- [4. Create Your First Command](#4-create-your-first-command)
	- [5. Test Your Code](#5-test-your-code)
  
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

<div class="padded-list-next"></div>

Open [plugin_metadata.yml](https://github.com/acceleratedscience/openad-plugin-demo/blob/main/openad_plugin_demo/plugin_metadata.yaml) and set your plugin name, namespace, etc.

!!! note
	Your plugin namespace will be prepended to all your commands, and will also be how your users request your plugin documentation. Keep it concise and uniqe, ideally 2-3 characters.

### 3. Clean Up

The demo plugin comes with some example commands and features to get your started.  
Make sure to delete or replace the content in the following files.

!!! note
	If you're still learning, you may want to delete this later.

<div class="tight-list-next"></div>

- [plugin_grammar_def.py]  
Replace with your own commands' pyparsing definitions. More on that below.
- [plugin_params.py]  
Remove everything under `# --- Edit below this line --- #` and replace with any variables you'll share between commands.
- [plugin_description.txt]  
Replace with your own plugin description. Note: you can also delete this file and use the `description` fields in [plugin_grammar_def.py] instead.
- [/commands]  
Delete all command directories except the `hello_world` one.

### 4. Create Your First Command

- Duplicate the [commands/hello_world] directory as a scaffold for your first command. Edit all parts where you see `# <-- EDIT`, the comments will guide you.
- Create your command definition using pyparsing. You may want to read our [crash course on pyparsing](knowledge-base.md#pyparsing-crash-course) below.
- Put your command logic inside `def exec_command()`. Read below about [how to return data](knowledge-base.md#returning-data).

Repeat for your next commands.
  
### 5. Test Your Code

Relaunch openad every time you want to see an edit you made.


```shell
exit
```
```shell
openad
```