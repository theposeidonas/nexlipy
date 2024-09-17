# modules/Hello/__init__.py

from errors.error_handler import error_handler

class Hello:
    """
    A class that represents a service task.
    When an instance is created, it can perform a specific operation.
    """

    def __init__(self, environment):
        self.environment = environment
        self.name = "Hello"  # Required for error_handler

    @error_handler()
    def run(self):
        if self.environment == "dev":
            self.dev()
        elif self.environment == "prod":
            self.prod()
        else:
            raise Exception("Environment must be either dev or prod")

    @error_handler()
    def dev(self):
        print("Running Hello module in development mode.")
        if (1 == 1):
            pass
        else:
            raise Exception("1 is equal to 1")

    @error_handler()
    def prod(self):
        print("Running Hello module in production mode.")
        pass
