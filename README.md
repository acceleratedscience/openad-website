# OpenAD Blog

Work in progress. Currently this is just housing the new blog, but soon the docs and the marketing website will join under the same roof.

<br>

## Adding Blog Posts

To publish a new blog post, simply add a `markdown` file to the [`main/blog/posts`](openad-tutorials/tree/main/main/blog/posts) directory. You can do this directly from GitHub without downloading the repository.

Make sure to add a header to your markdown file:

```markdown
---
date: 2025-03-06
draft: true
links:
    - local/related-link.md
    - http://external-related-link.com
---
```

-   Any updates pushed to the `main` branch will immediately be deployed.
-   Any files that are edited or added directly on GitHub, will also trigger a fresh deployment.
-   Blog posts with `draft: true` in the header won't be included in the build, but can be previewed locally.
-   Deployment takes about 2-3 minutes, progress can be followed under the [Actions](/actions) tab.

<br>

## For Developers

### Stack

This is a heavily skinned version of the [Material theme](https://squidfunk.github.io/mkdocs-material/) for [MkDocs](https://www.mkdocs.org), which runs on Python. We use the Material [blog plugin](https://squidfunk.github.io/mkdocs-material/plugins/blog/) for the blog functionality.

### Run locally

```shell
# Create & activate a virtual environment
python3 -m venv ~/ad-venv
source ~/ad-venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Launch development server
mkdocs serve

# Launch at custom port
mkdocs serve -a localhost:9999
```

### Build locally

```shell
mkdocs build
```

### Notes

The [McDocs Material documentation](https://squidfunk.github.io/mkdocs-material/) is very thorough. One useful thing to know is that we can override templates with our own version, by mirroring the [Material templates](https://github.com/squidfunk/mkdocs-material/tree/master/src/templates) inside the `main/_overrides` folder, and then setting the custom template in the page metadata:

```markdown
---
title: Home Page
template: home.html
---
```

To keep this project as much compatible as possible with the official MkDocs Materials, we chose not to rely on custom templates and instead opted for cold hard CSS overriding. These overrides are organized by theme under `main/css`.

The only page that is using a custom template if the homepage.
