import json
import re
#import urllib.request
import urllib3
import webbrowser

from pytube import YouTube

api_key = "***PUT IN YOUR API KEY HERE***"

video_id = "C0PuCgQrxZU"
#url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={api_key}"
url = "https://www.youtube.com/watch?v=4wrKMI2Ehik&lc=UgwiiyzQradKKfW8FmZ4AaABAg"

http = urllib3.PoolManager()
r = http.request('GET', url)
print(r.data)
#json_url = urllib.request.urlopen(url)
#data = json.loads(json_url.read())
data = "Hola"
print(data)
#print(json_url)
