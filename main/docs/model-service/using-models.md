# Using a Model Service

!!! note

    If your service was deployed to SkyPilot, jump to the instructions for SkyPilot below.

Once you have deployed a model service, you need to catalog it in OpenAD in order to use it.

### Demonstration Service

If you've already deployed your own model service, you can skip this step.  
Otherwise, launch the demo service to learn how work with OpenAD services.

You can try this out live in our [Colab tutorial](https://colab.research.google.com/drive/15iizKPQ9hJ-yexegI1MNpeoqinb6C5-V#scrollTo=8t0kAlk2Clw_){target=\_blank}.  
To learn how to deploy a model, go to [Deploying Models](deploying-models.md).

```shell
pip install git+https://github.com/acceleratedscience/openad_service_utils.git@0.3.1
```

```shell
openad
```

```shell
model service demo
```

```shell
|    Demo model service started at http://localhost:8034
|    PID: 0000
```

### Using the Service

<div class="padded-list" markdown>

1. Launch OpenAD

    ```shell
    openad
    ```

2. Catalog the service  
   _(Replace the service URL with the one of your own deployment)_

    ```shell
    catalog model service from remote 'http://localhost:8034' as demo_service
    ```

3. See the available commands for the service

    ```shell
    demo_service ?
    ```

4. Run inference

    ```shell
    demo_service get molecule property num_atoms for CC
    ```

    ```shell
    demo_service get molecule property num_atoms for NCCc1c[nH]c2ccc(O)cc12
    ```

    This will output:

    ```
    subject    property      result
    ---------  ----------  --------
    CC         num_atoms          2
    ```

    ```
    subject                 property      result
    ----------------------  ----------  --------
    NCCc1c[nH]c2ccc(O)cc12  num_atoms         13
    ```

</div>

### Service Status

You can easily check your services status by running:

```
model service status
```

This should display:

```
Service        Status     Endpoint                              Host
-------------  ---------  ------------------------------------  ------
demo_service   Connected  https://open.accelerate.science/demo  remote
```

---

## Using a Model Service on SkyPilot

Once you have [set up SkyPilot on AWS](deploying-models.md#cloud-deployment-to-skypilot-on-aws), using a model works slightly different.

<div class="padded-list" markdown>

1.  You can catalog any service directly from GitHub by its `git@github` url.  
    To catalog the SMI-TED service, for example:

    ```shell
    catalog model service from 'git@github.com:acceleratedscience/openad-service-smi-ted.git' as smi_ted
    ```

2.  Start the service

    > Note: this may take multiple minutes

    ```shell
    model service up smi_ted
    ```

3.  Check if the service is ready

    ```shell
    model service status
    ```

4.  See the available commands for the service

    ```shell
    smi_ted ?
    ```

5.  Shut down the service

    ```shell
    model service down smi_ted
    ```

</div>
