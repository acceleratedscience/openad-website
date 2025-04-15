# Installing OpenAD

<div class="sub-title" markdown>
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/openad)](https://pypi.org/project/openad/)
[![PyPI version](https://img.shields.io/pypi/v/openad)](https://pypi.org/project/openad/)
[![License MIT](https://img.shields.io/github/license/acceleratedscience/open-ad-toolkit)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
</div>

## Tl;dr

```shell
pip install openad
```

```shell
openad
```

!!! info

    When installing on macOS without a virtual environment, you may need to use `python3` and `pip3` instead of `python` and `pip`.

## Installing on macOS / Linux

!!! info

    -   **Contributors:** Skip to [Installation for Development](developers.md#installation-for-development)
    -   **Linux users:** Check the [Linux Notes](#linux-notes)
    -   **Poetry:** If you prefer Poetry, you can run the setup wizard instead: `poetry add openad`

<!-- Note: step 1 & 2 are repeated, make sure any updates are done in both places -->

<div class="padded-list" markdown>

1.  **Before you start**  
    Ensure you're running Python 3.10.10+ or 3.11 - see [Upgrading Python](installation.md#upgrading-python).

    To see what version you are running:

    ```shell
    python -V
    ```

    > **Note:** Due to an issue with one of our dependencies, Python 3.12 is not yet supported.

2.  **Set up your virtual environment** (recommended)

    ```shell
    python -m venv ~/ad-venv
    ```

    ```shell
    source ~/ad-venv/bin/activate
    ```

    > **Note:** Use `python3` on macOS.  
    > **Note:** To exit the virtual environment, you can run `deactivate`

3.  **Install OpenAD**

    ```shell
    pip install openad
    ```

4.  Continue to [Getting Started]

</div>

## Installing on Windows

In order to run OpenAD on Windows 11, you will need to install the Ubuntu [WSL](https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux) package.

<div class="padded-list" markdown>

1.  **Verify Windows version**  
    To check if you are running Windows 11 or later, press `Win` + `R`, type "winver", and press `Enter`. A window will open showing your Windows version.

2.  **Verify WSL**  
    To check if you already have WSL installed, run `wsl -l -v` into the terminal. To see more information about your current version of Ubuntu, run `lsb_release -a`

3.  **Install WSL**  
    Install WSL and create a user called 'openad' or one of your choosing.

    ```shell
    wsl --install Ubuntu-22.04
    ```

    **Optional:** To setup an Ubuntu Python environment from scratch, continue to <a href="#linux-notes">Linux Notes</a>

4.  Continue to [Getting Started]

</div>

## Appendix

### Upgrading Python

There's many ways to install or upgrade Python. We'll use `pyenv`.

<div class="padded-list" markdown>

1.  **Install pyenv**

    ```shell
    curl https://pyenv.run | bash
    ```

2.  **Set up your shell environment for Pyenv**  
    Detailed instructions can be found [here](https://github.com/pyenv/pyenv?tab=readme-ov-file#set-up-your-shell-environment-for-pyenv). If you're using Zsh, you can run the commands below:

    ```shell
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
    ```

    ```shell
    echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
    ```

    ```shell
    echo 'eval "$(pyenv init -)"' >> ~/.zshrc
    ```

3.  **Reboot your shell**  
    You can either open a new window or run:

    ```shell
    exec $SHELL
    ```

4.  **Install Python**  
    Please note that OpenAD requires **Python 3.10.10+** or **3.11**.  
    Due to an issue with one of our dependencies, Python 3.12 is not yet supported.

    ```shell
    pyenv install 3.11
    ```

5.  **Activate this version of Python**  
    If you wish to set this version as the default:

    ```shell
    pyenv global 3.11
    ```

    Alternatively, if you only wish to activate it in the current shell:

    ```shell
    pyenv shell 3.11
    ```

6. **Good to know:**  
    If you're setting up a virtual environment, you need to set the python version _before_ creating the venv.

    ```shell
    pyenv shell 3.11
    ```
    ```shell
    python -m venv my_venv
    ```

    You can see the list of installed versions by running:
    
    ```shell
    pyenv versions
    ```
    
    You can see the currently installed version by running:
    
    ```shell
    pyenv version
    ```

</div>

### Linux Notes

If you wish to setup an Ubuntu Python environment from scratch, run:

```shell
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.11-full
sudo apt install python3-pip
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 100
sudo pip install pip --upgrade
```

You will need to restart your Linux session before running `pip install openad` so that the python libraries are in your path.

If you get an error when running `init_magic`, you may first need to setup the default iPython profile for magic commands.

```shell
ipython profile create
```

[Getting Started]: getting-started.md
