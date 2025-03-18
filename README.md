# OpenAD Website

This repo holds the public OpenAD website:

[openad.accelerate.science](https://openad.accelerate.science)

- Marketing page
- Documentation
- Blog / Tutorials

<br>

[![Create blog post](main/_assets_main/create-post.svg)](README-blog.md)

<br>

### Run local

> Note: you can publish blog posts directly from GitHub.

```shell
# Create & activate a virtual environment
python3 -m venv ~/ad-venv
source ~/ad-venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Launch development server
mkdocs serve

# Optional: launch on custom port
mkdocs serve -a localhost:9999
```

### Build local

```shell
mkdocs build
```

### Publish

Just push the `main` branch to GitHub, deployment is automated with GitHub actions.

<br>

## Developer Notes

### Stack

This is a heavily skinned version of the [Material theme](https://squidfunk.github.io/mkdocs-material/) for [MkDocs](https://www.mkdocs.org), which is a Python-based website generator that builds a website from markdown files.

We use the Material [blog plugin](https://squidfunk.github.io/mkdocs-material/plugins/blog/) for the blog functionality.

### Architecture

- All content lives inside markdown files in the [/main](main) directory.
- Navigation and all other site settings are controlled from [mkdocs.yml](mkdocs.yml)
- The homepage as well as certain components use HTML overrides, more on which below.

#### HTML overrides

Overrides let us customize the HTML components that are used to render the site, by mirroring the [Material templates](https://github.com/squidfunk/mkdocs-material/tree/master/src/templates) inside the `main/_overrides` folder.

For components, we can simply override [the original templates]((https://github.com/squidfunk/mkdocs-material/tree/master/src/templates)) with our own version by mirroring them inside the `main/_overrides` folder.

For full-page overrides (only used for the homepage), we can specify a custom template in the page metadata:

```markdown
---
title: Home Page
template: home.html
---
```

In most cases we opted for cold hard CSS overrides (see [main/_css](main/_css)) to maintain compatibility with MkDocs.

<br>

### Documentation

- [MkDocs documentation](https://www.mkdocs.org) - The base framework
- [Material documentation](https://squidfunk.github.io/mkdocs-material/) - Material is a theme for MkDocs with a bunch of additional functionality built in.

<br>

## Hosting & Domain Name

This website is hosted on GitHub Pages at [acceleratedscience.github.io/openad-website](https://acceleratedscience.github.io/openad-website). Our domain is regsitered with Google domains, with the [CNAME](CNAME) file connecting it.

Note that setting the domain name in the GitHub pages settings is not enough, as the build process will rebuild the `gh-pages` branch every time, wiping out the custom domain. [More info](https://github.com/mkdocs/mkdocs/issues/1257).