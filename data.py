import requests

params = {
    "amount": 10,
    "category": 12,
    "type": "boolean",
}
response = requests.get(url="https://opentdb.com/api.php", params=params)
response.raise_for_status()
question_data = response.json()["results"]

