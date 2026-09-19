from Account import Account
from MinimumBalanceViolationException import MinimumBalanceViolationException


class SavingsAccount(Account):

    MINIMUM_BALANCE = 500.0
    ACCOUNT_TYPE = "Savings"
    INTEREST_RATE = 4.0

    def __init__(self, account_number, name, age, initial_balance):
        super().__init__(
            account_number,
            name,
            age,
            initial_balance
        )

    def get_minimum_balance(self):
        return self.MINIMUM_BALANCE

    def get_account_type(self):
        return self.ACCOUNT_TYPE

    def withdraw(self, amount, pin):
        """
        Overrides Account.withdraw() to enforce Savings minimum balance constraint (₹500).
        Demonstrates method overriding and runtime polymorphism.
        """
        self.validate_active()
        self.validate_pin(pin)
        self.validate_amount(amount)

        if self.balance - amount < self.MINIMUM_BALANCE:
            raise MinimumBalanceViolationException(
                f"Cannot withdraw. Minimum balance of "
                f"₹{self.MINIMUM_BALANCE} required. "
                f"Available after withdrawal: ₹{self.balance - amount}"
            )

        self.balance -= amount

    def calculate_interest(self, years):
        if years < 0:
            raise ValueError(
                "Years must be non-negative"
            )

        return (
            self.get_balance()
            * (self.INTEREST_RATE / 100)
            * years
        )

    def get_interest_rate(self):
        return self.INTEREST_RATE
