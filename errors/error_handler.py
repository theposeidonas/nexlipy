# errors/error_handler.py

import logging
import time
import functools
import config

class ModuleFailedException(Exception):
    """When a module reaches the maximum number of retries, it is thrown."""
    def __init__(self, module_name):
        self.module_name = module_name
        super().__init__(f"Module {module_name} has failed after maximum retries.")

# Logging yapılandırması
logging.basicConfig(
    filename='logs/service.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def error_handler(max_retries=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            retries = 0
            if max_retries is None:
                max_retries_config = config.service.service_behavior.retry_attempts
            else:
                max_retries_config = max_retries
            while retries <= max_retries_config:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    class_name = None
                    if args:
                        instance = args[0]
                        if hasattr(instance, '__class__'):
                            class_name = instance.__class__.__name__
                    if class_name:
                        module_name = class_name
                    else:
                        module_name = func.__name__
                    logging.error(f"{module_name} module error: {str(e)}", exc_info=True)
                    retries += 1
                    if retries > max_retries_config:
                        logging.error(f"Maximum number of attempts for {module_name} reached.")
                        raise ModuleFailedException(module_name)
                    else:
                        logging.info(f"{module_name} restarting... (Attempt: {retries}/{max_retries_config})")
                        time.sleep(config.service.service_behavior.retry_interval)
        return wrapper
    return decorator
