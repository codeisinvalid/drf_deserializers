import requests
import json

URL = "http://127.0.0.1:8000/student-create"

data = {
    'name':'Rajan',
    'roll':200,
    'city':'India',
    'grade': "MBBS"
}

json_data = json.dumps(data)
# print(json_data)
r = requests.post(url = URL, data = json_data)
data = r.json()
print(data)
