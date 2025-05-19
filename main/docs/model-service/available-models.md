<!--

DO NOT EDIT
-----------
This file is auto-generated.
To update it, consult instructions:
https://github.com/acceleratedscience/openad-website/tree/generator

-->

# Publicly Available Models

Below an overview of our available open-source models. Find them on [GitHub here](https://github.com/orgs/acceleratedscience/repositories?q=%22openad-service-%22).  
Go to [Deploying Models](deploying-models.md) for more detailed deployment options beyond the quick-start.

<br><br>

<details markdown><summary><h4>SMI-TED &nbsp;/&nbsp; Property Prediction on SMILES Input</h4></summary>
<div markdown>

[:carbon-icn-github: openad-service-smi-ted](https://github.com/acceleratedscience/openad-service-smi-ted){ .md-button }
[compose.yml](https://raw.githubusercontent.com/acceleratedscience/openad-service-smi-ted/main/compose.yaml){ .md-button .md-button--primary download='compose.yml' }
[Instructions](/docs/model-service/deploying-models.md#deployment-via-container-composeyaml-recommended){ .md-button .md-button--tertiary }  

This OpenAD service provides access to **SMILES-based Transformer Encoder-Decoder** (SMI-TED), a foundation model for materials science and chemistry. SMI-TED is an encoder-decoder model pre-trained on a curated dataset of 91 million SMILES samples sourced from PubChem, equivalent to 4 billion molecular tokens. SMI-TED offers several predictive models, including quantum property prediction, with two main variants ( 289 M and 8 × 289 M ).

More information:  
[github.com/IBM/materials](https://github.com/IBM/materials)  
[huggingface.co/ibm/materials.smi-ted](https://huggingface.co/ibm/materials.smi-ted)  
[arxiv.org/abs/2407.20267](https://arxiv.org/abs/2407.20267)


Support for:  
✅ Docker / Podman Compose  
✅ Docker / Podman  
✅ Google Cloud Run  
✅ Apple Silicon - [more info](/docs/model-service/deploying-models.md#apple-silicon)  


Quick start with Docker Compose:
```
curl -O https://raw.githubusercontent.com/acceleratedscience/openad-service-smi-ted/main/compose.yaml
```
```
docker compose create
```
```
docker compose start
```
```
openad
```
```
catalog model service from remote 'http://127.0.0.1:8080' as smi_ted
```

</div>
</details>

<details markdown><summary><h4>BMFM-SM &nbsp;/&nbsp; Property Prediction on SMILES Input</h4></summary>
<div markdown>

[:carbon-icn-github: openad-service-bmfm-sm](https://github.com/acceleratedscience/openad-service-bmfm-sm){ .md-button }
[compose.yml](https://raw.githubusercontent.com/acceleratedscience/openad-service-bmfm-sm/main/compose.yaml){ .md-button .md-button--primary download='compose.yml' }
[Instructions](/docs/model-service/deploying-models.md#deployment-via-container-composeyaml-recommended){ .md-button .md-button--tertiary }  

This OpenAD service provides access to BioMedical Foundation Models: Small Molecules (BMFM-SM), namely the **Biomed-multi-view** foundation model. BMFM-SM has models for predicting many properties from the well-known MoleculeNet benchmarks:

| BACE | BBBP | CLINTOX | ESOL | FREESOLV | HIV |
| ---- | ---- | ------- | ---- | -------- | --- |

| LIPOPHILICITY | MUV | QM7 | SIDER | TOX21 | TOXCAST |
| ------------- | --- | --- | ----- | ----- | ------- |

More information:  
[github.com/BiomedSciAI/biomed-multi-view](https://github.com/BiomedSciAI/biomed-multi-view)  
[arxiv.org/abs/2410.19704](https://arxiv.org/abs/2410.19704)


Support for:  
✅ Docker / Podman Compose  
✅ Docker / Podman  
☹️ Google Cloud Run  
✅ Apple Silicon - [more info](/docs/model-service/deploying-models.md#apple-silicon)  


Quick start with Docker Compose:
```
curl -O https://raw.githubusercontent.com/acceleratedscience/openad-service-bmfm-sm/main/compose.yaml
```
```
docker compose create
```
```
docker compose start
```
```
openad
```
```
catalog model service from remote 'http://127.0.0.1:8080' as bmfm_sm
```

</div>
</details>

<details markdown><summary><h4>BMFM-PM &nbsp;/&nbsp; Property Prediction on FASTA Input using MAMMAL</h4></summary>
<div markdown>

[:carbon-icn-github: openad-service-bmfm-pm](https://github.com/acceleratedscience/openad-service-bmfm-pm){ .md-button }
[compose.yml](https://raw.githubusercontent.com/acceleratedscience/openad-service-bmfm-pm/main/compose.yaml){ .md-button .md-button--primary download='compose.yml' }
[Instructions](/docs/model-service/deploying-models.md#deployment-via-container-composeyaml-recommended){ .md-button .md-button--tertiary }  

This OpenAD service provides access to the **Biomed-multi-alignment** foundation model, with two models for protein property prediction that take FASTA string input: **protein solubility** (Sol) and **drug-target interaction** (DTI), which takes SMILES for the drug input and FASTA for the target input.

- **Sol** task is from benchmark data defined here: https://academic.oup.com/bioinformatics/article/34/15/2605/4938490
- **DTI** task is from benchmark data from TD Commons: https://tdcommons.ai/multi_pred_tasks/dti/

More information:  
[github.com/BiomedSciAI/biomed-multi-alignment](https://github.com/BiomedSciAI/biomed-multi-alignment)


Support for:  
✅ Docker / Podman Compose  
✅ Docker / Podman  
☹️ Google Cloud Run  
☹️ Apple Silicon - [more info](/docs/model-service/deploying-models.md#apple-silicon)  


Quick start with Docker Compose:
```
curl -O https://raw.githubusercontent.com/acceleratedscience/openad-service-bmfm-pm/main/compose.yaml
```
```
docker compose create
```
```
docker compose start
```
```
openad
```
```
catalog model service from remote 'http://127.0.0.1:8080' as bmfm_pm
```

</div>
</details>

<details markdown><summary><h4>REINVENT 4 &nbsp;/&nbsp; Generative Models with SMILES Output</h4></summary>
<div markdown>

[:carbon-icn-github: openad-service-reinvent4](https://github.com/acceleratedscience/openad-service-reinvent4){ .md-button }
[compose.yml](https://raw.githubusercontent.com/acceleratedscience/openad-service-reinvent4/main/compose.yaml){ .md-button .md-button--primary download='compose.yml' }
[Instructions](/docs/model-service/deploying-models.md#deployment-via-container-composeyaml-recommended){ .md-button .md-button--tertiary }  

This OpenAD service provides access to the **REINVENT 4** molecular design tool, which is used for de novo design, scaffold hopping, R-group replacement, linker design, molecule optimization, and other small molecule design tasks. REINVENT uses a Reinforcement Learning (RL) algorithm to generate optimized molecules compliant with a user-defined property profile defined as a multi-component score. Transfer Learning (TL) can be used to create or pre-train a model that generates molecules closer to a set of input molecules. 

More information:  
[github.com/MolecularAI/REINVENT4](https://github.com/MolecularAI/REINVENT4)  
[link.springer.com/article/10.1186/s13321-024-00812-5](https://link.springer.com/article/10.1186/s13321-024-00812-5)


Support for:  
✅ Docker / Podman Compose  
✅ Docker / Podman  
✅ Google Cloud Run  
☹️ Apple Silicon - [more info](/docs/model-service/deploying-models.md#apple-silicon)  


Quick start with Docker Compose:
```
curl -O https://raw.githubusercontent.com/acceleratedscience/openad-service-reinvent4/main/compose.yaml
```
```
docker compose create
```
```
docker compose start
```
```
openad
```
```
catalog model service from remote 'http://127.0.0.1:8080' as reinvent4
```

</div>
</details>

<details markdown><summary><h4>Generation &nbsp;/&nbsp; Generative Models with SMILES or SELFIES Output</h4></summary>
<div markdown>

[:carbon-icn-github: openad-service-gen](https://github.com/acceleratedscience/openad-service-gen){ .md-button }
[Instructions](/docs/model-service/deploying-models.md#deployment-via-container){ .md-button .md-button--tertiary }  

This OpenAD service provides access to generative algorithms that output SMILES or SELFIES.

- [Regression Transformer, 2023](https://github.com/IBM/regression-transformer). Uses transformers for both regression and generation. Generates SELFIES based on desired properties.
- [PaccMann, 2020](https://paccmann.github.io/). Uses autoencoders to generate molecules to target cancer based on omics profiles.
- [TorchDrug, 2021](https://torchdrug.ai/). Offers two kinds of graph-based networks to generate SMILES: [GCPN](https://proceedings.neurips.cc/paper_files/paper/2018/file/d60678e8f2ba9c540798ebbde31177e8-Paper.pdf) and [GraphAF](https://arxiv.org/pdf/2001.09382).
- [MOSES, 2020](https://github.com/molecularsets/moses). [GuacaMol, 2019](https://github.com/BenevolentAI/guacamol). And more.

These generative algorithms were previously offered in [the open source library, GT4SD](https://github.com/GT4SD/gt4sd-core).


Support for:  
☹️ Docker / Podman Compose  
✅ Docker / Podman  
✅ Google Cloud Run  
☹️ Apple Silicon - [more info](/docs/model-service/deploying-models.md#apple-silicon)  


Quick start with Docker:
```
git clone https://github.com/acceleratedscience/openad-service-gen
```
```
cd openad-service-gen
```
```
docker build -t gen .
```
```
docker run -p 8080:8080 gen
```
```
openad
```
```
catalog model service from remote 'http://127.0.0.1:8080' as gen
```

</div>
</details>

<details markdown><summary><h4>Properties &nbsp;/&nbsp; Property Prediction on SMILES, FASTA or CIF Input</h4></summary>
<div markdown>

[:carbon-icn-github: openad-service-prop](https://github.com/acceleratedscience/openad-service-prop){ .md-button }
[Instructions](/docs/model-service/deploying-models.md#deployment-via-container){ .md-button .md-button--tertiary }  

This OpenAD service provides access to property predictive models in computational chemistry (some in the area of small molecules, others in proteins) and in materials science. For small molecules, input is in SMILES format. For proteins, input is in FASTA format. For materials science, input is in CIF file format. These models were previously offered in [the open-source library, GT4SD](https://github.com/GT4SD/gt4sd-core).


Support for:  
☹️ Docker / Podman Compose  
✅ Docker / Podman  
☹️ Google Cloud Run  
☹️ Apple Silicon - [more info](/docs/model-service/deploying-models.md#apple-silicon)  


Quick start with Docker:
```
git clone https://github.com/acceleratedscience/openad-service-prop
```
```
cd openad-service-prop
```
```
docker build -t prop .
```
```
docker run -p 8080:8080 prop
```
```
openad
```
```
catalog model service from remote 'http://127.0.0.1:8080' as prop
```

</div>
</details>

<details markdown><summary><h4>MoLeR &nbsp;/&nbsp; SMILES Generation on SMILES Scaffolds</h4></summary>
<div markdown>

[:carbon-icn-github: openad-service-moler](https://github.com/acceleratedscience/openad-service-moler){ .md-button }
[Instructions](/docs/model-service/deploying-models.md#deployment-via-container){ .md-button .md-button--tertiary }  

This OpenAD service provides access to MoLeR, a model for conditional, small-molecule (SMILES) generation based on molecular scaffold input (also SMILES). MoLeR uses TensorFlow as its deep learning platform.

More information:  
[github.com/microsoft/molecule-generation](https://github.com/microsoft/molecule-generation)  
[arxiv.org/abs/2103.03864](https://arxiv.org/abs/2103.03864)


Support for:  
☹️ Docker / Podman Compose  
✅ Docker / Podman  
☹️ Google Cloud Run  
☹️ Apple Silicon - [more info](/docs/model-service/deploying-models.md#apple-silicon)  


Quick start with Docker:
```
git clone https://github.com/acceleratedscience/openad-service-moler
```
```
cd openad-service-moler
```
```
docker build -t moler .
```
```
docker run -p 8080:8080 moler
```
```
openad
```
```
catalog model service from remote 'http://127.0.0.1:8080' as moler
```

</div>
</details>

<details markdown><summary><h4>MoLFormer &nbsp;/&nbsp; Property Prediction Highlights on SMILES Input</h4></summary>
<div markdown>

[:carbon-icn-github: openad-service-molf](https://github.com/acceleratedscience/openad-service-molf){ .md-button }
[Instructions](/docs/model-service/deploying-models.md#deployment-via-container){ .md-button .md-button--tertiary }  

MoLFormer / Three finetuned property prediction models on MoleculeNet tasks: BACE classification, ClinTox multiclass, and QM9 alpha regression.


Support for:  
☹️ Docker / Podman Compose  
✅ Docker / Podman  
☹️ Google Cloud Run  
☹️ Apple Silicon - [more info](/docs/model-service/deploying-models.md#apple-silicon)  


Quick start with Docker:
```
git clone https://github.com/acceleratedscience/openad-service-molf
```
```
cd openad-service-molf
```
```
docker build -t molf .
```
```
docker run -p 8080:8080 molf
```
```
openad
```
```
catalog model service from remote 'http://127.0.0.1:8080' as molf
```

</div>
</details>
