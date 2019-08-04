import configparser

class Configs:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('secrets.ini')
        self.default_config = self.config['DEFAULT']
        self.api_key = self.get_api_key()

    def get_api_key(self):
        return self.default_config['api_key']

