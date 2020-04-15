import json


class Config:

    def get_config(self):
        with open('../config.json') as config_file:
            data = json.load(config_file)
        return data
