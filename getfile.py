import requests

# GitHub raw file URL
url = "https://raw.githubusercontent.com/plotly/datasets/master/2014_us_cities.csv"

# Make the GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Read the content of the file
    file_content = response.text
    
    # Print the file content
    print(file_content)
else:
    # Handle the case when the request fails
    print("Failed to retrieve the file. Status code:", response.status_code)