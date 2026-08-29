from AccountException import AccountException

class InvalidAmountException(AccountException):
    """
    Thrown when an invalid amount is provided (negative or zero).
    """
    def __init__(self, message):
        super().__init__(message)
