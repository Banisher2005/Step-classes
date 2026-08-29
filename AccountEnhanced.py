class Account:
    def __init__(self, accountNumber, name, age, initialBalance, accountType):
        self.__accountNumber = accountNumber
        self.__name = name
        
        # Age Validation
        self.__age = age if age >= 18 else 18
        
        # Account Type Validation
        if accountType not in ["Savings", "Current"]:
            self.__accountType = "Savings"
        else:
            self.__accountType = accountType
            
        # Minimum Balance Rules on Creation
        min_balance = 500.0 if self.__accountType == "Savings" else 1000.0
        self.__balance = initialBalance if initialBalance >= min_balance else min_balance
        
        # Status management
        self.__status = "Active"
        
        # PIN protection
        self.__pin = None

    def deposit(self, amount):
        if self.__status == "Inactive":
            return False
        if amount <= 0:
            return False
        self.__balance += amount
        return True

    def withdraw(self, amount, pin):
        if self.__status == "Inactive":
            return False
        
        # Assuming if pin is not set, we can't withdraw unless verifyPin handles it
        # The prompt says verifyPin returns true if matches.
        if not self.verifyPin(pin):
            return False
            
        if amount <= 0:
            return False
            
        min_balance = 500.0 if self.__accountType == "Savings" else 0.0
        if self.__balance - amount < min_balance:
            return False
            
        self.__balance -= amount
        return True

    def closeAccount(self):
        if self.__status == "Inactive":
            return False
        self.__status = "Inactive"
        return True

    def reopenAccount(self):
        if self.__status == "Active":
            return False
        self.__status = "Active"
        return True

    def setPin(self, pin):
        if isinstance(pin, int) and 1000 <= pin <= 9999:
            self.__pin = pin
            return True
        return False

    def verifyPin(self, pin):
        if self.__pin is None:
            return False
        return self.__pin == pin

    def hasPin(self):
        return self.__pin is not None

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
        self.__age = age if age >= 18 else 18
