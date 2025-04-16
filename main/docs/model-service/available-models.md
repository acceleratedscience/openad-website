<!--

DO NOT EDIT
-----------
This file is auto-generated.
To update it, consult instructions:
https://github.com/acceleratedscience/openad-website/tree/generator

-->

# Publicly Available Models

<details markdown><summary><h3>SMI-TED &nbsp;/&nbsp; Inference for SMILES</h3></summary>
<div markdown>

[:carbon-icn-github: openad-service-smi-ted](https://github.com/acceleratedscience/openad-service-smi-ted){ .md-button }
[compose.yml](https://github.com/acceleratedscience/openad-service-smi-ted/raw/main/compose.yaml){ .md-button .md-button--primary download='compose.yml' }
[Instructions](/docs/model-service/prepackaged-models/#deployment-via-container-composeyml){ .md-button .md-button--tertiary }  

This OpenAD service provides access to the **SMILES-based Transformer Encoder-Decoder** (SMILES-TED), which is an encoder-decoder model pre-trained on a curated dataset of 91 million SMILES samples sourced from PubChem, equivalent to 4 billion molecular tokens. SMI-TED supports various complex tasks, including quantum property prediction, with two main variants ( 289 M and 8 × 289 M ).

More information:  
[github.com/IBM/materials](https://github.com/IBM/materials)  
[huggingface.co/ibm/materials.smi-ted](https://huggingface.co/ibm/materials.smi-ted)  
[arxiv.org/abs/2407.20267](https://arxiv.org/abs/2407.20267)


Support for:  
✅ Docker / Podman Compose  
✅ Docker / Podman  
✅ Apple Silicon - [more info](/docs/model-service/prepackaged-models/#apple-silicon)  


Quick start with Docker Compose:
```
curl -O https://github.com/acceleratedscience/openad-service-smi-ted/raw/main/compose.yaml
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

<details markdown><summary><h3>BMFM-SM &nbsp;/&nbsp; Inference for SMILES</h3></summary>
<div markdown>

[:carbon-icn-github: openad-service-bmfm-sm](https://github.com/acceleratedscience/openad-service-bmfm-sm){ .md-button }
[compose.yml](https://github.com/acceleratedscience/openad-service-bmfm-sm/raw/main/compose.yaml){ .md-button .md-button--primary download='compose.yml' }
[Instructions](/docs/model-service/prepackaged-models/#deployment-via-container-composeyml){ .md-button .md-button--tertiary }  

This OpenAD service provides access to the **Biomedmultiview** foundation model with checkpoints for the following properties:

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
✅ Apple Silicon - [more info](/docs/model-service/prepackaged-models/#apple-silicon)  


Quick start with Docker Compose:
```
curl -O https://github.com/acceleratedscience/openad-service-bmfm-sm/raw/main/compose.yaml
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

<details markdown><summary><h3>BMFM-PM &nbsp;/&nbsp; Inference for Proteins using MAMMAL</h3></summary>
<div markdown>

[:carbon-icn-github: openad-service-bmfm-pm](https://github.com/acceleratedscience/openad-service-bmfm-pm){ .md-button }
[compose.yml](https://github.com/acceleratedscience/openad-service-bmfm-pm/raw/main/compose.yaml){ .md-button .md-button--primary download='compose.yml' }
[Instructions](/docs/model-service/prepackaged-models/#deployment-via-container-composeyml){ .md-button .md-button--tertiary }  

This OpenAD service provides access to the **Biomedmultialignment** foundation model with checkpoints for the following properties:

| Sol | DTI |
| --- | --- |

More information:  
[github.com/BiomedSciAI/biomed-multi-alignment](https://github.com/BiomedSciAI/biomed-multi-alignment)


Support for:  
✅ Docker / Podman Compose  
✅ Docker / Podman  
❌ Apple Silicon - [more info](/docs/model-service/prepackaged-models/#apple-silicon)  


Quick start with Docker Compose:
```
curl -O https://github.com/acceleratedscience/openad-service-bmfm-pm/raw/main/compose.yaml
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

<details markdown><summary><h3>REINVENT &nbsp;/&nbsp; Inference for SMILES</h3></summary>
<div markdown>

[:carbon-icn-github: openad-service-reinvent4](https://github.com/acceleratedscience/openad-service-reinvent4){ .md-button }
[compose.yml](https://github.com/acceleratedscience/openad-service-reinvent4/raw/main/compose.yaml){ .md-button .md-button--primary download='compose.yml' }
[Instructions](/docs/model-service/prepackaged-models/#deployment-via-container-composeyml){ .md-button .md-button--tertiary }  

This OpenAD service provides access to the **REINVENT 4** molecular design tool, which is used for de novo design, scaffold hopping, R-group replacement, linker design, molecule optimization, and other small molecule design tasks. REINVENT uses a Reinforcement Learning (RL) algorithm to generate optimized molecules compliant with a user-defined property profile defined as a multi-component score. Transfer Learning (TL) can be used to create or pre-train a model that generates molecules closer to a set of input molecules. 

More information:  
[github.com/MolecularAI/REINVENT4](https://github.com/MolecularAI/REINVENT4)  
[link.springer.com/article/10.1186/s13321-024-00812-5](https://link.springer.com/article/10.1186/s13321-024-00812-5)


Support for:  
✅ Docker / Podman Compose  
✅ Docker / Podman  
❌ Apple Silicon - [more info](/docs/model-service/prepackaged-models/#apple-silicon)  


Quick start with Docker Compose:
```
curl -O https://github.com/acceleratedscience/openad-service-reinvent4/raw/main/compose.yaml
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

<details markdown><summary><h3>Generation Inference for SMILES</h3></summary>
<div markdown>

[:carbon-icn-github: openad-service-gen](https://github.com/acceleratedscience/openad-service-gen){ .md-button }
[Instructions](/docs/model-service/prepackaged-models/#deployment-via-container){ .md-button .md-button--tertiary }  

_No description available._


Support for:  
❌ Docker / Podman Compose  
✅ Docker / Podman  
❌ Apple Silicon - [more info](/docs/model-service/prepackaged-models/#apple-silicon)  


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

<details markdown><summary><h3>Property Inference for SMILES</h3></summary>
<div markdown>

[:carbon-icn-github: openad-service-prop](https://github.com/acceleratedscience/openad-service-prop){ .md-button }
[Instructions](/docs/model-service/prepackaged-models/#deployment-via-container){ .md-button .md-button--tertiary }  

_No description available._


Support for:  
❌ Docker / Podman Compose  
✅ Docker / Podman  
❌ Apple Silicon - [more info](/docs/model-service/prepackaged-models/#apple-silicon)  


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

<details markdown><summary><h3>MOLER Inference for SMILES</h3></summary>
<div markdown>

[:carbon-icn-github: openad-service-moler](https://github.com/acceleratedscience/openad-service-moler){ .md-button }
[Instructions](/docs/model-service/prepackaged-models/#deployment-via-container){ .md-button .md-button--tertiary }  

_No description available._


Support for:  
❌ Docker / Podman Compose  
✅ Docker / Podman  
❌ Apple Silicon - [more info](/docs/model-service/prepackaged-models/#apple-silicon)  


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

<details markdown><summary><h3>MoLFormer Inference for SMILES</h3></summary>
<div markdown>

[:carbon-icn-github: openad-service-molf](https://github.com/acceleratedscience/openad-service-molf){ .md-button }
[Instructions](/docs/model-service/prepackaged-models/#deployment-via-container){ .md-button .md-button--tertiary }  

_No description available._


Support for:  
❌ Docker / Podman Compose  
✅ Docker / Podman  
❌ Apple Silicon - [more info](/docs/model-service/prepackaged-models/#apple-silicon)  


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
