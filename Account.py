class Account:
    def __init__(self, accountNumber, name, age, initialBalance, accountType):
        self.__accountNumber = accountNumber
        self.__name = name
        self.__age = age
        self.__balance = initialBalance
        self.__accountType = accountType
        self.__status = "Active"

    def deposit(self, amount):
        if amount <= 0:
            return False
        self.__balance += amount
        return True

    def withdraw(self, amount):
        if amount <= 0 or amount > self.__balance:
            return False
        self.__balance -= amount
        return True

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
        self.__age = age
