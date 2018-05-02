class UnsupportedConf(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class IncorrectEndpoint(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class CouldNotCreateConfiguration(Exception):
    def __init__(self, destination):
        msg = "Could not create configuration in destination: {}"
        msg = msg.format(destination)
        super().__init__(msg)

