import requests
import lxml.html

url = "https://webcom.academy/"
response = requests.get(url)
tree = lxml.html.fromstring(response.text)
title = tree.xpath('//title')[0]
print(title.text_content())