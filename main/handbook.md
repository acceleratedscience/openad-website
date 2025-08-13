---
title: OpenAD
hide:
    - navigation
    - toc
---

<!--
This is an unlisted page with instructions for IBM consultants on how to:
- Set up OpenAD
- Wrap a ML model
- Deploy it on cloud platform of choice
- Make it available via OpenBridge
- Monitor & troubleshoot
-->

# OpenAD Handbook <!-- omit in toc -->

!!! Info

    This guide is meant for IBM consultants. General documentation can be [found here](/docs).

<br>

#### Table of Contents <!-- omit in toc -->

-   [What is OpenAD](#what-is-openad)
    -   [Core Functionality](#core-functionality)
    -   [Accessing OpenAD](#accessing-openad)
-   [Wrapping Models for OpenAD](#wrapping-models-for-openad)
    -   [Available Models](#available-models)
    -   [Wrapping your Own Models](#wrapping-your-own-models)
-   [Deployment](#deployment)
-   [OpenBridge Proxy Service](#openbridge-proxy-service)

---

## What is OpenAD

OpenAD is an open source toolkit for molecular research.  
It is meant to be integrated into larger workflows, rather than being standalone software.

<br>

#### Core Functionality

1.  A [**model service**](/docs/model-service/) that provides simplified & homogenized access to [various ML models](/docs/model-service/available-models/)
1.  A [**molecule viewer**](/docs/gui#molecule-viewer) that lets you visualize and see details for:

    -   Sets of small molecules in 2D - [Tutorial](/blog/2025/03/19/visualizing-molecules-in-jupyter-notebook-from-a-list-or-dataframe/)  
        _Input: list of identifiers, SDF or CSV files_
    -   Individual small molecules in 2D + 3D - [Tutorial](/blog/2025/03/17/how-to-visualize-a-molecule-in-jupyter-notebook/)  
        _Input: identifier, MDL files_
    -   Proteins, Crystals and other macromolecules in 3D - [Tutorial](/blog/2025/03/24/how-to-visualize-proteins-in-jupyter-notebook/)  
        _Input: FASTA string, CIF or PDB files_

1.  A [**workspace**](/docs/base-concepts/#workspaces) where you can store and display molecular file formats like SDF, CSV, PDB, CIF as well as any other type of file.

<br>

#### Accessing OpenAD

OpenAD is a command line interface (CLI) that works in tandem with a graphical user interface (GUI).  
But it can be accessed in different ways:

-   Via [**terminal**](/docs/getting-started/), by launching the OpenAD interactive shell
    -   Ideal for learning and quick access
    -   GUI opens in a browser window when requested
-   Via [**Jupyter Notebook**](/docs/getting-started/), by using "magic commands"
    -   Ideal for iterative and experimental research
    -   GUI opens in an iframe when requested
-   Via [**Google Colab**](https://colab.research.google.com/drive/13r9LojtJTLZ8MEO1KNqJAKTieWmEUJQM), by using "magic commands"
    -   Ideal for no-setup access and popular amongst students
    -   GUI opens in an iframe when requested
-   Via [**API**](/docs/api)
    -   Ideal for batching large datasets
    -   GUI not available

## Wrapping Models for OpenAD

The landscape of available ML models for molecular research is vast and chaotic. We developed a "wrapper" template which can provide any Python model with a standardized RESTful API, which can then be consumed by OpenAD.

<br>

#### Available Models

We've wrapped a number of IBM Research's own open source models, which are ready to be deployed.

&rarr; [Available models](/docs/model-service/available-models/)

<br>

#### Wrapping your Own Models

By wrapping your own models, you can simplify access for yourself and others.

&rarr; [Learn how to wrap a model](https://github.com/acceleratedscience/openad_service_utils)

## Deployment

Once a model is wrapped, it can be hosted on your local machine (if hardware allows) or deployed on your cloud platform of choice.

&rarr; [Learn how to deploy a model](/docs/model-service/deploying-models/)  
&rarr; [Helm charts template for Kubernetes](https://github.com/acceleratedscience/openad-model-helm-template)

## OpenBridge Proxy Service

!!! info

    Using the OpenBridge proxy server is optional but recommended if you're dealing with propriatary models and security is a concern.

OpenBridge is a proxy server and user authentication and management service. What it does:

1. Proxy traffic from the Bridge URL to your hosted models while keeping their actual location securely hidden
2. Provide an interface for user and user group management, giving you fine grained controls for who gets to access which model

&rarr; [Deploy OpenBridge](https://github.com/acceleratedscience/bridge/blob/main/doc/deployment.md)  
&rarr; Publish models under OpenBridge - COMING SOON
