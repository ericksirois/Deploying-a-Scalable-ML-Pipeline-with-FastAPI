import json
import requests

url = "http://127.0.0.1:8000"

# TODO: send a GET using the URL http://127.0.0.1:8000
r_get = requests.get(url)

# TODO: print the status code
print(f'GET request status code: {r_get.status_code}')
# TODO: print the welcome message
print(f'GET request message: {r_get.json()}')


data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States",
}

# TODO: send a POST using the data above
r_post = requests.post(f'{url}/data/', json=data)

# TODO: print the status code
print(f'POST request status code: {r_post.status_code}')
# TODO: print the result
print(f'POST request message: {r_post.json()}')
