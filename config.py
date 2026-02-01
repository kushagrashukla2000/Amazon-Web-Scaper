import json

CONFIG = {}

def load_config():
    global CONFIG
    with open("config.json") as config_file:
        CONFIG = json.load(config_file)