# notebookgenerator
Generate Jupyter notebook for datascience using Azure Open AI.

# Inital setup
1. Clone the repo:
```
git clone https://github.com/pyx7b/notebookgenerator.git
```

2. Got to project directory:
```
cd notebookgnerator
```

3. Setup python virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```

4. Install python modules:
```
pip install -r requirements.txt
```


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

3. A Jupyter notebook will be created in the folder `notebook`.

4. Open the notebook.

5. Install the modules in the notebook.

6. Run the code and Good Luck! (Given its chatGPT, it may not work all the time)

## Testing
To test the code without incurring tokens.

1. Uncomment line 36 in `chat2ipynb.py` to read result from text file:
```
result = read_file("source.txt")
```

2. Comment off call to OpenAI service at line 39:
```
# result = get_chat_response(prompt)
```

3. Run the code without input prompt:
```
python3 chat2ipynb.py
```

4. Go to `notebook` folder to find your `.ipynb` file.

## Others
- Refer `notebook\example_us_population.ipynb` for a working output.
- `getfile.py` is a code reference to use `request` to download file from source.
- Error handling are not done really well.