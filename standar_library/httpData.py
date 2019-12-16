import urllib.request
import json
import textwrap

url = "https://www.googleapis.com/books/v1/volumes?q=isbn:1101904224"
url2 = "http://www.abc.es/hemeroteca/neoteo"

with urllib.request.urlopen(url) as f:
	text = f.read()
	decodedtext = text.decode('utf-8')
	print(textwrap.fill(decodedtext, width=50))


print()

obj = json.loads(decodedtext)
print(obj['kind'])

# print(obj['items'][0]['searchInfo']['textSnippet'])

print("--- Getting code from website ---")

webUrl = urllib.request.urlopen(url2)

print("Request Code: " + str(webUrl.getcode()))
print("Data: ")
print(webUrl.read())
