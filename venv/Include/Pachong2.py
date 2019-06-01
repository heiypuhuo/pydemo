#!/usr/bin/python
import requests

get = requests.get("https://www.cnbeta.com/")
print(get.text)

