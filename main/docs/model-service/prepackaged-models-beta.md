[Apple Silicon]: #apple-silicon
[AWS Dashboard]: https://console.aws.amazon.com
[IAM Dashboard]: https://console.aws.amazon.com/iam
[Users]: https://console.aws.amazon.com/iam/home#/users

# Prepackaged Models

!!! warning
    Documentation is under development and may be inacurate.

!!! info
    **Apple users:** Most models won't run on Apple Silicon processors. See the [Apple Silicon] section below for more information.

## Options

There's different ways to set up a model service.

2. [Deployment via container + compose.yml](#deployment-via-container-composeyml) (recommended when available)  
   _Deploy your model locally or in the cloud, using Docker or Podman compose_
3. [Deployment via container](#containerizing-a-model) (recommended)  
   _Deploy your model locally or in the cloud, using Docker or Podman build_
4. [Cloud deployment to SkyPilot on AWS](#deploying-to-skypilot-on-aws) (advanced)  
   _Leverage cloud computing power_

<!-- 1. [Runninig a model locally](#running-a-model-locally)  
   _Quick setup, low overhead, slow performance_
2. [Containerize a model](#containerizing-a-model) (recommended)  
   _Deploy your model anywhere using Docker or Podman_
3. [Deploy to SkyPilot on AWS](#deploying-to-skypilot-on-aws) (advanced)  
   _Leverage cloud computing power_ -->




<!------------------------------------------------------------>

## Deployment via Container + compose.yml

Containerizing a model with [Docker Compose](https://docs.docker.com/compose/) or [Podman Compose](https://docs.podman.io/en/latest/markdown/podman-compose.1.html) is the easiest way, and our recomended solution to spin up a model service. However, support is still limited.

### Support

For a model to support containerization, it needs to have a `compose.yml` file in the root directory. We aim for all our models to come with containerization support, but this is a work in in progress.

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

## Deploying to SkyPilot on AWS

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

### Spinning Up a Model

1.  Install any service by its url (see [available models](#available-models) on top), for example the property inference service:

    ```shell
    catalog model service from 'git@github.com:acceleratedscience/property_inference_service.git' as prop
    ```

1.  Start the service – this can take up to 10 minutes

    ```shell
    model service up prop
    ```

1.  Check if the service is ready

    ```shell
    model service status
    ```

1.  Shut down the service

    ```shell
    model service down prop
    ```

1.  To see all available model commands, pull up the general help and look towards the bottom of the command list.

    ```shell
    ?
    ```

## Apple Silicon

Apple Silicon chips (aka M1, M2, M3 etc.) utilize the ARM64 instruction set architecture (ISA), which is incompatible with the standard x86-64 ISA our models are compiled for.

Some of the models have been prepped with alternative images that are able to run on Apple Silicon via emulator (with some impact on performance), however support is far from consistent.

Also, because Apple Silicon is a [SoC](https://en.wikipedia.org/wiki/System_on_a_chip) processor without discrete GPU, there is no support for GPU deployment. When using Docker or Podman compose, make sure to disable this part in the yml file.

If you will be using our models in a production environment, it's recommended to deploy the container to the cloud.