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

<details markdown><summary><h4>SMI-TED &nbsp;/&nbsp; Inference for SMILES</h4></summary>
<div markdown>

[:carbon-icn-github: openad-service-smi-ted](https://github.com/acceleratedscience/openad-service-smi-ted){ .md-button }
[compose.yml](https://raw.githubusercontent.com/acceleratedscience/openad-service-smi-ted/main/compose.yaml){ .md-button .md-button--primary download='compose.yml' }
[Instructions](/docs/model-service/deploying-models/#deployment-via-container-composeyaml-recommended){ .md-button .md-button--tertiary }  

This OpenAD service provides access to **SMILES-based Transformer Encoder-Decoder** (SMI-TED), a foundation model for materials science and chemistry. SMI-TED is an encoder-decoder model pre-trained on a curated dataset of 91 million SMILES samples sourced from PubChem, equivalent to 4 billion molecular tokens. SMI-TED supports various complex tasks, including quantum property prediction, with two main variants ( 289 M and 8 × 289 M ).

More information:  
[github.com/IBM/materials](https://github.com/IBM/materials)  
[huggingface.co/ibm/materials.smi-ted](https://huggingface.co/ibm/materials.smi-ted)  
[arxiv.org/abs/2407.20267](https://arxiv.org/abs/2407.20267)


Support for:  
✅ Docker / Podman Compose  
✅ Docker / Podman  
✅ Google Cloud Run  
✅ Apple Silicon - [more info](/docs/model-service/deploying-models#apple-silicon)  


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

<details markdown><summary><h4>BMFM-SM &nbsp;/&nbsp; Inference for SMILES</h4></summary>
<div markdown>

[:carbon-icn-github: openad-service-bmfm-sm](https://github.com/acceleratedscience/openad-service-bmfm-sm){ .md-button }
[compose.yml](https://raw.githubusercontent.com/acceleratedscience/openad-service-bmfm-sm/main/compose.yaml){ .md-button .md-button--primary download='compose.yml' }
[Instructions](/docs/model-service/deploying-models/#deployment-via-container-composeyaml-recommended){ .md-button .md-button--tertiary }  

This OpenAD service provides access to BioMedical Foundation Models: Small Molecules (BMFM-SM), namely the **Biomed-multi-view** foundation model with checkpoints for inference on the following small-molecule properties, a subset of the MoleculeNet benchmarks:

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
✅ Apple Silicon - [more info](/docs/model-service/deploying-models#apple-silicon)  


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

<details markdown><summary><h4>BMFM-PM &nbsp;/&nbsp; Inference for Proteins using MAMMAL</h4></summary>
<div markdown>

[:carbon-icn-github: openad-service-bmfm-pm](https://github.com/acceleratedscience/openad-service-bmfm-pm){ .md-button }
[compose.yml](https://raw.githubusercontent.com/acceleratedscience/openad-service-bmfm-pm/main/compose.yaml){ .md-button .md-button--primary download='compose.yml' }
[Instructions](/docs/model-service/deploying-models/#deployment-via-container-composeyaml-recommended){ .md-button .md-button--tertiary }  

This OpenAD service provides access to the **Biomed-multi-alignment** foundation model, with checkpoints for two protein properties that work on FASTA string input: **protein solubility** (Sol) and **drug-target interaction** (DTI).

- **Sol** task is from benchmark data defined here: https://academic.oup.com/bioinformatics/article/34/15/2605/4938490
- **DTI** task is from benchmark data from TD Commons: https://tdcommons.ai/multi_pred_tasks/dti/

More information:  
[github.com/BiomedSciAI/biomed-multi-alignment](https://github.com/BiomedSciAI/biomed-multi-alignment)


Support for:  
✅ Docker / Podman Compose  
✅ Docker / Podman  
☹️ Google Cloud Run  
☹️ Apple Silicon - [more info](/docs/model-service/deploying-models#apple-silicon)  


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

<details markdown><summary><h4>REINVENT 4 &nbsp;/&nbsp; Inference for SMILES</h4></summary>
<div markdown>

[:carbon-icn-github: openad-service-reinvent4](https://github.com/acceleratedscience/openad-service-reinvent4){ .md-button }
[compose.yml](https://raw.githubusercontent.com/acceleratedscience/openad-service-reinvent4/main/compose.yaml){ .md-button .md-button--primary download='compose.yml' }
[Instructions](/docs/model-service/deploying-models/#deployment-via-container-composeyaml-recommended){ .md-button .md-button--tertiary }  

This OpenAD service provides access to the **REINVENT 4** molecular design tool, which is used for de novo design, scaffold hopping, R-group replacement, linker design, molecule optimization, and other small molecule design tasks. REINVENT uses a Reinforcement Learning (RL) algorithm to generate optimized molecules compliant with a user-defined property profile defined as a multi-component score. Transfer Learning (TL) can be used to create or pre-train a model that generates molecules closer to a set of input molecules. 

More information:  
[github.com/MolecularAI/REINVENT4](https://github.com/MolecularAI/REINVENT4)  
[link.springer.com/article/10.1186/s13321-024-00812-5](https://link.springer.com/article/10.1186/s13321-024-00812-5)


Support for:  
✅ Docker / Podman Compose  
✅ Docker / Podman  
✅ Google Cloud Run  
☹️ Apple Silicon - [more info](/docs/model-service/deploying-models#apple-silicon)  


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

<details markdown><summary><h4>Generation Inference for SMILES</h4></summary>
<div markdown>

[:carbon-icn-github: openad-service-gen](https://github.com/acceleratedscience/openad-service-gen){ .md-button }
[Instructions](/docs/model-service/deploying-models/#deployment-via-container){ .md-button .md-button--tertiary }  

_No description available._


Support for:  
☹️ Docker / Podman Compose  
✅ Docker / Podman  
✅ Google Cloud Run  
☹️ Apple Silicon - [more info](/docs/model-service/deploying-models#apple-silicon)  


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

<details markdown><summary><h4>Property Inference for SMILES</h4></summary>
<div markdown>

[:carbon-icn-github: openad-service-prop](https://github.com/acceleratedscience/openad-service-prop){ .md-button }
[Instructions](/docs/model-service/deploying-models/#deployment-via-container){ .md-button .md-button--tertiary }  

_No description available._


Support for:  
☹️ Docker / Podman Compose  
✅ Docker / Podman  
☹️ Google Cloud Run  
☹️ Apple Silicon - [more info](/docs/model-service/deploying-models#apple-silicon)  


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

<details markdown><summary><h4>MOLER Inference for SMILES</h4></summary>
<div markdown>

[:carbon-icn-github: openad-service-moler](https://github.com/acceleratedscience/openad-service-moler){ .md-button }
[Instructions](/docs/model-service/deploying-models/#deployment-via-container){ .md-button .md-button--tertiary }  

_No description available._


Support for:  
☹️ Docker / Podman Compose  
✅ Docker / Podman  
☹️ Google Cloud Run  
☹️ Apple Silicon - [more info](/docs/model-service/deploying-models#apple-silicon)  


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

<details markdown><summary><h4>MoLFormer Inference for SMILES</h4></summary>
<div markdown>

[:carbon-icn-github: openad-service-molf](https://github.com/acceleratedscience/openad-service-molf){ .md-button }
[Instructions](/docs/model-service/deploying-models/#deployment-via-container){ .md-button .md-button--tertiary }  

_No description available._


Support for:  
☹️ Docker / Podman Compose  
✅ Docker / Podman  
☹️ Google Cloud Run  
☹️ Apple Silicon - [more info](/docs/model-service/deploying-models#apple-silicon)  


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
