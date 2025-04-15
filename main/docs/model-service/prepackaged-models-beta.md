[Apple Silicon]: #apple-silicon
[Cataloging a Containerized Model]: #cataloging-a-containerized-model
[available services]: /docs/model-service/available-models.md

# Prepackaged Models

!!! info
    **Apple users:** Some models won't run on Apple Silicon processors.  
    See the [Apple Silicon] section below for more information.

## Deployment Options

There's different ways to deploy a service.

<!-- no toc -->
1. [Deploy via container + compose.yml](#deploy-locally-via-container-composeyml)  
   _Deploy your model locally or in the cloud, using Docker or Podman compose_  
   **Recommended**{ .flag .green } (when available)  
2. [Deploy via container](#containerizing-a-model)  
   _Deploy your model locally or in the cloud, using Docker or Podman build_
3. [Deploy locally using a Python virtual environment](#deploy-locally-using-a-python-virtual-env)  
   _Install requirements and manage your own environment_
4. [Cloud deployment to Red Hat OpenShift](#deploying-to-red-hat-openshift)  
   _Leverage cloud computing power_
5. [Cloud deployment to SkyPilot on AWS](#deploying-to-skypilot-on-aws)  
   _Leverage cloud computing power_




<!------------------------------------------------------------>
## Deployment via Container + compose.yml **Recommended**{ .flag .green }

When available, containerizing a model using [Docker Compose](https://docs.docker.com/compose/) / [Podman Compose](https://docs.podman.io/en/latest/markdown/podman-compose.1.html) is the easiest (and our recommended) way to deploy a model service.

### Support

To check if a service supports compose, check the service's details in our list [available services], or look in the service's GitHub repo if a `compose.yml` file is present.

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
    If you will be running multiple service, you may want to change the host port, eg. `8081:8080`

First build the container image:
```shell
(podman or docker) compose create
```

Next, start the container:
```shell
(podman or docker) compose start
```

!!! note
    If your device does not have a descrete GPU (as is the case for [Apple Silicon] devices), the `start` command will fail with the following error:

    ```shell
    Error response from daemon: could not select device driver "" with capabilities: [[gpu]]
    ```

    In this case, you can simply disable this part of the `compose.yml` instructions:
    ```shell
    # deploy:
    #   resources:
    #     reservations:
    #       devices:
    #         - capabilities: [gpu]
    ```

Once the service is running, continue to [Cataloging a Containerized Model].



<!------------------------------------------------------------>
## Deployment via Container

### Prerequisites

Make sure you have [Docker](https://www.docker.com) and the [Docker Buildx plugin](https://docs.docker.com/reference/cli/docker/buildx/) installed.

### Set up Container

Clone the model's GitHub repository:
```shell
git clone https://github.com/acceleratedscience/<repository_name>
```

Set the file cursor to the downloaded repository and run the build:

> **Note:** The `<model_name>` you can choose yourself.

```shell
cd <repository_name>
```
```shell
docker build -t <model_name> .
```

!!! note
    **Apple users:** If you're running on [Apple Silicon], you'l need to add `--platform linux/amd64` to the build command, to force the AMD64 architecture usinbg an emulator.

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
catalog model service from remote 'http://127.0.0.1:8080' as <service_name>
```
```
model service status
```

If all goes well, the status should say `Connected`
```
Service         Status       Endpoint                Host    API expires
--------------  -----------  ----------------------  ------  -------------
<service_name>  Connected    http://127.0.0.1:8080/  remote  No Info
```

As a reminder, to see all available model commands, run:
```shell
model ?
```

<!------------------------------------------------------------>
## Deploy Locally using a Python Virtual Environment

!!! info
    If you are using an [Apple Silicon] device, deploy using Docker instead. See [Apple Silicon] for more info.

<div class="padded-list" markdown>
- Create a virtual environment running Python `3.11`. We'll use [pyenv](/docs/installation/#upgrading-python).

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

- Install the model requirements as described in the model's repository (not to be confused with the OpenAD service wrapper). Models not listed below should deploy with Docker instead.
    
    | Model Name | GitHub |
    | ---------- | ------ |
    | **SMI-TED** | [github.com/IBM/materials](https://github.com/IBM/materials/) |
    | **BMFM-SM** | [github.com/BiomedSciAI/biomed-multi-view](https://github.com/BiomedSciAI/biomed-multi-view) |
    | **BMFM-PM** | [github.com/BiomedSciAI/biomed-multi-alignment](https://github.com/BiomedSciAI/biomed-multi-alignment) |
    | **REINVENT** | [github.com/MolecularAI/REINVENT4](https://github.com/MolecularAI/REINVENT4) |

- Install the OpenAD service utilities:
  
    ```shell
    pip install git+https://github.com/acceleratedscience/openad_service_utils.git
    ```

    !!! note
        Downloading of the models will be prompted by your first request and may take some time.  
        You can pre-load the models using [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html).

        ```shell
        mkdir -p ~/.openad_models/properties/molecules && aws s3 sync s3://ad-prod-biomed/molecules/mammal/ /tmp/.openad_models/properties/molecules/mammal --no-sign-request --exact-timestamps
        ```

- Clone the service repo:

    ```shell
    git clone https://github.com/acceleratedscience/openad-service-<service-name>
    ```

- Move the file cursor into the cloned service repo:

    ```shell
    cd openad-service-<service-name>
    ```

- Start the service:

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

    

    

- Open a new terminal session and launch OpenAD:

    ```shell
    openad
    ```

- Within the OpenAD shell, catalog the service you just started:

    ```shell
    catalog model service from remote 'http://127.0.0.1:8080' as <service-name>
    ```

- To see the available service commands, run:

    ```shell
    <service-name> ?
    ```

</div>


<!------------------------------------------------------------>
## Deploying to SkyPilot on AWS

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

### Spinning Up a Service

1.  Install any service by its `git@github` url, which you can find in the service's GitHub repo under the `<> Code` button.
    To spin up the Property inference service:

    ```shell
    catalog model service from 'git@github.com:acceleratedscience/property_inference_service.git' as prop
    ```

2.  Start the service – this can take up to 10 minutes

    ```shell
    model service up prop
    ```

3.  Check if the service is ready

    ```shell
    model service status
    ```

4.  Shut down the service

    ```shell
    model service down prop
    ```

5.  To see all available model commands, pull up the general help and look towards the bottom of the command list.

    ```shell
    ?
    ```


<!------------------------------------------------------------>
## Apple Silicon

Apple Silicon chips (aka M1, M2, M3 etc.) utilize the ARM64 instruction set architecture (ISA), which is incompatible with the standard x86-64 ISA our models are compiled for.

Some of the models have been prepped with alternative images that are able to run on Apple Silicon via emulator (with some impact on performance), however support is far from consistent.

Also, because Apple Silicon is a [SoC](https://en.wikipedia.org/wiki/System_on_a_chip) processor without discrete GPU, there is no support for GPU deployment. When using Docker or Podman compose, make sure to disable this part in the `compose.yml` file:

```
# deploy:
#   resources:
#     reservations:
#       devices:
#         - capabilities: [gpu]
```

If you will be using our models in a production environment, it's recommended to deploy the container to the cloud.