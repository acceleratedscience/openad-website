import re
from mkdocs.config.config_options import Type
from mkdocs.config.base import Config
from mkdocs.plugins import BasePlugin

# The configuration options for the yml file
class PluginConfig(Config):
    base_url = Type(str, default='')

# The plugin class with event hooks
# https://www.mkdocs.org/dev-guide/plugins/#events
class ImageUrlPlugin(BasePlugin[PluginConfig]):
    def __init__(self):
        self.base_url = ""
        
    def on_config(self, config):
        self.base_url = config.get('site_url', '') or ''
        return config
        
    def on_page_markdown(self, markdown, page, config, files):
        # Find all image references and prepend base URL if not already an absolute URL
        pattern = r'!\[([^\]]*)\]\((?!http)([^)]+)\)'
        replacement = r'![\1](' + self.base_url + r'\2)'
        return re.sub(pattern, replacement, markdown)