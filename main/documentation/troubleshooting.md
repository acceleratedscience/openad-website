# Troubleshooting

Here are some common problems you may come across:

-   When updating to OpenAD `0.4.0` or above, first remove all toolkits by runnning `list toolkits` and then `remove toolkit <toolkit_name>`.
-   If you can't get openAD to run, try deleting the `~/.openad` directory, especially if you have run older versions of OpenAD in the past. Make sure to back up your workspaces if you want to keep your files.
-   When installing on macOS without a virtual environment, you may need to use `python3` and `pip3` instead of `python` and `pip`.
-   Ensure you're running Python **3.10.10+** or **3.11** - see [Upgrading Python](installation.md#upgrading-python). Due to an issue with one of our dependencies, Python 3.12 is not yet supported.
