# Lab 1 - virtualenv
# 4. Make a Python script that prints out the version of the requests library.
import requests
print(requests.__version__)

# Lab 1 - curl
# 5. Modify your Python script to GET the Google homepage
response = requests.get("https://google.com")
# print(response.text)

# Lab 1 - curl
# 10. Modify your Python script so that it downloads itself...
rawURL= "https://raw.githubusercontent.com/toppingart/CMPUT-404-Lab-1/main/lab1.py"
response = requests.get(rawURL)
print(response.text)

