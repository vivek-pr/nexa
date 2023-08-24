import os
import requests


def query_witai(text):
    access_token = os.environ.get('WIT_AI_TOKEN')
    if not access_token:
        raise ValueError("WIT_AI_TOKEN environment variable not set!")
    endpoint = "https://api.wit.ai/message"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
    }
    params = {
        'v': '20200805',  # API version, you might need to change this depending on the latest version.
        'q': text  # Your query to Wit.ai
    }

    response = requests.get(endpoint, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_intent_from_response(response_data):
    if response_data and 'intents' in response_data and len(response_data['intents']) > 0:
        return response_data['intents'][0]['name']  # get the name of the top intent
    return None

