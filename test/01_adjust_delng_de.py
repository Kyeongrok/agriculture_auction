import json

with open('map_auction.json') as f:
    jo = json.loads(f.read())

for item in jo:
    print(item)

