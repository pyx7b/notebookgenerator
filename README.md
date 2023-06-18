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


## Full Code Description

This Python code is designed to take a prompt as input, call an OpenAI service to get a response, and then split the response into code blocks and markdown cells. The resulting output is a Jupyter notebook file that can be used for further analysis or presentation.

The code starts by importing the necessary modules, including `sys`, `nbformat`, `re`, and a custom module called `openai_service`. It then defines a constant called `TEST_PROMPT` that is used for testing purposes. 

The `read_file` function is a helper function that reads a text file into a string. This function is not used in the current implementation, but it could be useful for test purposes.

The main part of the code starts by getting the input text string from the command line. If no input is provided, it uses the `TEST_PROMPT` constant. The `get_chat_response` function from the `openai_service` module is then called with the prompt as input, and the resulting string is stored in the `result` variable.

The `result_array` variable is created by splitting the `result` string into an array of strings using a regular expression that matches code blocks. The resulting array contains alternating markdown and code block strings.

A new Jupyter notebook is created using the `nbf.v4.new_notebook()` function. A header cell is added to the notebook that includes the original prompt and the resulting response. The `result_array` is then iterated over, and each markdown and code block is added to the notebook as a new cell using the `nbf.v4.new_markdown_cell()` and `nbf.v4.new_code_cell()` functions.

Finally, a unique file name is generated using the `uuid` module, and the resulting notebook is saved to a file with the `.ipynb` extension in a subdirectory called `notebook`.
