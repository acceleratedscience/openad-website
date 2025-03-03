<!-- uv venv .venv -->

source .venv/bin/activate

<!-- deactivate -->

pip install -r requirements.txt

mkdocs serve
mkdocs build

# Development

##### Update requirements.txt with pip packages

uv pip freeze > requirements.txt
