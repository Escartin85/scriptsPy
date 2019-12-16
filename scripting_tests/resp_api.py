import requests

url = 'http://jsonplaceholder.typicode.com/photos'
response = requests.get(url)
print(response.json())

jsonPayload = {
    'albumId':1,
    'title':'test',
    'url':'nothing.com',
    'thumbnailUrl':'nothing.com'
}

response = requests.post(url,json=jsonPayload)
print(response.json())

url = 'http://jsonplaceholder.typicode.com/photos/100'

response = requests.put(url, json=jsonPayload)
print(response.json())

response = requests.delete(url)
print(response.json())

url = 'http://api.github.com/user'
response = requests.get(url)
print(response.json())

response = requests.get(url, auth=('djw-test', 'password1'))
print(response.json())

response = requests.get(url, headers={'Authorization':'Bearer 73d5e5c58625baa8ef988a75c8142454434ccae4'})
print(response.json())

my_json = response.json()
for key in my_json.keys():
    print(key)

print(my_json['plan'])
