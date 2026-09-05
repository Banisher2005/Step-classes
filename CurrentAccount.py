from Account import Account


class CurrentAccount(Account):

    MINIMUM_BALANCE = 1000.0
    ACCOUNT_TYPE = "Current"
    OVERDRAFT_LIMIT = 5000.0

    def __init__(self, account_number, name, age, initial_balance):
        super().__init__(
            account_number,
            name,
            age,
            initial_balance
        )

        self.overdraft_used = 0.0

    def get_minimum_balance(self):
        return self.MINIMUM_BALANCE

    def get_account_type(self):
        return self.ACCOUNT_TYPE

    # ===== Overdraft Withdrawal =====

    def withdraw(self, amount, pin):
        self.validate_active()
        self.validate_pin(pin)
        self.validate_amount(amount)

        available_balance = (
            max(0.0, self.get_balance() - self.get_minimum_balance())
            + self.get_available_overdraft()
        )

        if amount > available_balance:
            raise Exception(
                f"Insufficient funds. Available: ₹{available_balance}, "
                f"Requested: ₹{amount}"
            )

        new_balance = self.get_balance() - amount

        # If balance goes below minimum, overdraft is used
        if new_balance < self.get_minimum_balance():
            self.overdraft_used = self.get_minimum_balance() - new_balance
        else:
            self.overdraft_used = 0.0

        self.balance = new_balance

    def deposit(self, amount):
        super().deposit(amount)
        if self.balance >= self.get_minimum_balance():
            self.overdraft_used = 0.0
        else:
            self.overdraft_used = self.get_minimum_balance() - self.balance

    # ===== Current Account Methods =====

    def get_overdraft_limit(self):
        return self.OVERDRAFT_LIMIT

    def get_overdraft_used(self):
        return self.overdraft_used

    def get_available_overdraft(self):
        return self.OVERDRAFT_LIMIT - self.overdraft_used

    def is_using_overdraft(self):
        return self.overdraft_used > 0

    def repay_overdraft(self, amount):
        if amount <= 0:
            raise ValueError(
                "Repayment amount must be positive"
            )

        if amount > self.overdraft_used:
            raise ValueError(
                f"Amount exceeds overdraft used "
                f"(₹{self.overdraft_used})"
            )

        self.overdraft_used -= amount
        self.balance += amount
