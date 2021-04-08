import json

person = {'name': 'rohan', 'age': 20, 'city': 'bangalore', 'titles': ['engineer', 'programmer'], 'HasChildren': False}
person_json = json.dumps(person)
print(person_json)

with open('person.json', 'w') as file:
    json.dump(person, file)


person = json.loads(person_json)
print(person)

