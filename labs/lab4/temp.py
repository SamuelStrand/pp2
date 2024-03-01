import json

with open(r'C:\Users\emilv\Documents\GitHub\pp2\labs\lab4\json\js.json', 'r') as file:
    data = json.load(file)

for item in data['imdata']:
    item['l1PhysIf']['attributes']['adminSt'] = 'down'

with open('output.json', 'w') as file:
    json.dump(data, file, indent=4)
