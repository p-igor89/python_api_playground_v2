import requests

response = requests.get("https://playground.learnqa.ru/api/check_type", params={"name": "User"})
print(response.text)

response = requests.post("https://playground.learnqa.ru/api/check_type", data={"param1": "value1"})
print(response.text)