"""
Custom hooks

Currently not in use but may come in handy.
This lets us add customisation in the build process,
eg. we could embed certain variables that get replaced
in the markdown files.

https://www.mkdocs.org/user-guide/configuration/#hooks
https://www.mkdocs.org/dev-guide/plugins/#events
"""

import re


def on_page_markdown(markdown, page, config, files):
    pattern = r"foobar"
    replacement = r"F-O-O-B-A-R"
    return re.sub(pattern, replacement, markdown)
