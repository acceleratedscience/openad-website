---
draft: false
description: Learn how to use OpenAD to visualize a batch of molecules in Jupyter Notebook from a list of SMILES or InChI strings.
date: 2025-03-19
authors:
    - moenen
categories:
    - Tutorials
    - Small Molecules
    - Visualization
---

# Visualizing Molecules in Jupyter Notebook from a List or DataFrame

Learn how to use OpenAD in Juptyter Notebook to visualize a list of SMILES or InChI strings.

<!-- more -->

<!-- INSERT:INSTALL_OPENAD_JUP.md -->

<!-- INSERT:JUP_VS_CLI.md -->

## Visualizing a List of Molecules

You can also visualize a batch of molecules from an [SDF or CSV file](../02-visualizing-sdf/_post.md#visualize-molecule-files) or [individually by identifier](../01-visualizing-smol-jupyter/_post.md#visualizing-a-single-molecule).

In practice, the output from a model or other tool will often result in a large batch of molecule identifiers stored in a list of DataFrame. OpenAD makes it easy to evaluate these results by visualizing them without the need of first storing them to disk.

For this demo, we'll start with a list of SMILES (InChI are also supported) of common hormones and convert them into a Pandas DataFrame with a "smiles" column.

```shell
import pandas as pd
my_mols = [
    'C[C@]12CCC(=O)C=C1CC[C@@H]3[C@@H]2[C@H](C[C@]4([C@H]3CC[C@@H]4C(=O)CO)C=O)O',
    'C[C@]12CCC(=O)C=C1CC[C@@H]3[C@@H]2[C@H](C[C@]4([C@H]3CC[C@@]4(C(=O)CO)O)C)O',
    'C[C@]12CC[C@H]3[C@H]([C@@H]1CC[C@@H]2O)CCC4=CC(=O)CC[C@]34C',
    'C[C@]12CC[C@H]3[C@H]([C@@H]1CC[C@@H]2O)CCC4=C3C=CC(=C4)O',
    'CC(=O)[C@H]1CC[C@@H]2[C@@]1(CC[C@H]3[C@H]2CCC4=CC(=O)CC[C@]34C)C',
    'C1=C(C=C(C(=C1I)OC2=CC(=C(C(=C2)I)O)I)I)C[C@@H](C(=O)O)N',
    'CC(=O)NCCC1=CNC2=C1C=C(C=C2)OC',
    'CNC[C@@H](C1=CC(=C(C=C1)O)O)O',
    'CC[C@H](C)[C@H]1C(=O)N[C@H](C(=O)N[C@H](C(=O)N[C@@H](CSSC[C@@H](C(=O)N[C@H](C(=O)N1)CC2=CC=C(C=C2)O)N)C(=O)N3CCC[C@H]3C(=O)N[C@@H](CC(C)C)C(=O)NCC(=O)N)CC(=O)N)CCC(=O)N'   
]
my_df = pd.DataFrame(my_mols, columns=['smiles'])
```

Next, we can visualize the DataFrame:

```shell
%openad show molset using dataframe my_df
```

![Display a list of molecules from a Pandas DataFrame](display-molecules-from-dataframe.png){ .img-border }

As you can see, we don't get much more information than the SMILES and a vizualization. You could open the detail page of any of these molecules and click the "Enrich" button to fetch data from PubChem, or a more easy way is to load the molecules into your working set, and enrich them all at once.

```shell
%openad load molecules from dataframe my_df enrich
```

This will take a minute to loop through the molecules, but when you then visualize your working set next, you'll see that you now have an enriched list with all the molecule's names, as well as a bunch of properties that are available on PubChem.

```shell
%openad show molecules
```

![Display a list of molecules enriched with data from PubChem](display-enriched-molecules.png){ .img-border }

![Display a progesterone molecules enriched with data from PubChem](enriched-molecule-progesterone.png){ .img-border }

<!-- INSERT:CONTINUE_LEARNING_SMOLS.md -->