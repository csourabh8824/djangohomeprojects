import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    response = requests.get(url=URL, data=json_data)
    # we are sending this data (r) to view function i.e on server side
    print(response.json())


# get_data(2)

def create_data():
    data = {
        'name': 'virat',
        'roll': 103,
        'city': 'delhi'
    }
    json_data = json.dumps(data)
    response = requests.post(url=URL, data=json_data)
    print(response.json())


# create_data()

def update_data():
    data = {
        'id': 3,
        'name': 'dhoni',
        'city': 'ranchi'
    }
    json_data = json.dumps(data)
    response = requests.put(url=URL, data=json_data)
    print(response.json())


# update_data()


def delete_data():
    data = {
        'id': 3
    }
    json_data = json.dumps(data)
    response = requests.delete(url=URL, data=json_data)
    print(response.json())


delete_data()
