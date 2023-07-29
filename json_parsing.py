import json

string_as_json_format = '{"name": "John", "age": 30, "city": "New York"}'
obj = json.loads(string_as_json_format)
print(obj["name"])

key = "name"
if key in obj:
    print(obj[key])
else:
    print(f"Key {key} not found")
