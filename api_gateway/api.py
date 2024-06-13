import requests
import json
from flask import jsonify

user_management_endpoint = "http://localhost:5001"
todo_management_endpoint = "http://localhost:5002"


def callApi(endpoint: str, route: str, body=None):
    response = requests.post(f"{endpoint}/{route}", json=body)
    return response.json(), response.status_code

def login(data):
    response, code = callApi(user_management_endpoint, "login", body=data)
    return jsonify(response), code

def user_exists(user_id):
    body = {"action":"read","id": user_id}
    response, code = callApi(user_management_endpoint, "users", body=body)
    print(response, code)
    if code == 200:
        return True
    return False

def userCRUD(data):
    if data.get('action') == 'delete':
        body = {"action": "read", "user_id": data.get('id')}
        response, code = callApi(todo_management_endpoint, "todo",body=body)
        for i in response['body']:
            body = {"action": "delete", "id": i['id']}
            callApi(todo_management_endpoint, "todo",body=body) # Should be optimized for bulk delete on todo management
    body, code = callApi(user_management_endpoint, "users", body=data)
    return jsonify(body), code

def todoCRUD(data):
    if data.get('action') == 'create':
        if not user_exists(data.get('user_id')):
            return jsonify(error='No user found with such id'), 404
    body, code = callApi(todo_management_endpoint, "todo", body=data)
    return jsonify(body), code