---
title: OpenAD
hide:
    - navigation
    - toc
---

<!--
This is an unlisted page with instructions for IBM consultants on how to:
- set up OpenAD
- wrap a ML model
- deploy it on a Kubernetes cluster
- make it available via OpenBridge
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
-   [Deployment on Kubernetes](#deployment-on-kubernetes)
-   [OpenBridge Proxy Service](#openbridge-proxy-service)
-   [Monitoring and Troubleshooting](#monitoring-and-troubleshooting)

---

## What is OpenAD

OpenAD is an open source toolkit for molecular research.  
It is meant to be integrated into larger workflows, rather than being standalone software.

<br>

#### Core Functionality

1.  A [**model service**](/docs/model-service/) that provides simplified & homogenized access to [various ML models](/docs/model-service/available-models/)
1.  A **molecule viewer** that lets you visualize and see details for:

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
-   Via **API**
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

Wrapping your own models is relevant for:

1. Companies who want to provide drastically simplified access to their models for their employees
2. Model authors who want to make their models more accessible to their audience
3. Opensource model consumers who want to have an easier way to work with their preferred models

&rarr; [Learn how to wrap a model](https://github.com/acceleratedscience/openad_service_utils)

## Deployment on Kubernetes

Once a model is wrapped, it can be hosted on your local machine (if hardware allows) or deployed on your cloud platform of choice.

> ??????????????  
> ??????????????  
> ??????????????

&rarr; [learn how to deploy a model](/docs/model-service/deploying-models/)

## OpenBridge Proxy Service

!!! Warning

    Still missing from docs @Daniel:

    -   Description paragraph in the GitHub README explaining what bridge does
    -   How to make your hosted models available under OpenBridge

[OpenBridge](https://github.com/acceleratedscience/bridge) is a proxy server that can handle user authentication and management. It is optional but the recommended approach if you're dealing with propriatary models and security is a concern.

Check the [OpenBridge documentation](https://github.com/acceleratedscience/bridge/blob/main/doc/deployment.md) for instructions on how to deploy OpenBridge and make your deployed models available under the proxy.

## Monitoring and Troubleshooting

> ??????????????  
> ??????????????  
> ??????????????
