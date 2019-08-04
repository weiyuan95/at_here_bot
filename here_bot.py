class HereBot:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = f'https://api.telegram.org/bot{self.api_key}/'