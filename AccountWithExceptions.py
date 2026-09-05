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
    def __init__(self, accountNumber, name, age, initialBalance, accountType=None):
        if age < self.MIN_AGE:
            raise ValueError(f"Age must be at least {self.MIN_AGE}")
            
        # Support both (accountNumber, name, age, initialBalance, accountType)
        # and (accountNumber, name, age, accountType, initialBalance)
        if isinstance(initialBalance, str) and (isinstance(accountType, (int, float)) or accountType is None):
            accountType, initialBalance = initialBalance, (accountType if accountType is not None else 0.0)

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

    def close_account(self):
        self.closeAccount()

    def reopen_account(self):
        self.reopenAccount()

    # ===== PIN Management =====
    def setPin(self, pin):
        if isinstance(pin, int) and self.MIN_PIN <= pin <= self.MAX_PIN:
            self.__pin = str(pin)
        elif isinstance(pin, str) and pin.isdigit() and len(pin) == 4:
            self.__pin = pin
        else:
            raise ValueError("PIN must be a 4-digit number")

    def set_pin(self, pin):
        self.setPin(pin)

    def verifyPin(self, pin):
        if self.__pin is None or pin is None:
            return False
        return self.__pin == str(pin)

    def verify_pin(self, pin):
        return self.verifyPin(pin)

    def hasPin(self):
        return self.__pin is not None

    def has_pin(self):
        return self.hasPin()

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

    # ===== Properties =====
    @property
    def balance(self):
        return self.__balance

    @property
    def status(self):
        return self.__status

    @property
    def account_number(self):
        return self.__accountNumber

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def account_type(self):
        return self.__accountType

    # ===== String Representation =====
    def __str__(self):
        pin_status = "Yes" if self.hasPin() else "No"
        return f"Account #{self.__accountNumber} | {self.__name} ({self.__age} yrs) | {self.__accountType} | ₹{self.__balance} | {self.__status} | PIN: {pin_status}"

    def __repr__(self):
        return self.__str__()

