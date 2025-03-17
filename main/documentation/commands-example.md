<!--

DO NOT EDIT
-----------
This file is auto-generated.
To update it, consult instructions:
https://github.com/acceleratedscience/open-ad-toolkit/tree/main/docs

-->

# OpenAD Commands

!!! warning

    This page is still under construction. Please refer to the built-in help for command documentation. [information here](getting-started.md#getting-started-jupyter).

<!-- This is the full list of available OpenAD commands.

!!! info

    When running commands from Jupyter, prepend them with `%openad` -->

### Macromolecules

<details markdown code>
<summary markdown>
show mmol | protein &lt;fasta&gt; | '&lt;pdb_id&gt;'
</summary>

Launch the molecule viewer to visualize your macromolecule and inspect its properties.

#### Examples

Show a protein by its PDBe ID:

```shell
show mmol '2g64'
```

Show a protein by its FASTA string:

```shell
show protein MAKWVCKICGYIYDEDAGDPDNGISPGTKFEELPDDWVCPICGAPKSEFEKLED
```

</details>
