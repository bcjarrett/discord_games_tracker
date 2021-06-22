import json


class Config:

    def __init__(self):
        try:
            with open('secrets.json') as env:
                self.json_secrets = json.loads(env.read())
        except (IOError, json.decoder.JSONDecodeError):
            self.json_secrets = None

    def __getitem__(self, item):
        try:
            return self.json_secrets[item]
        except KeyError:
            raise KeyError(f'{item} is not in the secrets file')

    def __setitem__(self, key, value):
        self.json_secrets[key] = value


conf = Config()

# Define attached cogs here
conf['COGS'] = [
    'game_tracker',
    'music',
    'mgmt'
]

# Database
conf['DATABASE'] = 'db.db'

conf['VC_IDS'] = [
]

conf['STEAM_API_URL'] = 'https://store.steampowered.com/api/appdetails?language=en&lang=en&appids='
