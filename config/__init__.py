# config

import yaml
import os

class Service:
    """
    A class that loads the YAML configuration file and provides access to its values as object attributes.
    """
    def __init__(self):
        config_path = os.path.join(os.path.dirname(__file__), 'service.yaml')
        with open(config_path, 'r') as file:
            config_data = yaml.safe_load(file)
        for key, value in config_data.items():
            if isinstance(value, dict):
                setattr(self, key, ConfigObject(value))
            else:
                setattr(self, key, value)

class ConfigObject:
    """
    A helper class to convert dictionary entries into object attributes.
    """
    def __init__(self, dictionary):
        for key, value in dictionary.items():
            setattr(self, key, value)

service = Service()