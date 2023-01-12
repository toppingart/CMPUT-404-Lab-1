# Lab 1 - virtualenv
# 4. Make a Python script that prints out the version of the requests library.
import requests
print(requests.__version__)

# Lab 1 - curl
# 5. Modify your Python script to GET the Google homepage
response = requests.get("https://google.com")
# print(response.text)
