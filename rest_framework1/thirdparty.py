import requests


#This script perform serialization
URL = "http://127.0.0.1:8000/studentlist/"
# URL = "http://127.0.0.1:8000/studentinfo/1"
r = requests.get(url=URL)
data = r.json()
print("api data", data)
