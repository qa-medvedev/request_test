import requests

url = "https://webcom.academy/"
response = requests.get(url)
print(response.headers)
