# OpenAD Tell Me

The "Tell Me" function lets you inquire an LLM on how to do certain things with OpenAD.

!!! info

    -   **Supported LLMs** [Ollama]
    -   **Ollama** requires an 8GB GPU.

## Ollama Setup

1.  Install [Ollama] onto your platform.

2.  Download the appropriate models.

    ```shell
    ollama pull granite3.1-dense:8b-instruct-q4_1
    ```
    ```shell
    ollama pull all-minilm:l6-v2
    ```

3.  Start the server if not already started.

    ```shell
    ollama serve
    ```

That's it for local usage. If you want to run Ollama remotely, continue below.

### Ollama Remote Setup with SkyPilot

1.  Check out our configuration file to launch ollama on SkyPilot: [ollama_setup.yaml](https://github.com/acceleratedscience/open-ad-toolkit/blob/main/openad/ollama_setup.yaml)

    ```shell
    sky serve up ollama_setup.yaml
    ```

1.  Set up local environment variables

    -   For windows `setx OLLAMA_HOST=<sky-server-ip>:11434`
    -   For Linux and macOS `export OLLAMA_HOST=<sky-server-ip>:11434`
    -   To reset to local use `OLLAMA_HOST=0.0.0.0:11434`

### Run Ollama

> **Note:** If prompted for an API key and none was setup, just leave the input empty.

```shell
set llm ollama
```
```shell
tell me <enter prompt>
```

[Ollama]: https://ollama.com
