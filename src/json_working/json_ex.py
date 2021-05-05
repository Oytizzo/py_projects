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

print(data)
print(type(data))
