from modules import load_modules
import time
import config

def start_service():
    modules = load_modules()
    while True:
        for module in modules:
            module.run()
            time.sleep(config.service.schedule.module_interval)
        time.sleep(config.service.schedule.cycle_interval)

if __name__ == "__main__":
    start_service()