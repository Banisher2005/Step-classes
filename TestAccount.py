from Account import Account

class TestAccount:
    def test_account(self):
        print("==================================================")
        print(" GLOBAL DIGITAL BANK - ACCOUNT TEST ")
        print("==================================================")
        
        print(">>> 1. Creating Account ")
        acc1 = Account(1001, "John Doe", 25, 1000.0, "Savings")
        print("Account created! ")
        print(f"Account #{acc1.getAccountNumber()} | {acc1.getName()} ({acc1.getAge()} yrs) | {acc1.getAccountType()} | ₹{acc1.getBalance()} | {acc1.getStatus()} ")
        
        print(">>> 2. Deposit Money ")
        amount = 500.0
        if acc1.deposit(amount):
            print(f"Depositing ₹{amount}: SUCCESS ")
            print(f"New balance: ₹{acc1.getBalance()} ")
            
        amount = -100.0
        if not acc1.deposit(amount):
            print(f"Depositing ₹{amount}: FAILED (Invalid amount) ")
            
        print(">>> 3. Withdraw Money ")
        amount = 200.0
        if acc1.withdraw(amount):
            print(f"Withdrawing ₹{amount}: SUCCESS ")
            print(f"New balance: ₹{acc1.getBalance()} ")
            
        amount = 2000.0
        if not acc1.withdraw(amount):
            print(f"Withdrawing ₹{amount}: FAILED (Insufficient balance) ")
            print(f"Current balance: ₹{acc1.getBalance()} ")
            
        print(">>> 4. Creating Another Account ")
        acc2 = Account(1002, "Jane Smith", 30, 2000.0, "Current")
        print(f"Account #{acc2.getAccountNumber()} | {acc2.getName()} ({acc2.getAge()} yrs) | {acc2.getAccountType()} | ₹{acc2.getBalance()} | {acc2.getStatus()} ")
        
        print(">>> 5. All Accounts ")
        print(f"Account #{acc1.getAccountNumber()} | {acc1.getName()} ({acc1.getAge()} yrs) | {acc1.getAccountType()} | ₹{acc1.getBalance()} | {acc1.getStatus()} ")
        print(f"Account #{acc2.getAccountNumber()} | {acc2.getName()} ({acc2.getAge()} yrs) | {acc2.getAccountType()} | ₹{acc2.getBalance()} | {acc2.getStatus()} ")
        
        print("==================================================")
        print(" TEST COMPLETED! ")
        print("==================================================")

if __name__ == "__main__":
    tester = TestAccount()
    tester.test_account()
