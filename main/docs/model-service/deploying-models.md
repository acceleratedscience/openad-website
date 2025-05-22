[Apple Silicon]: #apple-silicon
[Cataloging a Containerized Model]: #cataloging-a-containerized-model
[available services]: /docs/model-service/available-models.md

# Deploying Models

!!! info
**Apple users:** Most models won't run on Apple Silicon (ARM64) processors, more information [below](#apple-silicon).  
 Check the list of [available services] to see which ones are compatible.

## Deployment Options

There's different ways to deploy a service.

<!-- no toc -->

1. [Deployment via container + compose.yaml](#deployment-via-container-composeyaml-recommended)  
   _Deploy your model locally or in the cloud, using Docker or Podman compose_  
   **Recommended**{ .flag .green } (when available)
2. [Deployment via container](#deployment-via-container)  
   _Deploy your model locally or in the cloud, using Docker or Podman build_
3. [Local deployment using a Python virtual environment](#local-deployment-using-a-python-virtual-environment)  
   _Install requirements and manage your own environment_
4. [Cloud deployment to Google Cloud Run](#cloud-deployment-to-google-cloud-run)  
   _Leverage cloud computing power, using a no-code deployment_  
   **Easy setup**{ .flag .yellow }
5. [Cloud deployment to Red Hat OpenShift](#cloud-deployment-to-red-hat-openshift)  
   _Leverage cloud computing power_
6. [Cloud deployment to SkyPilot on AWS](#cloud-deployment-to-skypilot-on-aws)  
   _Leverage cloud computing power_

<!------------------------------------------------------------>

## Deployment via Container + compose.yaml **Recommended**{ .flag .green }

When available, containerizing a model using [Docker Compose](https://docs.docker.com/compose/){ target='\_blank' } / [Podman Compose](https://docs.podman.io/en/latest/markdown/podman-compose.1.html){ target='\_blank' } is the easiest (and our recommended) way to deploy a model service.

### Support

To check if a service supports compose, check the service's details in our list [available services], or look in the service's GitHub repo if a `compose.yaml` file is present.

If you're running on an Apple computer, make sure to check the [Apple Silicon] section below.

### Preparation

Create the `.openad_models` folder in your home directory.

```shell
mkdir -p ~/.openad_models
```

### Build and Start

!!! note
**Chosing a port:** Before you start, consider the port you want to run the service on.  
 By default, `8080:8080` maps host port 8080 to container port 8080.  
 If you will be running multiple service, you may want to change the host port in the `compose.yaml`, eg. `8081:8080`

First build the container image:

```shell
[ docker/podman ] compose create
```

Next, start the container:

```shell
[ docker/podman ] compose start
```

!!! note
If your device does not have a descrete GPU (as is the case for [Apple Silicon] devices), the `start` command will fail with the following error:

    ```shell
    Error response from daemon: could not select device driver "" with capabilities: [[gpu]]
    ```

    In this case, you can simply disable this part of the `compose.yaml` instructions:

    ```shell
    # deploy:
    #   resources:
    #     reservations:
    #       devices:
    #         - capabilities: [gpu]
    ```

    Then run the `create` and `start` commands again.

Once the service is running, continue to [Cataloging a Containerized Model].

<!------------------------------------------------------------>

## Deployment via Container

### Prerequisites

Make sure you have [Docker](https://www.docker.com) and the [Docker Buildx plugin](https://docs.docker.com/reference/cli/docker/buildx/) installed.

Then create the `.openad_models` folder in your home directory.

```shell
mkdir -p ~/.openad_models
```

<!-- Repeat note about 'Downloading of the models will...' ?? -->
<!-- See https://github.com/acceleratedscience/openad-service-smi-ted/tree/main?tab=readme-ov-file#deployment-locally-via-compose -->

### Set up Container

Clone the model's GitHub repository:

```shell
git clone https://github.com/acceleratedscience/<repository_name>
```

Set the working directory to the downloaded repository and run the build:

> **Note:** The `<model_name>` you can choose yourself.

```shell
cd <repository_name>
```

```shell
docker build -t <model_name> .
```

!!! note
**Apple users:** If you're running on [Apple Silicon], you'l need to add `--platform linux/amd64` to the build command, to force the AMD64 architecture using an emulator.

    ```shell
    docker build --platform linux/amd64 -t <model_name> .
    ```

After the build is complete, run the container and make the server available on port 8080:

```shell
docker run -p 8080:8080 <model_name>
```

Once the service is running, continue to [Cataloging a Containerized Model].

<!------------------------------------------------------------>

## Cataloging a Containerized Model

Once the container is running, you can catalog the model in OpenAD:

First, lauch the OpenAD shell:

```shell
openad
```

Then catalog the service, and check the status.

```shell
catalog model service from remote 'http://127.0.0.1:8080' as <service-name>
```

```
model service status
```

If all goes well, the status should say `Connected`

```
Service         Status       Endpoint                Host    API expires
--------------  -----------  ----------------------  ------  -------------
<service-name>  Connected    http://127.0.0.1:8080/  remote  No Info
```

As a reminder, to see all available model commands, run:

```shell
model ?
```

<!------------------------------------------------------------>

## Local deployment using a Python virtual environment

!!! info
If you are using an [Apple Silicon] device, deploy using Docker instead. See [Apple Silicon] for more info.

<div class="padded-list" markdown>
- Create a virtual environment running Python `3.11`. We'll use [pyenv](/docs/installation.md#upgrading-python).

    > **Note:** Python `3.10.10+` or `3.11` are supported, Python `3.12` is not.

    ```shell
    pyenv shell 3.11
    ```
    ```shell
    python -m venv my-venv
    ```
    ```shell
    source my-venv/bin/activate
    ```

-   Install the model requirements as described in the model's repository (not to be confused with the OpenAD service wrapper). Models not listed below should deploy with Docker instead.

    | Model Name   | GitHub                                                                                                 |
    | ------------ | ------------------------------------------------------------------------------------------------------ |
    | **SMI-TED**  | [github.com/IBM/materials](https://github.com/IBM/materials/)                                          |
    | **BMFM-SM**  | [github.com/BiomedSciAI/biomed-multi-view](https://github.com/BiomedSciAI/biomed-multi-view)           |
    | **BMFM-PM**  | [github.com/BiomedSciAI/biomed-multi-alignment](https://github.com/BiomedSciAI/biomed-multi-alignment) |
    | **REINVENT** | [github.com/MolecularAI/REINVENT4](https://github.com/MolecularAI/REINVENT4)                           |

-   Install the OpenAD service utilities:

    ```shell
    pip install git+https://github.com/acceleratedscience/openad_service_utils.git
    ```

    !!! note
    Downloading of the models will be prompted by your first request and may take some time.  
     You can pre-load the models using [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html).

          ```shell
          mkdir -p ~/.openad_models/properties/molecules && aws s3 sync s3://ad-prod-biomed/molecules/mammal/ /tmp/.openad_models/properties/molecules/mammal --no-sign-request --exact-timestamps
          ```

-   Clone the service repo:

    ```shell
    git clone https://github.com/acceleratedscience/openad-service-<service-name>
    ```

-   Move the working directory into the cloned service repo:

    ```shell
    cd openad-service-<service-name>
    ```

-   Start the service:

    The start command differs per model:

    ```shell
    # SMI-TED / REINVENT
    python app.py
    ```

    ```shell
    # BMFM-SM
    python ./bmfm_sm_api/sm_implementation.py
    ```

    ```shell
    # BMFM-PM
    python ./implementation.py
    ```

-   Open a new terminal session and launch OpenAD:

    ```shell
    openad
    ```

-   Within the OpenAD shell, catalog the service you just started:

    ```shell
    catalog model service from remote 'http://127.0.0.1:8080' as <service-name>
    ```

-   To see the available service commands, run:

    ```shell
    <service-name> ?
    ```

</div>

<!------------------------------------------------------------>

## Cloud deployment to Google Cloud Run

Deploying a model to Google Cloud Run is the easiest way to deploy a model to the cloud, as Google Cloud can spin up the service directly from the GitHub repository using only the Dockerfile.

### Step 1: Preparation

-   Install [Google Cloud CLI](https://cloud.google.com/sdk/docs/install)
-   Go to [Available Models](available-models.md) to verify if the model you want to deploy supports Google Cloud
-   Fork the GitHub repo of the model you want to deploy.

### Step 2: Google Cloud Run

-   Go to [console.cloud.google.com/run](https://console.cloud.google.com/run)
-   Create a project
-   Start your free trial if you need to (credit card required)
-   Click the _"Create service"_ button in an empty project  
    (or click _"Deploy container"_ and select _"Service"_)
-   Select second option: _"Continuously deploy from a repository"_
    -   Click _"Setup with Cloud Build"_
    -   Connect GitHub & install Cloud Build for your fork
    -   Under _"Build Type"_ select _"Dockerfile"_ (keep default location)
-   Choose _"Require authentication"_
-   Click _"Container(s), Volumes, Networking, Security"_ at the bottom
    -   Under Resources, set Memory & CPU to 8GB & 4CPU or higher
    -   Under Requests, set the Request timeout to the maximum of 3600 sec
-   Click _"Create"_
-   Copy the service URL on top (we'll refer to it as `<service_url>`)  
    It should look something like this:

    ```
    https://openad-service-reinvent4-012345678999.us-central1.run.app
    ```

    > **Note:** Your service will have a green checkmark next to its name, but it won't be available until _"Building and deploying from repository"_ is done and also displays the green checkmark.

### Step 3: Terminal

<div class="padded-list" markdown>

-   Login to Google Cloud

    > **Note:** The `application-default` clause stores your credentials on disk and is required to auto-refresh your auth tokens.

    ```
    gcloud auth application-default login
    ```

-   If you haven't done so yet, you may have to set your project.

    > **Note:** To find your project's ID, go to the [Google Cloud Console](https://console.cloud.google.com/run) and click the button with your project's name (probably 'My FIrst Project') next to the Google Cloud logo.

    ```
    gcloud config set project <project_id>`
    ```

-   Fetch your auth token

    ```
    gcloud auth print-identity-token
    ```

-   Copy the token

</div>

### Step 4: OpenAD

<div class="padded-list" markdown>

-   Create auth group for Google Cloud

    > **Note:** You can call this group anything, we'll call it gcloud

    ```
    model auth add group gcloud with '<auth_token>'
    ```

-   Catalog the service

    ```
    catalog model service from remote '<service_url>' as <service_name>
    ```

-   Service will be listed as "Not ready" until the build is done  
     (~15-20 min depending on the model)

    ```
    model service status
    ```

</div>

<!------------------------------------------------------------>

## Cloud deployment to Red Hat OpenShift

If the service you're trying to deploy has a `/helm-chart` folder, it's been prepared for deployment on OpenShift.

> **Note:** The `<service-name>` and `<build-name>` you can choose yourself. We'll show an example for SMI-TED.

1. Install the helm chart

    ```shell
    helm install <service-name> <path-to-helm-chart-dir>
    ```

    ```shell
    # Example for SMI-TED
    helm install smi-ted ./helm-chart
    ```

2. Start a new build

    ```shell
    oc start-build <build-name>
    ```

    ```shell
    # Example for SMI-TED
    oc start-build smi-ted-build
    ```

3. Wait for the build to complete

    ```shell
    LATEST_BUILD=$(oc get builds | grep '<build-name>-' | awk '{print $1}' | sort -V | tail -n 1)
    ```

    ```shell
    # Example for SMI-TED
    LATEST_BUILD=$(oc get builds | grep 'smi-ted-build-' | awk '{print $1}' | sort -V | tail -n 1)
    ```

    ```shell
    oc wait --for=condition=Complete build/$LATEST_BUILD --timeout=15m
    ```

4. Run a request test

    ```shell
    curl "http://$(oc get route <service-name>-openad-model -o jsonpath='{.spec.host}')/health"
    ```

    ```shell
    # Example for SMI-TED
    curl "http://$(oc get route smi-ted-openad-model -o jsonpath='{.spec.host}')/health"
    ```

<!------------------------------------------------------------>

## Cloud deployment to SkyPilot on AWS

[AWS dashboard]: https://console.aws.amazon.com„
[IAM dashboard]: https://console.aws.amazon.com/iam
[Users]: https://console.aws.amazon.com/iam/home#/users

### Setting up SkyPilot

1.  <details><summary>AWS account</summary>

    <div markdown>

    -   Head to [aws.com](https://aws.com/)
    -   Click the _[Create an AWS Account]_ button in the top right corner
    -   Follow instructions, including setting up a root user

    </div>
    </details>

2.  <details><summary>AWS user with correct permissions</summary>

    <div markdown>

    Starting from your [AWS dashboard]:

    -   Search for _"IAM"_ in the search bar
    -   From your [IAM dashboard], click _"[Users]"_ in the lefthand sidebar
    -   Click the _[Create user]_ button in the top right hand corner
    -   Leave the _"Provide user access to the AWS Management Console"_ box unchecked
    -   Up next on the _"Set Permissions"_ screen, select the third option: _"Attach policies directly"_
    -   In the box below, click the _[Create policy]_ button
    -   Create a new policy with minimal permissions for Skypilot, following thye [Skypilot instructions](https://skypilot.readthedocs.io/en/latest/cloud-setup/cloud-permissions/aws.html)
    -   On the next screen, search for the policy you just created, which would be called `minimal-skypilot-policy` per the instructions
    -   Finish the process to attach the policy to your user

    </div>
    </details>

3.  <details><summary>AWS Access key</summary>

    <div markdown>

    Starting from the [IAM dashboard]:

    -   Click _"[Users]"_ in the lefthand sidebar
    -   Click on the user you created in the previous step
    -   Click _"Create access key"_ on the right side of the summary on top
    -   Select the first option, _"Command Line Interface (CLI)"_ as use case
    -   Finish the process to create the access key
    -   Store the secret access key in your password manager, as you will not be able to access it after creation

    </div>
    </details>

4.  <details><summary>AWS command line tool</summary>

    <div markdown>

    Starting from a terminal window:

    -   Install **awscli**

        ```shell
        python -m pip install awscli
        ```

        > **Note:** For more nuanced instructions, please refer to [pypi](https://pypi.org/project/awscli/#getting-started)

    -   Add the credentials for the AWS user you set up in step 3.

        ```shell
        aws configure
        ```

        -   Your user's access key can be found in your [IAM dashboard] > [Users], however the secret access key should have been stored in your password manager or elsewhere.
        -   The fields _"Default region name"_ and _"Default output format"_ can be left blank

    </div>
    </details>

5.  <details><summary>SkyPilot</summary>

    <div markdown>

    [SkyPilot](https://skypilot.readthedocs.io/en/latest/getting-started/installation.html) is a framework for running AI and batch workloads on any infrastructure. We're using AWS.

    Starting from a terminal window:

    -   If you are running OpenAD in a virtual environment, make sure your virtual environment is activated. If you followed the [default installation instructions](../installation.md), you should be able to run:

        ```shell
        source ~/ad-venv/bin/activate
        ```

    -   Install Skypilot for AWS

        ```shell
        pip install "skypilot[aws]"
        ```

    -   After installation, verify if you have cloud access

        ```shell
        sky check
        ```

    </div>
    </details>

<!------------------------------------------------------------>

## Apple Silicon

Apple Silicon chips (aka M1, M2, M3 etc.) utilize the ARM64 instruction set architecture (ISA), which is incompatible with the standard x86-64 ISA the models are compiled for.

Some are able to run on Apple Silicon via emulator (with some impact on performance), however support is not consistent.

Also, because Apple M processors are a [SoC](https://en.wikipedia.org/wiki/System_on_a_chip) without discrete GPU, there is no support for GPU deployment. When using Docker or Podman compose, make sure to disable this part in the `compose.yaml` file:

```
# deploy:
#   resources:
#     reservations:
#       devices:
#         - capabilities: [gpu]
```

If you will be using our models in a production environment, it's recommended to deploy the container to the cloud.
