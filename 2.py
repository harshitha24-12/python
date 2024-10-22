import json

with open('sample-data.json', 'r') as file:
    data = json.load(file)

#printing firstName values
for item in data:
    print(item.get('firstName'))
