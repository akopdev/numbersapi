class WrongNumber(Exception):
    def __init__(self, message="Wrong number"):
        self.message = message
        super().__init__(self.message)

class OptionNotSupported(Exception):
    def __init__(self, message="Not supported option"):
        self.message = message
        super().__init__(self.message)

class ServiceResponseError(Exception):
    def __init__(self, message="numbersapi.com failed to response"):
        self.message = message
        super().__init__(self.message)