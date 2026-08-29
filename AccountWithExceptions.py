from AccountException import AccountException
from InvalidAmountException import InvalidAmountException
from InsufficientBalanceException import InsufficientBalanceException
from MinimumBalanceViolationException import MinimumBalanceViolationException
from InactiveAccountException import InactiveAccountException
from InvalidPinException import InvalidPinException

class Account:
    # ===== Constants =====
    MIN_BALANCE_SAVINGS = 500.0
    MIN_BALANCE_CURRENT = 1000.0
    MIN_AGE = 18
    MIN_PIN = 1000
    MAX_PIN = 9999

    # ===== Constructor =====
    def __init__(self, accountNumber, name, age, initialBalance, accountType):
        if age < self.MIN_AGE:
            raise ValueError(f"Age must be at least {self.MIN_AGE}")
            
        if accountType not in ["Savings", "Current"]:
            raise ValueError("Account type must be 'Savings' or 'Current'")
            
        min_balance = self.MIN_BALANCE_SAVINGS if accountType == "Savings" else self.MIN_BALANCE_CURRENT
        if initialBalance < min_balance:
            raise ValueError(f"Initial balance for {accountType} account cannot be below {min_balance}")
            
        self.__accountNumber = accountNumber
        self.__name = name
        self.__age = age
        self.__balance = initialBalance
        self.__accountType = accountType
        self.__status = "Active"
        self.__pin = None

    # ===== Business Methods =====
    def deposit(self, amount):
        self.validateActive()
        
        if amount <= 0:
            raise InvalidAmountException("Deposit amount must be positive")
            
        self.__balance += amount

    def withdraw(self, amount, pin):
        self.validateActive()
        
        if not self.hasPin():
            raise InvalidPinException("PIN not set")
            
        if not self.verifyPin(pin):
            raise InvalidPinException("Incorrect PIN")
            
        if amount <= 0:
            raise InvalidAmountException("Withdrawal amount must be positive")
            
        if amount > self.__balance:
            raise InsufficientBalanceException("Insufficient balance for withdrawal")
            
        min_balance = self.getMinimumBalance()
        if self.__balance - amount < min_balance:
            raise MinimumBalanceViolationException(f"Withdrawal would violate minimum balance requirement of {min_balance}")
            
        self.__balance -= amount

    # ===== Account Status Management =====
    def closeAccount(self):
        if self.__status == "Inactive":
            raise RuntimeError("Account is already closed")
        self.__status = "Inactive"

    def reopenAccount(self):
        if self.__status == "Active":
            raise RuntimeError("Account is already active")
        self.__status = "Active"

    # ===== PIN Management =====
    def setPin(self, pin):
        if not (isinstance(pin, int) and self.MIN_PIN <= pin <= self.MAX_PIN):
            raise ValueError("PIN must be a 4-digit number")
        self.__pin = pin

    def verifyPin(self, pin):
        return self.__pin == pin

    def hasPin(self):
        return self.__pin is not None

    # ===== Helper Methods =====
    def getMinimumBalance(self):
        return self.MIN_BALANCE_SAVINGS if self.__accountType == "Savings" else self.MIN_BALANCE_CURRENT

    def validateActive(self):
        if self.__status == "Inactive":
            raise InactiveAccountException("Account is inactive")

    # ===== Getters =====
    def getAccountNumber(self):
        return self.__accountNumber

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getBalance(self):
        return self.__balance

    def getAccountType(self):
        return self.__accountType

    def getStatus(self):
        return self.__status

    def setName(self, name):
        self.__name = name

    def setAge(self, age):
        if age < self.MIN_AGE:
            raise ValueError(f"Age must be at least {self.MIN_AGE}")
        self.__age = age
