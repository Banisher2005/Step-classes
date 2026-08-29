from AccountEnhanced import Account

class TestAccountEnhanced:
    def format_acc(self, acc):
        pin_status = "Yes" if acc.hasPin() else "No"
        return f"Account #{acc.getAccountNumber()} | {acc.getName()} ({acc.getAge()} yrs) | {acc.getAccountType()} | ₹{acc.getBalance()} | {acc.getStatus()} | PIN: {pin_status}"

    def run_tests(self):
        print("============================================================")
        print(" ENHANCED ACCOUNT TEST (BOOLEAN RETURNS) ")
        print("============================================================")
        
        print(">>> Test 1: Valid Account Creation ")
        acc1 = Account(1001, "John Doe", 25, 1000.0, "Savings")
        print(self.format_acc(acc1) + " ")
        
        print(">>> Test 2: Invalid Age (under 18) ")
        print("Creating account with age 16 ")
        acc2 = Account(1002, "Young Kid", 16, 500.0, "Savings")
        print(f"Age auto-corrected to: {acc2.getAge()} ")
        print(self.format_acc(acc2) + " ")
        
        print(">>> Test 3: Invalid Account Type ")
        print('Creating account with type "Invalid" ')
        acc3 = Account(1003, "Test User", 25, 500.0, "Invalid")
        print(f"Account type defaulted to: {acc3.getAccountType()} ")
        print(self.format_acc(acc3) + " ")
        
        print(">>> Test 4: Minimum Balance Enforcement on Creation ")
        print("Creating Savings account with ₹300 (below minimum) ")
        acc4 = Account(1004, "Bob Wilson", 25, 300.0, "Savings")
        print(f"Balance auto-corrected to minimum: ₹{acc4.getBalance()} ")
        print(self.format_acc(acc4) + " ")
        
        print(">>> Test 5: Withdrawal with Minimum Balance ")
        acc5 = Account(1005, "Alice Brown", 30, 1000.0, "Current")
        acc5.setPin(1111)
        print(f"Initial: {self.format_acc(acc5)} ")
        amount = 200.0
        if acc5.withdraw(amount, 1111):
            print(f"Withdrawing ₹{amount}: SUCCESS ")
            print(f"New balance: ₹{acc5.getBalance()} ")
        print(f"After withdrawal: {self.format_acc(acc5)} ")
        amount = 900.0
        if not acc5.withdraw(amount, 1111):
            print(f"Withdrawing ₹{amount} (would leave ₹-100): FAILED (Minimum balance violation) ")
            print(f"Current balance: ₹{acc5.getBalance()} ")
            
        print(">>> Test 6: Account Status Management ")
        acc6 = Account(1006, "Charlie Green", 35, 2000.0, "Savings")
        print(f"Initial: {self.format_acc(acc6)} ")
        if acc6.closeAccount():
            print("Closing account: SUCCESS ")
        print(f"After close: {self.format_acc(acc6)}")
        
        amount = 500.0
        if not acc6.deposit(amount):
            print(f"Depositing ₹{amount} to closed account: FAILED (Account inactive) ")
        if acc6.reopenAccount():
            print("Reopening account: SUCCESS ")
        print(f"After reopen: {self.format_acc(acc6)} ")
        
        print(">>> Test 7: PIN Protection ")
        acc7 = Account(1007, "Diana Prince", 28, 1500.0, "Savings")
        if acc7.setPin(1234):
            print("Setting PIN 1234: SUCCESS ")
        amount = 200.0
        if acc7.withdraw(amount, 1234):
            print(f"Withdrawing ₹{amount} with correct PIN (1234): SUCCESS ")
            print(f"New balance: ₹{acc7.getBalance()} ")
            
        amount = 100.0
        if not acc7.withdraw(amount, 9999):
            print(f"Withdrawing ₹{amount} with incorrect PIN (9999): FAILED (Incorrect PIN) ")
            
        if not acc1.hasPin() and not acc1.withdraw(amount, 1234):
            print(f"Withdrawing ₹{amount} with PIN not set: FAILED (PIN not set) ")
            
        print(">>> Test 8: All Accounts Summary ")
        print(self.format_acc(acc1) + " ")
        print(self.format_acc(acc2) + " ")
        print(self.format_acc(acc3) + " ")
        print(self.format_acc(acc4) + " ")
        print(self.format_acc(acc5) + " ")
        print(self.format_acc(acc6) + " ")
        print(self.format_acc(acc7) + " ")
        
        print("============================================================")
        print(" ENHANCED TEST COMPLETED! ")
        print("============================================================")

if __name__ == "__main__":
    tester = TestAccountEnhanced()
    tester.run_tests()
