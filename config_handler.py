import configparser

def load_config(file_path="config/config.ini"):
    config = configparser.ConfigParser()
    config.read(file_path)
    return config

def get_config_value(section, key):
    config = load_config()
    return config.get(section, key)
