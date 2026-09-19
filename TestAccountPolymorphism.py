from Account import Account
from SavingsAccount import SavingsAccount
from CurrentAccount import CurrentAccount
from AccountException import AccountException
from InactiveAccountException import InactiveAccountException
from InsufficientBalanceException import InsufficientBalanceException
from InvalidAmountException import InvalidAmountException
from InvalidPinException import InvalidPinException
from MinimumBalanceViolationException import MinimumBalanceViolationException


class TestAccountPolymorphism:

    @staticmethod
    def process_monthly_fee(account: Account, fee: float, pin: str):
        """
        Demonstrates polymorphism: this function accepts an abstract Account reference,
        yet at runtime it invokes the appropriate overridden withdraw() method
        for whichever concrete subclass is passed in.
        """
        print(f"Applying fee of ₹{fee} to {account.get_account_type()} Account #{account.get_account_number()}")
        account.withdraw(fee, pin)
        print(f"Fee applied! New balance: ₹{account.get_balance()}")

    @staticmethod
    def run_tests():
        print("=" * 60)
        print("ACTIVITY 8: POLYMORPHISM AND METHOD OVERRIDING TEST")
        print("=" * 60)

        # Test 1: Abstract Base Class Guard
        print("\n>>> Test 1: Abstract Class Instantiation Guard")
        try:
            print("Attempting to instantiate abstract Account class directly...")
            Account(1000, "Direct Account", 30, 1000.0)
            print("SUCCESS: (Unexpected)")
        except TypeError as e:
            print("CAUGHT TYPEERROR (Expected):", e)

        # Test 2: Creating Subclasses
        print("\n>>> Test 2: Subclass Instantiation")
        try:
            sa = SavingsAccount(1001, "Alice Smith", 25, 5000.0)
            sa.set_pin("1111")
            print("Savings Account created:")
            print(sa)

            ca = CurrentAccount(2001, "Bob Jones", 35, 2000.0)
            ca.set_pin("2222")
            print("Current Account created:")
            print(ca)
        except Exception as e:
            print("EXCEPTION:", e)

        # Test 3: Polymorphic Collection & Iteration
        print("\n>>> Test 3: Polymorphic Collection Processing")
        accounts = [sa, ca]
        print(f"Managing {len(accounts)} accounts polymorphically in a list:")
        for acc in accounts:
            print(
                f"- Account #{acc.get_account_number()} | "
                f"Type: {acc.get_account_type()} | "
                f"Min Balance: ₹{acc.get_minimum_balance()} | "
                f"Balance: ₹{acc.get_balance()}"
            )

        # Test 4: Polymorphic Deposits
        print("\n>>> Test 4: Polymorphic Deposit")
        deposit_amount = 1000.0
        for acc in accounts:
            try:
                acc.deposit(deposit_amount)
                print(f"Deposited ₹{deposit_amount} to Account #{acc.get_account_number()}: SUCCESS (Balance: ₹{acc.get_balance()})")
            except Exception as e:
                print("EXCEPTION:", e)

        # Test 5: Method Overriding - Withdrawal Behavior
        print("\n>>> Test 5: Method Overriding - Specialized Withdrawal")
        
        # 5a. Savings Account enforcing minimum balance of ₹500
        print("\n--- 5a. Savings Account Minimum Balance Enforcement ---")
        print(f"Current Savings Balance: ₹{sa.get_balance()} (Min required: ₹{sa.get_minimum_balance()})")
        
        # Valid withdrawal
        try:
            print("Withdrawing ₹2000.0 with PIN 1111...")
            sa.withdraw(2000.0, "1111")
            print(f"SUCCESS! Remaining balance: ₹{sa.get_balance()}")
        except Exception as e:
            print("EXCEPTION:", e)

        # Attempting withdrawal that violates minimum balance (₹500)
        try:
            print(f"Attempting to withdraw ₹3800.0 (would leave ₹{sa.get_balance() - 3800.0} < ₹500)...")
            sa.withdraw(3800.0, "1111")
            print("SUCCESS (Unexpected)")
        except MinimumBalanceViolationException as e:
            print("CAUGHT EXPECTED MinimumBalanceViolationException:")
            print(f"  -> {e}")
        except Exception as e:
            print("UNEXPECTED EXCEPTION:", e)

        # 5b. Current Account allowing overdraft up to ₹5000
        print("\n--- 5b. Current Account Overdraft Protection ---")
        print(f"Current Account Balance: ₹{ca.get_balance()} (Min: ₹{ca.get_minimum_balance()}, Overdraft Limit: ₹{ca.get_overdraft_limit()})")
        
        # Withdrawal exceeding balance but within overdraft limit
        try:
            print("Withdrawing ₹5000.0 with PIN 2222 (exceeds balance ₹3000, utilizes overdraft)...")
            ca.withdraw(5000.0, "2222")
            print(f"SUCCESS! Balance: ₹{ca.get_balance()}")
            print(f"Overdraft Used: ₹{ca.get_overdraft_used()}")
            print(f"Available Overdraft: ₹{ca.get_available_overdraft()}")
            print(f"Is Using Overdraft? {ca.is_using_overdraft()}")
        except Exception as e:
            print("EXCEPTION:", e)

        # Withdrawal exceeding overdraft limit
        try:
            print("\nAttempting to withdraw ₹4000.0 (exceeds remaining available overdraft)...")
            ca.withdraw(4000.0, "2222")
            print("SUCCESS (Unexpected)")
        except InsufficientBalanceException as e:
            print("CAUGHT EXPECTED InsufficientBalanceException:")
            print(f"  -> {e}")
        except Exception as e:
            print("UNEXPECTED EXCEPTION:", e)

        # Test 6: Overdraft Repayment and Auto-Clearing on Deposit
        print("\n>>> Test 6: Overdraft Handling & Repayment (CurrentAccount)")
        print(f"Current Overdraft Used: ₹{ca.get_overdraft_used()}")
        try:
            print("Repaying ₹1000.0 of overdraft...")
            ca.repay_overdraft(1000.0)
            print(f"SUCCESS! New Balance: ₹{ca.get_balance()}, Overdraft Used: ₹{ca.get_overdraft_used()}")
        except Exception as e:
            print("EXCEPTION:", e)

        try:
            print("Depositing ₹3000.0 to automatically clear remaining overdraft...")
            ca.deposit(3000.0)
            print(f"SUCCESS! New Balance: ₹{ca.get_balance()}, Overdraft Used: ₹{ca.get_overdraft_used()}")
            print(f"Is Using Overdraft? {ca.is_using_overdraft()}")
        except Exception as e:
            print("EXCEPTION:", e)

        # Test 7: Subclass Specific Features
        print("\n>>> Test 7: Subclass-Specific Features")
        print(f"Savings Account Interest Rate: {sa.get_interest_rate()}% p.a.")
        for years in [1, 3, 5]:
            interest = sa.calculate_interest(years)
            print(f"  Interest for {years} yr(s) on ₹{sa.get_balance()}: ₹{interest:.2f} (Total: ₹{sa.get_balance() + interest:.2f})")

        # Test 8: Polymorphic Dynamic Dispatch via Generic Function
        print("\n>>> Test 8: Runtime Polymorphism via Generic Function")
        for acc in accounts:
            pin = "1111" if isinstance(acc, SavingsAccount) else "2222"
            TestAccountPolymorphism.process_monthly_fee(acc, 50.0, pin)

        # Test 9: Exception Handling with Subclasses
        print("\n>>> Test 9: Exception Hierarchy Verification on Subclasses")
        
        # Test Invalid PIN
        try:
            print("Testing invalid PIN (9999) on SavingsAccount:")
            sa.withdraw(100.0, "9999")
        except InvalidPinException as e:
            print(f"CAUGHT EXPECTED InvalidPinException: {e}")

        # Test Negative Amount
        try:
            print("Testing negative withdrawal amount (-500.0) on CurrentAccount:")
            ca.withdraw(-500.0, "2222")
        except InvalidAmountException as e:
            print(f"CAUGHT EXPECTED InvalidAmountException: {e}")

        # Test Inactive Account
        try:
            print("Closing SavingsAccount and attempting deposit:")
            sa.close_account()
            sa.deposit(100.0)
        except InactiveAccountException as e:
            print(f"CAUGHT EXPECTED InactiveAccountException: {e}")
            sa.reopen_account()
            print("Reopened SavingsAccount successfully.")

        # Test 10: All Accounts Summary
        print("\n>>> Test 10: All Accounts Summary (Polymorphic __str__)")
        for acc in accounts:
            print(acc)

        print("=" * 60)
        print("POLYMORPHISM TEST COMPLETED SUCCESSFULLY!")
        print("=" * 60)


if __name__ == "__main__":
    TestAccountPolymorphism.run_tests()
