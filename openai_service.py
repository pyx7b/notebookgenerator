import os
import openai
from dotenv import dotenv_values

# Load the environment variables from the .env file
env_vars = dotenv_values('.env')

openai.api_type = "azure"
openai.api_base = env_vars['AZURE_ENDPOINT_BASE']
openai.api_version = "2023-03-15-preview"
openai.api_key = env_vars['AZURE_ENDPOINT_API_KEY']

def get_chat_response(prompt):
    # Send a completion call to generate an answer
    print('Sending completion call to OpenAI...')

    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a data scientist whose role is to write the code for Jupyter notebooks for data analysis. Provide source of example data if available. If available, download example data files using requests before referencing them."},
        {"role": "user", "content": prompt}
    ],
    engine=env_vars['AZURE_DEPLOYMENT_NAME'],
    temperature=0.7,
    max_tokens=800,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None
    )

    return(completion.choices[0].message.content)
