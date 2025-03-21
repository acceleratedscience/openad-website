---
draft: false
description: Learn how to use OpenAD to visualize the contents of SDF, MOL, CSV & SMI files in a convenient molecule grid.
date: 2025-03-18
categories:
    - Tutorials
    - Small Molecules
    - Visualization
---

# How to Visualize SDF files and Other Molecular File Formats

Learn how to use OpenAD to visualize the contents of different molecular file formats in a convenient molecule grid.

Supported file formats are SDF, CSV, SMI and MOL.

<!-- more -->

<!-- INSERT:INSTALL_OPENAD.md -->

<!-- INSERT:CLI_VS_JUP.md -->

## Visualize Molecule Files

You can also visualize a batch of molecules from a [list or DataFrame](../03-visualizing-list-df/_post.md#visualizing-a-list-of-molecules) or [individually by identifier](../01-visualizing-smol-jupyter/_post.md#visualizing-a-single-molecule).

Let's start with downloading a sample for each of our supported file formats:

- SDF file: [sample_molecules1.sdf](/_assets/sample_molecules/sample_molecules1.sdf)
- CSV file: [sample_molecules2.csv](/_assets/sample_molecules/sample_molecules2.csv)
- SMI file: [sample_molecules3.smi](/_assets/sample_molecules/sample_molecules3.smi)
- MOL file: [geraniol.mol](/_assets/sample_molecules/geraniol.mol)

Now copy the files over to your workspace. Update the source paths if needed.

```shell
import from '~/Downloads/sample_molecules1.sdf' to 'sample_molecules1.sdf'
import from '~/Downloads/sample_molecules2.csv' to 'sample_molecules2.csv'
import from '~/Downloads/sample_molecules3.smi' to 'sample_molecules3.smi'
import from '~/Downloads/geraniol.mol' to 'geraniol.mol'
```

You should get a success message if they're copied over successfully. You can check by listing the files in your workspace:

```shell
list files
```

Next, you can simply open the files to see the molecules inside.

```shell
open 'sample_molecules1.sdf'
```

```shell
open 'sample_molecules2.csv'
```

```shell
open 'sample_molecules3.smi'
```

```shell
open 'geraniol.mol'
```

![Visualizing an SDF file](sdf-file.png){ .img-border }

This works both from the command line or from a Jupyter Notebook:

```shell
%openad open 'sample_molecules1.sdf'
```

![Visualizing an SDF file](sdf-file-jupyter.png){ .img-border }

From here, you can open a molecule to see more details and a 3D visualization. You can even enrich a molecule by fetching data from PubChem.

![Molecule detail](molecule-detail.png){ .img-border }

To learn how to combine molecules from different files and manipulate them together, you may want to learn about [working with the molecule working set](../04-working-with-mws/_post.md).

<!-- INSERT:CONTINUE_LEARNING_SMOLS.md -->