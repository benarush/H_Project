import requests
import json

def get_token():
    username = "H_Project"
    password = "Aa12Aa12"
    post_data = {'username': username, 'password': password}
    r = requests.post('http://127.0.0.1:8000/messages/login/', data=post_data)
    response = json.loads(r.text)
    if "token" in response.keys():
        return response["token"]
    return response["non_field_errors"]

def test_token(token):
    response = requests.post('http://127.0.0.1:8000/messages/api/my_details/', headers={'Authorization':'Token ' + token})
    print(json.dumps(json.loads(response.text), indent=2))

def get_all_messages_send(token):
    response = requests.post('http://127.0.0.1:8000/messages/api/message_sent/', headers={'Authorization':'Token ' + token})
    print(response.text)
    print(json.dumps(json.loads(response.text), indent=2))

def get_all_messages_recieved(token):
    response = requests.post('http://127.0.0.1:8000/messages/api/message_receiver/', headers={'Authorization':'Token ' + token})
    print(response.text)
    print(json.dumps(json.loads(response.text), indent=2))

def create_message(token):
    data = {
    "subject": "Bla Bla555",
    "message": "yoo yooo5555",
    "receiver_username": "TestUser"
    }
    response = requests.post('http://127.0.0.1:8000/messages/api/create_message/',
                             headers={'Authorization': 'Token ' + token},
                             data=data)
    print(response.text)

def delete_message(token, message_id):
    response = requests.post('http://127.0.0.1:8000/messages/api/delete_message/' + message_id,
                             headers={'Authorization': 'Token ' + token})
    print(response.text)


token = get_token()
#test_token(token)
print(token)
#get_all_messages_recieved(token)
#create_message(token)
#get_all_messages_send(token)
#delete_message(token, str(7))
