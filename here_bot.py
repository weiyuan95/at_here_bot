from config import Configs
import requests as r

class HereBot:
    def __init__(self):
        configs = Configs()
        self.api_key = configs.api_key
        self.base_url = f'https://api.telegram.org/bot{self.api_key}'

    def auth_check(self):
        get_bot_url = f'{self.base_url}/getMe'
        resp = r.post(get_bot_url)

        return resp.json()