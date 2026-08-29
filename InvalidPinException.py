from AccountException import AccountException

class InvalidPinException(AccountException):
    """
    Thrown when PIN is incorrect or not set.
    """
    def __init__(self, message):
        super().__init__(message)
