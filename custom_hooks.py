"""
Custom hooks

Currently not in use but may come in handy.
This lets us add customisation in the build process,
eg. we could embed certain variables that get replaced
in the markdown files.

https://www.mkdocs.org/user-guide/configuration/#hooks
https://www.mkdocs.org/dev-guide/plugins/#events
"""

import os
import re

snippets = {}


# MkDocs hook - https://www.mkdocs.org/dev-guide/plugins/#on_pre_page
def on_pre_page(page, config, files):
    global snippets
    snippets = _read_snippets("main/_snippets")


# MkDocs hook - https://www.mkdocs.org/dev-guide/plugins/#on_page_markdown
def on_page_markdown(markdown, page, config, files):
    # Style the excerpt
    markdown = _style_excerpt(markdown)

    # Replace snippets
    for [snippet_name, snippet_content] in snippets.items():
        pattern = f"<!-- INSERT:{snippet_name} -->"
        markdown = re.sub(pattern, snippet_content, markdown)
    return markdown


def _style_excerpt(markdown: str) -> str:
    """
    Wrap the excerpt into a div with a class so we can style it.
    """
    content_split = markdown.split("<!-- more -->")
    if len(content_split) == 2:
        title_and_excerpt = content_split[0].strip()
        body = content_split[1].strip()
        title = re.search(r"^(# .+)$", title_and_excerpt, re.MULTILINE)
        if title:
            title = title.group(0)
            excerpt = title_and_excerpt.split(title)[1]
            if excerpt:
                excerpt = f"<div class='excerpt' markdown>{excerpt}</div>"

            return "\n".join([title, excerpt, "<!-- more -->", body])
    return markdown


def _read_snippets(dir_path) -> dict[str, str]:
    """
    Loop through all snippet files and return an object
    with filename/snippet-content key/value pairs.

    returns:
        {
            SNIPPET_FOO: "foobar",
            SNIPPET_BAR: "barfoo"
            ...
        }
    """
    try:
        snippets = {}
        for filename in os.listdir(dir_path):
            filepath = os.path.join(dir_path, filename)
            if os.path.isfile(filepath):
                try:
                    with open(filepath, "r", encoding="utf-8") as file:
                        snippets[filename] = file.read().strip()
                except FileNotFoundError:
                    snippets[filename] = f"[ Missing snippet: '{filename}' not found ]"
                    print(f"Warning: Snippet file not found: {filepath}")
        return snippets

    except FileNotFoundError:
        print(f"Error: Directory '{dir_path}' not found.")
        return {}
    except PermissionError:
        print(f"Error: Permission denied for directory '{dir_path}'.")
        return {}
