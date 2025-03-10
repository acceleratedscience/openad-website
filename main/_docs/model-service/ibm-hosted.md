<sub>&larr; [OpenAD](../../#openad) &nbsp;/&nbsp; [Models Service](../models-service.md) / Connecting to IBM-hosted Models</sub>

# Connecting to IBM-hosted Models

This service is for registered IBM partners only. Make sure you know who your group admin is.  
For more information about registering as an IBM partner, contact openad.toolkit@ibm.com.

<br>

## Step 1: Register at the OpenAD Portal

1.  **Log in to the OpenAD Portal**  
    Go to [open.accelerate.science](https://open.accelerate.science) and log in with your IBMid. Create one is necessary.  
    You'll see: _"Your account is pending to be added to a group"_

        <img src="assets/openad-portal-landing.png" width="623" />

1.  **Request Group Assignment**  
    Log out and contact your group administrator to add you to the appropriate group.

1.  **Verify Account Setup**  
    Log in again after receiving confirmation, your _group_ and _role_ should be displayed.

<br>

## Step 2: Generate an Access Token

1. Navigate to the **Access Token** tab
2. Click **Generate Token**
3. Click anywhere on the token to copy it, we'll need it later

    > [!WARNING]
    > Treat this token like a password. It grants full access to the system under your credentials.

<br>

## Step 3: Connect to a Model

If you haven't already, [install the OpenAD toolkit](../#quick-install).

### 3.1. Choose a model

To see what model subscriptions you have access to, check the **Your Subscriptions** tab in the OpenAD Portal.

<br>

### 3.2. Configure Authentication

```shell
# Replace YOUR_ACCESS_TOKEN with your actual access token
>> model auth add group default with 'YOUR_ACCESS_TOKEN'
```

<br>

### 3.3. Connect to a Model

In this example we'll connect to the molformer model.

```shell
>> catalog model service from remote 'https://open.accelerate.science/proxy' as molformer using (auth_group=default inference-service=molformer)
```

<br>

#### Understanding the Connection Command

| Command Component                         | Description                          |
| ----------------------------------------- | ------------------------------------ |
| `catalog model service from remote`       | Connects to a model via URL          |
| `'https://open.accelerate.science/proxy'` | The endpoint for model inference     |
| `'molformer'`                             | Your chosen name for this service    |
| `USING (auth_group=default ...)`          | References your authentication group |
| `USING (... Inference-Service=molformer)` | The model subscription name          |

<br>

## Step 4: Verify the Connection

```shell
>> model service status
```

Expected output:

```text
Service    Status     Endpoint                               Host    Token Expires
---------  ---------  -------------------------------------  ------  -----------------
molformer  Connected  https://open.accelerate.science/proxy  remote  Wed Sep 11, 2030
```

<br>

## Step 5: Explore Available Model Functions

```shell
>> molformer ?
```

You'll see available commands for the model:

```text
Commands starting with "molformer"
- molformer get molecule property molformer_classification for [<list of SMILES>] | <SMILES> USING (<parameter>=<value> <parameter>=<value>) (save_as '<filename.csv>')
- molformer get molecule property molformer_multitask_classification for [<list of SMILES>] | <SMILES> USING (<parameter>=<value> <parameter>=<value>) (save_as '<filename.csv>')
- molformer get molecule property molformer_regression for [<list of SMILES>] | <SMILES> USING (<parameter>=<value> <parameter>=<value>) (save_as '<filename.csv>')
```

<br>

## Step 6: Run Model Inference

```shell
>> molformer get molecule property molformer_classification for 'OC12COC3=NCC1C23'
```

Expected output:

```text
subject           property                  result
----------------  ------------------------  --------
OC12COC3=NCC1C23  molformer_classification  [1]
```

<br><br><br>

---

<br><br><br>

## Command Documentation

-   See all command related to the model service:

    ```shell
    >> model ?
    ```

-   To see detailed documentation for any individual command, append a `?` to the unique beginning of the command:

    ```shell
    >> model auth add group ?
    ```

## Troubleshooting

-   **Connection Issues**: Verify your token has not expired and the inference URL is correct.
-   **Authentication Errors**: Regenerate your token if necessary.
-   **Model Not Available**: Check your dashboard for available model subscriptions.
-   **Model misspelled**: Make sure there is no type in the `inference-service` parameter.
-   **Command Syntax Errors**: Use the `?` command to verify proper syntax.

## Best Practices

-   Store important results using the `save_as` parameter in commands (can also in a follow-up command`)
-   Use descriptive service names when connecting to models.
-   Organize multiple models and authentication groups logically.
-   Back up your access token securely.
