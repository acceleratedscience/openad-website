import os
import re
import pandas as pd
import requests
from .shared import (
    DO_NOT_EDIT,
    FLAG_ERROR,
    source_dir,
    read_template_file,
    write_output_file,
)

from openad.helpers.output import output_error, output_text, output_success

branch = "main"


def generate_model_docs(filename="model-service~available-models.md"):
    """
    Generate the available-models.md page for the documentation.

    - Start from the _templates/model-service~available-models.md template
    - Load the models.csv file from _templates/models.csv
    - Scrape the README.md files from the GitHub repositories listed in models.csv
    - Generate overview markdown for each model
    - Store result in _output/docs/model-service~available-models.md

    Note: The copy_docs script will interpret the ~ in the filename to know
    the path in the /docs directory where to copy the file to.
    """

    output_text(
        f"<h1>Generating <yellow>{filename}</yellow> from input/models.csv</h1>",
        pad_top=2,
    )

    # Read commands.md input content
    available_models_md = read_template_file(filename)

    # Insert DO NOT EDIT comment
    available_models_md = re.sub(
        r"{{DO_NOT_EDIT}}", DO_NOT_EDIT, available_models_md, flags=re.DOTALL
    )

    # Scrape README.md files from GitHub
    model_data = scrape_repos()
    if not model_data:
        return

    # Generate markdown
    markdown = generate_md(model_data)

    # Insert in template and save
    available_models_md = available_models_md + "\n\n" + markdown
    write_output_file("docs/" + filename, available_models_md)

    # for model in model_data:
    #     output_text(f"<yellow>Name:</yellow> {model['name']}", pad_top=1)
    #     output_text(f"<yellow>Title:</yellow> {model['title']}")
    #     output_text(f"<yellow>Repo name:</yellow> {model['repo_name']}")
    #     output_text(f"<yellow>Url:</yellow> {model['url']}")
    #     output_text(f"<yellow>Compose:</yellow> {model['compose']}")
    #     output_text(f"<yellow>Description:</yellow> {model['description']}"[:100] + "...")


def scrape_repos():
    """
    Loop through docs/source/models.csv and scrape information from GitHub.
    """

    csv = os.path.join(source_dir, "models.csv")
    df = pd.read_csv(csv)

    results = []
    for _, row in df.iterrows():
        repo_url = row["Repository"]
        # Raw URL:                    https://github.com/acceleratedscience/<repo_name>/raw/main/<filename>
        # Forwards to: https://raw.githubusercontent.com/acceleratedscience/<repo_name>/main/<filename>
        # The first URL can't be downloaded using curl, so we need to use the second one
        repo_url_raw = repo_url.replace("github.com", "raw.githubusercontent.com")
        name = row["Name"]
        try:
            # Scrape the README.md file
            readme_url = f"{repo_url}/raw/refs/heads/{branch}/README.md"
            repo_name = readme_url.replace(
                "https://github.com/acceleratedscience/", ""
            ).split("/", maxsplit=1)[0]
            output_text(f"<soft>Scraping README for {name}: {repo_name}</soft>")
            readme_response = requests.get(readme_url, timeout=10)
            readme_text = (
                readme_response.text if readme_response.status_code == 200 else ""
            )
            title = readme_text.split("\n")[0] if readme_text else "No title found"
            title = title.replace("<!-- omit from toc -->", "")
            title = re.sub(r"^# ", "", title)
            title = title.strip()
            description = parse_description(readme_text, repo_name)

            # Check support for Docker (Dockerfile)
            dockerfile_url = f"{repo_url_raw}/main/Dockerfile"
            dockerfile_exists = (
                requests.get(dockerfile_url, timeout=10).status_code == 200
            )

            # Check support for Docker compose (compose.yaml)
            compose_yml_url = f"{repo_url_raw}/main/compose.yaml"
            compose_exists = (
                requests.get(compose_yml_url, timeout=10).status_code == 200
            )

            # Check for Apple Silicon support (<!-- support:apple_silicon:true -->)
            apple_silicon_supported = (
                True  # Supported
                if "<!-- support:apple_silicon:true -->" in readme_text
                else (
                    False  # Not supported
                    if "<!-- support:apple_silicon:false -->" in readme_text
                    else None  # Unknown
                )
            )

            # Check for Google Cloud Run support (<!-- support:gcloud:true -->)
            gcloud_supported = (
                True  # Supported
                if "<!-- support:gcloud:true -->" in readme_text
                else (
                    False  # Not supported
                    if "<!-- support:gcloud:false -->" in readme_text
                    else None  # Unknown
                )
            )

            # Append results
            results.append(
                {
                    "name": name,
                    "title": title,
                    "repo_name": repo_name,
                    "url": repo_url,
                    "compose_yml_url": compose_yml_url,
                    "description": description,
                    "support:docker": dockerfile_exists,
                    "support:compose": compose_exists,
                    "support:apple-silicon": apple_silicon_supported,
                    "support:gcloud": gcloud_supported,
                }
            )
        except Exception as e:
            output_text(FLAG_ERROR)
            output_error(f"Aborted: error processing <yellow>{name}</yellow>: {e}")
            return None

    return results


