import json

import logging
from logging import handlers
from logging.handlers import RotatingFileHandler

from pytest import fixture


class Config:
    log_path = "test_log.log"
    loggers = {}

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Config, cls).__new__(cls)
        return cls.instance

    def log(self):
        if self.loggers.get("log"):
            return self.loggers.get("log")

        logger = logging.getLogger('log')
        logger.setLevel(logging.INFO)

        # Here we define our formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        log_handler = handlers.RotatingFileHandler(self.log_path)
        log_handler.setLevel(logging.INFO)
        # Here we set our log_handler's formatter
        log_handler.setFormatter(formatter)

        logger.addHandler(log_handler)
        self.loggers["log"] = logger
        return self.loggers["log"]

    def get_config(self):
        with open('config.json') as config_file:
            data = json.load(config_file)
        return data


