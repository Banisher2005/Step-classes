from AccountException import AccountException

class InsufficientBalanceException(AccountException):
    """
    Thrown when attempting to withdraw more than available balance.
    """
    def __init__(self, message):
        super().__init__(message)
