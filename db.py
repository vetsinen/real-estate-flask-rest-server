import json

with open('db.json') as json_file:
    rooms = json.load(json_file)

print(len(rooms))
filtered = [x for x in rooms if x['district']=='Оболонь']
print(len(filtered))
print(filtered[:3])

dictlist = [{'first': 'James', 'last': 'Joule'}, {'first': 'James','last': 'Watt'},{'first': 'Christian','last': 'Doppler'}]
arr2 = [x for x in dictlist if x['first'] == 'James']
