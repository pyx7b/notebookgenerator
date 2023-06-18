# notebookgenerator
Generate Jupyter notebook for datascience using Azure Open AI.

## Usage

1. Update the `.env` file with the your configurations:

```
AZURE_ENDPOINT_BASE = "https://xxxxx.openai.azure.com/"
AZURE_DEPLOYMENT_NAME = "xxxxx"
AZURE_ENDPOINT_API_KEY = "xxxxx"

```

2. Execute the script by providing it with a prompt `python3 chat2ipynb.py "<prompt>"`, e.g.:

```
python3 chat2ipynb.py "display a map of USA with population data"
```