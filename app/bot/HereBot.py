import os
import requests as r


base_url = f'https://api.telegram.org/bot{os.getenv("API_KEY")}'

def auth_check():
    get_bot_url = f'{base_url}/getMe'
    resp = r.post(get_bot_url)

    return resp.json()