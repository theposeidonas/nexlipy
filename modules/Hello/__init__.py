# modules/Hello

class Hello:
    """
    A class that represents a service task.
    When an instance is created, it can perform a specific operation.
    """

    def __init__(self, environment):
        self.environment = environment

    def run(self):
        if self.environment == "dev":
            self.dev()
        elif self.environment == "prod":
            self.prod()
        else:
            print(f"Unknown environment: {self.environment}")

    # Development-specific logic goes here
    @staticmethod
    def dev():
        print("Running Hello module in development mode.")


    # Production-specific logic goes here
    @staticmethod
    def prod():
        print("Running Hello module in production mode.")
