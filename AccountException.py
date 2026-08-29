class AccountException(Exception):
    """
    Base exception for all account-related errors.
    """
    def __init__(self, message):
        super().__init__(message)
