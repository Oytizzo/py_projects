''' JavaScript object Notation '''
import json

people_string = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "123-456-789",
            "emails": ["johnsmith@example.com", "john.smith@example.com"],
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "456-789-126",
            "emails": null,
            "has_license": true
        }
    ]
}
'''

data = json.loads(people_string)

for person in data['people']:
    del person['phone']

new_string = json.dumps(data, indent=2, sort_keys=True)

print(new_string)
print(type(new_string))
