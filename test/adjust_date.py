import json
# map으로 만듬

r = {}
with open('all_2020_half.json') as f:
    jo = json.loads(f.read())

    for item in jo:
        if r.get(item['delngDe']) == None:
            r[item['delngDe']] = []
        r[item['delngDe']].append(item)


with open('map_auction.json', 'w+') as f:
    f.write(json.dumps(r))



