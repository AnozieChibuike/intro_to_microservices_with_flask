import requests
import json

user_management_endpoint = "XXXXXXXXXXXXXXXXXXXXXXXXXXX"

def user_exists(user_id):
    body = {"action":"read","user_id": user_id}
    response = requests.post(f"{user_management_endpoint}/users", json=body)
    if response.status_code == 200:
        return True
    return False