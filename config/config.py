import json

import logging
from logging.handlers import RotatingFileHandler

from pytest import fixture


class Config:
    log_path = "test_log.log"

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Config, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        logging.basicConfig(filename=self.log_path,
                            format='%(asctime)s %(message)s',
                            filemode='w')

        # Creating an object
        self.logger = logging.getLogger("Rotating log")
        # Setting the threshold of logger to DEBUG
        self.logger.setLevel(logging.INFO)

        handler = RotatingFileHandler(self.log_path, maxBytes=1000,
                                      backupCount=5)
        self.logger.addHandler(handler)

    def get_config(self):
        with open('config.json') as config_file:
            data = json.load(config_file)
        return data


