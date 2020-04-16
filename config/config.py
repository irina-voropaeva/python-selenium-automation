import json

import logging

from pytest import fixture


class Config:

    def __init__(self):
        logging.basicConfig(filename="test_log.log",
                            format='%(asctime)s %(message)s',
                            filemode='w')

        # Creating an object
        self.logger = logging.getLogger()
        # Setting the threshold of logger to DEBUG
        self.logger.setLevel(logging.INFO)

    def get_config(self):
        with open('../config.json') as config_file:
            data = json.load(config_file)
        return data


