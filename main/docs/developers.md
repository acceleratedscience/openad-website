# OpenAD for Developers

OpenAD is fully open source and we encourage contributions.  
If you have any questions, please [get in touch](../about.md).

## Developing Plugins

Building your own OpenAD plugin lets you to integrate your own tools into the OpenAD workflow.

Jump to the [plugin developer guide](plugin-development/index.md) for detailed instructions.

## Installation for Development

<details markdown>
<summary>Install using the setup wizard (uses poetry)</summary>
<div class="padded-list" markdown>

1.  **Step 1: Download the repo**

    ```shell
    git clone https://github.com/acceleratedscience/open-ad-toolkit.git
    ```

    Or to download a specific branch, you can run instead:

    ```shell
    git clone -b <branch_name> https://github.com/acceleratedscience/open-ad-toolkit.git
    ```

2.  **Step 2: Launch the setup wizard**

    ```shell
    cd open-ad-toolkit
    ./setup.sh
    ```

</div>
</details>

<details markdown>
<summary>Install using pip</summary>
<div class="padded-list" markdown>

<!-- Note: step 1 & 2 are repeated, make sure any updates are done in both places -->

1.  **Step 0: Before you start**  
    Ensure you're running Python 3.10.10+ or 3.11 - see [Upgrading Python](installation.md#upgrading-python).

    To see what version you are running:

    ```shell
    python -V
    ```

    > **Note:** Due to an issue with one of our dependencies, Python 3.12 is not yet supported.

2.  **Step 1: Set up your virtual environment** (recommended)

    ```shell
    python -m venv ~/ad-venv
    source ~/ad-venv/bin/activate
    ```

    > **Note:** Use `python3` on macOS.  
    > **Note:** To exit the virtual environment, you can run `deactivate`

3.  **Step 2: Download the repo**

    ```shell
    git clone https://github.com/acceleratedscience/open-ad-toolkit.git
    ```

    Or to download a specific branch, you can run instead:

    ```shell
    git clone -b <branch_name> https://github.com/acceleratedscience/open-ad-toolkit.git
    ```

4.  **Step 2: Install OpenAD**

    ```shell
    cd open-ad-toolkit
    pip install -e .
    ```

    > **Note:** The -e flag stands for "editable". This means that instead of copying the package's files to the Python site-packages directory as in a regular installation, pip creates a symbolic link (symlink) from your package's source code directory into your Python environment.  
    > This way you can make changes to the source code of the package, and those changes are immediately reflected in your Python environment. You don't need to reinstall the package every time you make a change.

</div>
</details>

## Testing a branch

To do a regular install from a particular branch, you can run:

```shell
pip install git+https://github.com/acceleratedscience/open-ad-toolkit.git@<branch_name>
```

<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
