# API Access

Use the API to run any command from a python script and capture the result for further processing.

This lets you integrate OpenAD into larger workflows involving other tools.

## The Basics

```python
from openad import OpenadAPI

oad = OpenadAPI()
result = oad.request("<command goes here>")

print(result)
```

## Example A - Workspace / File System

In this example we filter out all files in your workspace starting with "sample-" and move them into a folder "samples".

[Open in Colab](https://colab.research.google.com/drive/1pxngmGxZtsvAoWfaWw6oas3POQqALSJw){ .md-button target=\_BLANK }

```python
from openad import OpenadAPI
oad = OpenadAPI()

# Get dataframe with files in your workspace
files_df = oad.request("list files")

# Filter out all files starting with 'sample-'
files_df_filtered = files_df[files_df["File Name"].str.startswith("sample-")]

# Scan for files
filenames = []
for file in files_df_filtered["File Name"]:
    filenames.append(file)

# No relevant files found
if len(filenames) == 0:
    print("⛔️ No files found that start with 'sample-'")

# List relevant files
else:
    print("The following files will be moved to the 'samples' directory:")
    print('-----------------------------------------------')
    print("• " + "\n• ".join(filenames))

    # Ask for confirmation
    cont = input("\nAre you sure you want to continue? (y/n)")

    # Move files
    if cont == "y":
        for fn in filenames:
            oad.request(f"move '{fn}' to 'samples' force")
        print(f"\n✅ {len(files_df_filtered)} files were moved into the 'samples' directory")

    # Abort
    else:
        print("\n❌ (No files were moved)")
```

## Example B - Molecule Working Set

In this example we'll use the Deep Search plugin to search scientific literature for molecules that are similar to a provided SMILES, and use RDKit to generate SVG images for each result.

[Open in Colab](https://colab.research.google.com/drive/1KIGI3syyIfBxR_FlVSnDwNonriSTWCVk){ .md-button target=\_BLANK }

```python
import os
from rdkit import Chem
from IPython.display import SVG, display, HTML

from openad import OpenadAPI
oad = OpenadAPI()

# Use Deep Search to search for similar molecules
candidates = oad.request("ds search for molecules similar to CC(=CCC/C(=C/CO)/C)C")

# Get your workspace path
cmd_pointer = oad.request("cmd_pointer")
workspace_path = cmd_pointer.workspace_path()

# Generate SVG image for each result
for i, smiles in enumerate(candidates["smiles"], start=1):

  # Generate SVG string using RDKit
  mol_rdkit = Chem.MolFromSmiles(smiles)
  mol_drawer = Chem.Draw.MolDraw2DSVG(400, 300)
  mol_drawer.DrawMolecule(mol_rdkit)
  mol_drawer.FinishDrawing()
  svg_str = mol_drawer.GetDrawingText()

  # Store SVG to your workspace
  destination_path = os.path.join(workspace_path, f"candidate-{i}.svg")
  with open(destination_path, "w") as f:
    _ = f.write(svg_str)

  # Visualize the SVG in the notebook
  print(f"---\nCandidate #{i}\n{smiles}:")
  SVG(svg_str)
```
