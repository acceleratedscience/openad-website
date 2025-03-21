---
draft: false
description: Learn how to import PDB data into your OpenAD workspace.
date: 2025-03-25
categories:
    - Tutorials
    - Proteins
---

# How to Import Proteins from the Protein Data Bank

Learn how to use OpenAD to easily import protein data from the RCSB Protein Data Bank using a protein's PDB ID or FASTA string.

<!-- more -->

<!-- INSERT:INSTALL_OPENAD.md -->

<!-- INSERT:CLI_VS_JUP.md -->

## Importing a Protein

First we visualize a protein, either by its PDB id, or by searching for a FASTA string:

```shell
show protein '9J4J'
```

```shell
show protein 'MSLNRHFTVSVFIVCKDKVLLHLHKKAKKMLPLGGHIEVNELPEEACIREAKEEAGLNVTLYNPIDINLKKSCDLSGEKLLINPIHTILGDVSPNHSHIDFVYYATTTSFETSPEIGESKILKWYSKEDLKNAHNIQENILVMATEALDLLEGHHHHHH'
```

This will open the protein in the macromolecule viewer, from where you can save it to your workspace.

![View protein](view-protein.png){ .img-border }

![View protein](save-protein.png){ .img-border }

<!-- INSERT:CONTINUE_LEARNING_PROTEINS.md -->