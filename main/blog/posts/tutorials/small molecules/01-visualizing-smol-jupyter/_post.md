---
draft: false
description: Learn how to use OpenAD to visualize a molecule in 2D and 3D from a SMILES, InChI, InChIKey, name or PubChem ID.
date: 2025-03-17
categories:
    - Tutorials
    - Small Molecules
    - Visualization
---

# How to Visualize a Molecule in Jupyter Notebook

Learn how to use OpenAD to visualize a molecule in 2D and 3D from a SMILES, InChI, InChIKey, name or PubChem ID.

<!-- more -->

<!-- INSERT:INSTALL_OPENAD_JUP.md -->

<!-- INSERT:JUP_VS_CLI.md -->

## Visualizing a Single Molecule

You can also visualize a batch of molecules from a [list or DataFrame](../03-visualizing-list-df/_post.md#visualizing-a-list-of-molecules), or from an [SDF or CSV file](../02-visualizing-sdf/_post.md#visualize-molecule-files).

```shell
%openad show molecule 'C1=CC(=C(C=C1CCN)O)O'
```

![Display a single molecule in Jupyter Notebook](display-single-molecule.png){ .img-border }


That was easy. And you can use any type of molecular identifier:  

- SMILES  
- InChI  

.. and if the molecule exists on PubChem:

- InChIKey
- name
- PubChem CID

```shell
%openad show molecule InChI=1S/C8H8/c1-2-5-3(1)7-4(1)6(2)8(5)7/h1-8H
```
```shell
%openad show molecule WAYJCOBMBRPWED-KWCYVHTRSA-N
```
```shell
%openad show molecule rubber
```
```shell
%openad show molecule 2854
```

<!-- INSERT:CONTINUE_LEARNING_SMOLS.md -->