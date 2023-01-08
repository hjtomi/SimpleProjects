import os
import requests
import time
import hmac
import hashlib

API_ENDPOINT = "wss://uat-stream.3ona.co/exchange/v1/user"

API_KEY = "ncFUy94LbYeBty1ptaLhKA"
API_SECRET_KEY = os.environ.get("API_SECRET_KEY")

public_auth_parameters = {
    "api_key": API_KEY,
    "id": 1,
    "method": "public/auth",
    "nonce": time.time_ns() // 1000000,
    "sig": "ds",
}

balance_parameters = {
    "id": 1,
    "method": "subscribe",
    "params": {
        "channels": ["user.balance"]
    }
}

param_str = ""

MAX_LEVEL = 3


def params_to_str(obj, level):
    if level >= MAX_LEVEL:
        return str(obj)

    return_str = ""
    for key in sorted(obj):
        return_str += key
        if obj[key] is None:
            return_str += 'null'
        elif isinstance(obj[key], list):
            for subObj in obj[key]:
                return_str += params_to_str(subObj, ++level)
        else:
            return_str += str(obj[key])
    return return_str


if "params" in public_auth_parameters:
    param_str = params_to_str(public_auth_parameters['params'], 0)

payload_str = public_auth_parameters['method'] + str(public_auth_parameters['id']) + public_auth_parameters['api_key'] + param_str + str(public_auth_parameters['nonce'])

public_auth_parameters['sig'] = hmac.new(
    bytes(str(API_SECRET_KEY), 'utf-8'),
    msg=bytes(payload_str, 'utf-8'),
    digestmod=hashlib.sha256
).hexdigest()

response = requests.get(API_ENDPOINT, params=public_auth_parameters)
response.raise_for_status()

print("auth", response.json())

response = requests.get(API_ENDPOINT, params=balance_parameters)
response.raise_for_status()

data = response.json()
print(data)
