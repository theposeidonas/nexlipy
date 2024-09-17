# main.py

from modules import load_modules
import time
import config
from errors.error_handler import ModuleFailedException
import logging


def start_service():
    modules = load_modules()
    while True:
        for module in modules[:]:
            try:
                module.run()
            except ModuleFailedException as e:
                logging.error(f"{module.name} module failed and removing from list.")
                modules.remove(module)
            except Exception as e:
                logging.error(f"{module.name} module has failed: {e}")
            time.sleep(config.service.schedule.module_interval)
        if not modules:
            logging.error("All modules failed. Program termination.")
            break
        time.sleep(config.service.schedule.cycle_interval)

if __name__ == "__main__":
    start_service()