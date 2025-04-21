from jsonschema import validate

# Define the expected JSON schema
user_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "email": {"type": "string"},
        "address": {
            "type": "object",
            "properties": {
                "street": {"type": "string"},
                "city": {"type": "string"},
                "zipcode": {"type": "string"}
            },
            "required": ["street", "city", "zipcode"]
        }
    },
    "required": ["id", "name", "email", "address"]
}

# Function to validate response
def validate_user_schema(response_json):
    validate(instance=response_json, schema=user_schema)

print(validate_user_schema(user_schema))



