# OpenAD Website
<!-- Author: moenen.erbuer@ibm.com -->

This repo holds the OpenAD website:

[openad.accelerate.science](https://openad.accelerate.science)

- Marketing page
- Documentation
- Blog / Tutorials

<br>

[![Create blog post](main/_assets/create-post.svg)](README-blog.md)

<br>

## Development

### Auto-generated content

Some of the documentation pages are automatically generated or updated by the `generate_docs()` script.  
Jump to the [/generator](generator#readme) directory for details.

### Development Server

Run the development server at [localhost:8000](http://localhost:8000)

> [!NOTE]
> **No need to clone this repo**  
> You can add or edit blog posts directly on GitHub and they will be published immediately.

```shell
# Create & activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Launch development server at :8000
mkdocs serve

# Optional: launch on custom port
mkdocs serve -a localhost:9999
```

### Build Local

```shell
mkdocs build
```

<br>

## Deployment

Deployment to GitHub pages happens automatically when changes are pushed to the `main` branch, via the [ci.yml build workflow](.github/workflows/ci.yml). Build progress can be followed under the [GitHub Actions tab](https://github.com/acceleratedscience/openad-website/actions).

<br>

## Hosting & Domain Name

<!-- Domain name is managed by IBM Webmaster Jerry Liao @jerryliao / jliao [at] ca.ibm.com  -->

This website is hosted on GitHub Pages at [acceleratedscience.github.io/openad-website](https://acceleratedscience.github.io/openad-website). Our domain is registered with Google domains and managed by the IBM webmaster, with a `CNAME` record pointing to `acceleratedscience.github.io` per [GitHub docs](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site#configuring-a-subdomain).

> [!WARNING]
> There is a local [CNAME](main/CNAME) file connecting the domain name to our GitHub pages website hardcoded in the `/main` folder. Usually this file is automatically added by GitHub Pages, but because our build process will rebuild the `gh-pages` branch every time, the GitHub-provided file gets erased with every update. Hardcoding the file circumvents that. [More info](https://github.com/mkdocs/mkdocs/issues/1257).

<br>

---

<br>

## Developer Notes

### Stack

This is a heavily skinned version of the [Material theme](https://squidfunk.github.io/mkdocs-material/) for [MkDocs](https://www.mkdocs.org), which is a Python-based website generator that builds a website from markdown files.

We use the Material [blog plugin](https://squidfunk.github.io/mkdocs-material/plugins/blog/) for the blog functionality.

<br>

### Architecture

- All content lives inside markdown files in the [/main](main) directory
- Navigation and all other site settings are controlled from [mkdocs.yml](mkdocs.yml)
- The homepage as well as certain components use HTML overrides, more on which below
- The build is written to [/site](site)
- A GitHub workflow called [ci.yml](.github/workflows/ci.yml) runs the build command and stores the build files into a branch called `gh-pages`, which is connected to our URL via GitHub Pages (see [Hosting & Domain Name](#hosting--domain-name) below)

<br>

### HTML overrides

Overrides let us customize the HTML components that are used to render the site, by mirroring the [Material templates](https://github.com/squidfunk/mkdocs-material/tree/master/src/templates) inside the `main/_overrides` folder.

For components, we can simply override [the original templates]((https://github.com/squidfunk/mkdocs-material/tree/master/src/templates)) with our own version by mirroring them inside the [/main/_overrides](main/_overrides) folder.

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