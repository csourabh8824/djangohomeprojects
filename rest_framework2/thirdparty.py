import requests
import json
# This script perform deserialization
URL = "http://127.0.0.1:8000/studentcreate/"

python_dict_data = {
    'name': 'sourabh',
    'roll': 101,
    'city': 'Indore'
}

json_data = json.dumps(python_dict_data)

r = requests.post(url=URL, data=json_data)
data = r.json()
print(data)
