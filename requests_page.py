#!/usr/bin/python

import requests
import re

import urllib
import base64

username=""	#username <change the value>
password=""	#password <change the value>

url = ""%username
session = requests.Session()

response = session.get(url, auth=(username, password))
response = session.post(url,auth=(username, password),
		data = {"query":"a"})	# Change the query value and query variable

print tesponse.url
print response.txt
