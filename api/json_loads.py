import json

import requests

json_string = '{"name": "Nitin", "age": 24, "city": "New York"}'
data = json.loads(json_string)  # ✅ Parses JSON from a string
print(type(json_string))
print(type(data))
print(data["city"])  # Output: New York

print(json_string)