import requests
import json
import os
import datetime

os.system("clear")
img = "https://images.plurk.com/32B15UXxymfSMwKGTObY5e.jpg"


# Search
img = requests.get(f'https://api.trace.moe/search?cutBorders&url={img}')
img = str(img.text)
img = json.loads(str(img))

# Get anime info
anilistQuery = '''
query ($id: Int) {
Media (id: $id, type: ANIME) {
    id
    title {
    romaji
    english
    native
    }
}
}
'''

anilistPOST = requests.post("https://graphql.anilist.co/", json={'query': anilistQuery, 'variables': {'id': img['result'][1]['anilist']}})
anilistPOST = str(anilistPOST.text)
anilistPOST = json.loads(str(anilistPOST))

print(img)
