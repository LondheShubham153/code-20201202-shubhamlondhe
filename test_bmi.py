import requests
import json


def test_get_header():

    url = "https://pybmi.herokuapp.com/bmi"
    payload={}
    headers = {}

    resp = requests.request("GET", url, headers=headers, data=payload)
    assert resp.status_code == 200

def test_post_header():

    url = "https://pybmi.herokuapp.com/bmi"
    payload="{\n        \"Gender\": \"Male\", \n        \"HeightCm\": 170, \n        \"WeightKg\": 75 \n}\n\n\n"
    headers = {
    'Content-Type': 'application/json'
    }

    resp = requests.request("POST", url, headers=headers, data=payload)
    assert resp.status_code == 200

