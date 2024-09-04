# modules

import os
import importlib
import config

def load_modules():
    env = config.service.environment
    modules = []
    module_path = os.path.dirname(__file__)
    for folder in os.listdir(module_path):
        folder_path = os.path.join(module_path, folder)
        if os.path.isdir(folder_path) and os.path.exists(os.path.join(folder_path, '__init__.py')):
            module = importlib.import_module(f'modules.{folder}')
            class_name = folder.capitalize()
            module_class = getattr(module, class_name)
            instance = module_class(env)
            modules.append(instance)
    return modules