def parse_description(readme_text, repo_name):
    description = readme_text.split("<!-- description -->")
    if len(description) > 1:
        description = description[1].split("<!-- /description -->")[0]
    else:
        output_error(f"{repo_name}<soft> - <!-- description --> tag missing</soft>")
        description = ""

    description = description.strip()
    if not description:
        description = "_No description available._"

    return description


def _scrape_repos():
    return [
        {
            "name": "gen",
            "title": "No title found",
            "repo_name": "generation_inference_service",
            "url": "https://github.com/acceleratedscience/generation_inference_service",
            "compose": False,
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam est risus, euismod vitae dapibus id, aliquam et velit. Nam rutrum gravida euismod. Donec posuere dui sodales massa blandit, et laoreet sapien varius. Fusce ut molestie leo. Nullam facilisis posuere quam, vel pellentesque dui. Donec elementum tincidunt quam vitae eleifend. Curabitur sed eleifend ligula.",
        },
        {
            "name": "prop",
            "title": "No title found",
            "repo_name": "property_inference_service",
            "url": "https://github.com/acceleratedscience/property_inference_service",
            "compose": False,
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam est risus, euismod vitae dapibus id, aliquam et velit. Nam rutrum gravida euismod. Donec posuere dui sodales massa blandit, et laoreet sapien varius. Fusce ut molestie leo. Nullam facilisis posuere quam, vel pellentesque dui. Donec elementum tincidunt quam vitae eleifend. Curabitur sed eleifend ligula.",
        },
        {
            "name": "moler",
            "title": "No title found",
            "repo_name": "moler_inference_service",
            "url": "https://github.com/acceleratedscience/moler_inference_service",
            "compose": False,
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam est risus, euismod vitae dapibus id, aliquam et velit. Nam rutrum gravida euismod. Donec posuere dui sodales massa blandit, et laoreet sapien varius. Fusce ut molestie leo. Nullam facilisis posuere quam, vel pellentesque dui. Donec elementum tincidunt quam vitae eleifend. Curabitur sed eleifend ligula.",
        },
        {
            "name": "molf",
            "title": "Molformer Inference Service",
            "repo_name": "molformer_inference_service",
            "url": "https://github.com/acceleratedscience/molformer_inference_service",
            "compose": False,
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam est risus, euismod vitae dapibus id, aliquam et velit. Nam rutrum gravida euismod. Donec posuere dui sodales massa blandit, et laoreet sapien varius. Fusce ut molestie leo. Nullam facilisis posuere quam, vel pellentesque dui. Donec elementum tincidunt quam vitae eleifend. Curabitur sed eleifend ligula.",
        },
        {
            "name": "smi-ted",
            "title": "SMI-TED Inference for SMILES",
            "repo_name": "openad-model-smited",
            "url": "https://github.com/acceleratedscience/openad-model-smited",
            "compose": True,
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam est risus, euismod vitae dapibus id, aliquam et velit. Nam rutrum gravida euismod. Donec posuere dui sodales massa blandit, et laoreet sapien varius. Fusce ut molestie leo. Nullam facilisis posuere quam, vel pellentesque dui. Donec elementum tincidunt quam vitae eleifend. Curabitur sed eleifend ligula.",
        },
        {
            "name": "bmfm-sm",
            "title": "BMFM Small Molecules Inference for Smiles",
            "repo_name": "bmfm-sm",
            "url": "https://github.com/acceleratedscience/bmfm-sm",
            "compose": True,
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam est risus, euismod vitae dapibus id, aliquam et velit. Nam rutrum gravida euismod. Donec posuere dui sodales massa blandit, et laoreet sapien varius. Fusce ut molestie leo. Nullam facilisis posuere quam, vel pellentesque dui. Donec elementum tincidunt quam vitae eleifend. Curabitur sed eleifend ligula.",
        },
        {
            "name": "bmfm-pm",
            "title": "BMFM MAMMAL Inference for Proteins",
            "repo_name": "bmfm_mammal_inference",
            "url": "https://github.com/acceleratedscience/bmfm_mammal_inference",
            "compose": True,
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam est risus, euismod vitae dapibus id, aliquam et velit. Nam rutrum gravida euismod. Donec posuere dui sodales massa blandit, et laoreet sapien varius. Fusce ut molestie leo. Nullam facilisis posuere quam, vel pellentesque dui. Donec elementum tincidunt quam vitae eleifend. Curabitur sed eleifend ligula.",
        },
    ]


