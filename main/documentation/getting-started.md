# Getting Started with OpenAD

## Tl;dr

Get started in your terminal:

```shell
openad
```

Get started with Jupyter Notebook examples:

```shell
init_magic
init_examples
jupyter lab ~/openad_notebooks/Table_of_Contents.ipynb
```

!!! warning

    If you get an error when running `init_magic`, you may first need to setup the default iPython profile for magic commands.

    ```shell
    ipython profile create
    ```

## Getting Started - CLI

-   **Enter the virtual environment**

    ```shell
    source ~/ad-venv/bin/activate
    ```

-   **Enter the command shell**

    ```shell
    openad
    ```

-   **Exit the command shell**<br>
    Hit `ctrl+c` or run:

    ```shell
    exit
    ```

-   **Run a single command from outside the command shell**

    ```shell
    openad <command>
    ```

-   **Exit the virtual environment**<br>

    ```shell
    deactivate
    ```

-   **Running Bash Commands**

    To run a command in bash mode, prepend it with `openad` and make sure to escape quotes.

    ```shell
    openad show molecules using file \'base_molecules.sdf\'
    ```

## Getting Started - Jupyter

### Setting up Jupyter

The following commands only need to be run once after installation:

<div class="padded-list-next"></div>

1.  **Activate your virtual environment**

    ```shell
    source ~/ad-venv/bin/activate
    ```

2.  **Create an iPython kernel**<br>
    This ports your virtual environment to Jupyter.

    ```shell
    python -m ipykernel install --user --name=ad-venv
    ```

    > **Note:** List your installed iPython kernels: `jupyter kernelspec list`  
    > Remove a kernel: `jupyter kernelspec uninstall ad-venv`

3.  **Install the magic commands**<br>
    This enables OpenAD commands to be run within a Jupyter Notebook.

    ```shell
    init_magic
    ```

    <details>
    <summary><b>Alternative:</b> Manually add magic commands</summary>
    <div markdown="block">

    If you don't want to activate magic commands in all Notebooks, you can instead activate them for individual Notebooks.

    -   Run `init_examples`
    -   Copy the file `~/openad_notebooks/openad.ipynb` to the same directory as the Notebook you wish to activate.
    -   In your Notebook, run this inside a code cell: `!run openad.ipynb`

    </div>
    </details>

4.  **Install example Notebooks**<br>
    This installs our example Notebooks at `~/openad_notebooks`.

    ```shell
    init_examples
    ```

<br>

###### Launching OpenAD in Jupyter

1.  **Open any Notebook**<br>
    The following command will open up the example Notebook:

    ```shell
    jupyter lab ~/openad_notebooks/Table_of_Contents.ipynb
    ```

1.  **Select the kernel**<br>
    Make sure to select the "ad-venv" iPython kernel. You can do this under _Kernel > Change Kernel_, or in the latest versions of Jupyter by clicking the kernel name in the top right hand corner. If you don't see your iPython kernel, make sure you followed the Jupyter Setup instructions listed above.

    ![Jupyter Notebook kernel](../assets/jupyter-notebook-kernel.png)
    ![Jupyter Lab kernel](../assets/jupyter-lab-kernel.png)
    <!-- <img src="../assets/jupyter-notebook-kernel.png"> -->
    <!-- <img src="../assets/jupyter-lab-kernel.png"> -->

1.  **Magic Commands**<br>
    Magic commands let you access any OpenAD CLI command from within Jupyter. They are invoked by the `%openad` prefix.

    ```shell
    %openad list files
    ```

    If you wish to retrieve data from an OpenAD command, you can use the `%openadd` prefix instead. This will return raw, unstyled data for further processing.

    ```shell
    my_data = %openadd display data 'my_data_file.csv'
    ```
