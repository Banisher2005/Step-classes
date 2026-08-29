from AccountException import AccountException

class MinimumBalanceViolationException(AccountException):
    """
    Thrown when withdrawal would violate minimum balance requirement.
    """
    def __init__(self, message):
        super().__init__(message)