def generate_md(model_data):
    """
    Generate the markdown code for the page, based off of the scraped model data.
    """

    output = []
    for model in model_data:
        # Parse
        # fmt:off
        title = model["title"]
        description = model["description"]
        repo_name = model["repo_name"]
        service_name = repo_name.replace("openad-service-", "").replace("-", "_")
        url = model["url"]
        compose_yml_url = model["compose_yml_url"]
        btn_github = f"[:carbon-icn-github: {repo_name}]({url}){{ .md-button }}"
        btn_compose = (
            f"[compose.yml]({compose_yml_url}){{ .md-button .md-button--primary download='compose.yml' }}"
            if model["support:compose"]
            else "--REMOVE-LINE--"
        )
        instructions_url_container = "/docs/model-service/deploying-models.md#deployment-via-container"
        instructions_url_compose = "/docs/model-service/deploying-models.md#deployment-via-container-composeyaml-recommended"
        instructions_url = instructions_url_compose if model["support:compose"] else instructions_url_container
        btn_instructions = f"[Instructions]({instructions_url}){{ .md-button .md-button--tertiary }}  "
        support_overview = (
            f"\n"
            "Support for:  \n"
            f"{'☹️' if not model['support:compose'] else '✅'} Docker / Podman Compose  \n"
            f"{'☹️' if not model['support:docker'] else '✅'} Docker / Podman  \n"
            f"{'☹️' if model['support:gcloud'] is False else '❓' if model['support:gcloud'] is None else '✅'} Google Cloud Run  \n"
            f"{'☹️' if model['support:apple-silicon'] is False else '❓' if model['support:apple-silicon'] is None else '✅'} Apple Silicon - [more info](/docs/model-service/deploying-models.md#apple-silicon)  \n"
            f"\n"
        )
        # fmt:on
        docker_compose_instructions = (
            "Quick start with Docker Compose:\n"
            "```\n"
            f"curl -O {compose_yml_url}\n"
            "```\n"
            "```\n"
            f"docker compose create\n"
            "```\n"
            "```\n"
            f"docker compose start\n"
            "```\n"
            "```\n"
            "openad\n"
            "```\n"
            "```\n"
            f"catalog model service from remote 'http://127.0.0.1:8080' as {service_name}\n"
            "```\n"
        )
        docker_build_instructions = (
            "Quick start with Docker:\n"
            "```\n"
            f"git clone {url}\n"
            "```\n"
            "```\n"
            f"cd {repo_name}\n"
            "```\n"
            "```\n"
            f"docker build -t {service_name} .\n"
            "```\n"
            "```\n"
            f"docker run -p 8080:8080 {service_name}\n"
            "```\n"
            "```\n"
            "openad\n"
            "```\n"
            "```\n"
            f"catalog model service from remote 'http://127.0.0.1:8080' as {service_name}\n"
            "```\n"
        )
        quickstart_instructions = (
            docker_compose_instructions
            if model["support:compose"]
            else (
                docker_build_instructions
                if model["support:docker"]
                else "--REMOVE-LINE--"
            )
        )

        # Compile
        html_block = [
            f"<details markdown><summary><h4>{title}</h4></summary>",
            "<div markdown>",
            "",
            # Buttons
            btn_github,
            btn_compose,
            btn_instructions,
            "",
            description,
            "",
            support_overview,
            quickstart_instructions,
            "</div>",
            "</details>",
            "",
        ]
        while "--REMOVE-LINE--" in html_block:
            html_block.remove("--REMOVE-LINE--")

        # Join
        output.append("\n".join(html_block))

    return "\n".join(output)


if __name__ == "__main__":
    generate_model_docs()
