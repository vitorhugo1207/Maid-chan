import requests 
import json


a = []
for x in range(82):
    r = requests.get('https://api.waifu.pics/nsfw/blowjob')
    r = str(r.text)
    r = json.loads(str(r))
    r = r['url']
    a.append(r)
    print(x)

r = ' '.join(map(str, a))
print(r)