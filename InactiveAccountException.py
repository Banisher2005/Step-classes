from AccountException import AccountException

class InactiveAccountException(AccountException):
    """
    Thrown when operation is attempted on an inactive account.
    """
    def __init__(self, message):
        super().__init__(message)
