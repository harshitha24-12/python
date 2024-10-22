import json
with open('cruise_ship_schema.json', 'r') as file:
    data = json.load(file)
#print the crew value from Json file
crew_data = data.get('crew', {})
print(crew_data)
