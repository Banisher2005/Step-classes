from abc import ABC, abstractmethod


class Account(ABC):

    MIN_AGE = 18
    MIN_PIN = 1000
    MAX_PIN = 9999

    def __init__(self, account_number, name, age, initial_balance):

        if age < self.MIN_AGE:
            raise ValueError(
                f"Customer must be at least {self.MIN_AGE} years old. "
                f"Provided: {age}"
            )

        min_balance = self.get_minimum_balance()

        if initial_balance < min_balance:
            raise ValueError(
                f"{self.get_account_type()} account requires minimum "
                f"balance of ₹{min_balance}. Provided: ₹{initial_balance}"
            )

        self.account_number = account_number
        self.name = name
        self.age = age
        self.balance = initial_balance
        self.status = "Active"
        self.pin = None

    @abstractmethod
    def get_minimum_balance(self):
        pass

    @abstractmethod
    def get_account_type(self):
        pass

    # ===== Validation =====

    def validate_active(self):
        if self.status != "Active":
            raise Exception(
                "Account is inactive. Please reopen the account "
                "or contact support."
            )

    def validate_amount(self, amount):
        if amount <= 0:
            raise ValueError(
                f"Amount must be positive. Provided: ₹{amount}"
            )

    def validate_pin(self, pin):
        if self.pin is None:
            raise ValueError("PIN not set for this account")

        if pin is None or str(self.pin) != str(pin):
            raise ValueError("Incorrect PIN")

    # ===== PIN =====

    def set_pin(self, pin):
        if isinstance(pin, str) and pin.isdigit():
            pin = int(pin)

        if not isinstance(pin, int) or pin < self.MIN_PIN or pin > self.MAX_PIN:
            raise ValueError(
                f"PIN must be between {self.MIN_PIN} and {self.MAX_PIN}"
            )

        self.pin = pin

    def has_pin(self):
        return self.pin is not None

    # ===== Deposit =====

    def deposit(self, amount):
        self.validate_active()
        self.validate_amount(amount)

        self.balance += amount

    # ===== Withdrawal =====

    def withdraw(self, amount, pin):
        self.validate_active()
        self.validate_pin(pin)
        self.validate_amount(amount)

        if self.balance - amount < self.get_minimum_balance():
            raise Exception(
                f"Cannot withdraw. Minimum balance of "
                f"₹{self.get_minimum_balance()} required. "
                f"Available after withdrawal: ₹{self.balance - amount}"
            )

        self.balance -= amount

    # ===== Account Status =====

    def close_account(self):
        self.status = "Inactive"

    def reopen_account(self):
        self.status = "Active"

    # ===== Getters =====

    def get_balance(self):
        return self.balance

    def get_account_number(self):
        return self.account_number

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_status(self):
        return self.status

    # ===== String Representation =====

    def __str__(self):
        pin_status = "Yes" if self.pin is not None else "No"

        return (
            f"Account #{self.account_number} | "
            f"{self.name} ({self.age} yrs) | "
            f"{self.get_account_type()} | "
            f"₹{self.balance} | "
            f"{self.status} | "
            f"PIN: {pin_status}"
        )

    def __repr__(self):
        return self.__str__()
