from AccountWithExceptions import Account


class TestAccountExceptions:

    @staticmethod
    def run_tests():
        print("=" * 60)
        print("ACCOUNT TEST WITH EXCEPTIONS")
        print("=" * 60)

        accounts = []

        # Test 1: Valid Account Creation
        print("\n>>> Test 1: Valid Account Creation")
        try:
            account = Account(1001, "John Doe", 25, "Savings", 1000.0)
            accounts.append(account)
            print("SUCCESS:", account)
        except Exception as e:
            print("EXCEPTION:", e)

        # Test 2: Invalid Age
        print("\n>>> Test 2: Invalid Age (under 18)")
        try:
            account = Account(1002, "Young Person", 16, "Savings", 1000.0)
            accounts.append(account)
            print("SUCCESS:", account)
        except Exception as e:
            print("EXCEPTION:", e)

        # Test 3: Invalid Account Type
        print("\n>>> Test 3: Invalid Account Type")
        try:
            account = Account(1003, "Bob Smith", 30, "Invalid", 1000.0)
            accounts.append(account)
            print("SUCCESS:", account)
        except Exception as e:
            print("EXCEPTION:", e)

        # Test 4: Minimum Balance on Creation
        print("\n>>> Test 4: Minimum Balance on Creation")
        print("Creating Savings account with ₹300")
        try:
            account = Account(1004, "Test User", 25, "Savings", 300.0)
            accounts.append(account)
            print("SUCCESS:", account)
        except Exception as e:
            print("\nEXCEPTION:", e)

        # Test 5: Valid Deposit and Withdrawal
        print("\n>>> Test 5: Valid Deposit and Withdrawal")
        try:
            account = Account(1005, "Alice Brown", 30, "Current", 1000.0)
            accounts.append(account)

            print("Account:", account)

            account.set_pin("1234")
            print("Setting PIN 1234: SUCCESS")

            print("Depositing ₹500.0: SUCCESS")
            account.deposit(500.0)
            print("Balance after deposit:", f"₹{account.balance}")

            print("Withdrawing ₹200.0: SUCCESS")
            account.withdraw(200.0, "1234")
            print("Balance after withdrawal:", f"₹{account.balance}")

            print(account)

        except Exception as e:
            print("EXCEPTION:", e)

        # Test 6: Invalid Deposit
        print("\n>>> Test 6: Invalid Deposit (Negative Amount)")
        try:
            print("Attempting to deposit ₹-100.0")
            accounts[1].deposit(-100.0)
            print("SUCCESS")
        except Exception as e:
            print("EXCEPTION:", e)

        # Test 7: Insufficient Balance
        print("\n>>> Test 7: Insufficient Balance")
        try:
            account = Account(1006, "Charlie Green", 35, "Savings", 500.0)
            account.set_pin("1234")
            accounts.append(account)

            print("Account:", account)
            print("Attempting to withdraw ₹1000.0")

            account.withdraw(1000.0, "1234")
            print("SUCCESS")

        except Exception as e:
            print("EXCEPTION:", e)

        # Test 8: Minimum Balance Violation
        print("\n>>> Test 8: Minimum Balance Violation")
        try:
            account = Account(1007, "Diana Prince", 28, "Savings", 1000.0)
            account.set_pin("1234")
            accounts.append(account)

            print("Account:", account)
            print("Attempting to withdraw ₹600.0")

            account.withdraw(600.0, "1234")
            print("SUCCESS")

        except Exception as e:
            print("EXCEPTION:", e)

        # Test 9: Inactive Account Operations
        print("\n>>> Test 9: Inactive Account Operations")
        try:
            account = Account(1008, "Eve Wilson", 32, "Current", 2000.0)
            accounts.append(account)

            print("Account:", account)

            account.close_account()
            print("Closing account: SUCCESS")

            try:
                print("Attempting to deposit ₹100.0 on closed account")
                account.deposit(100.0)
                print("SUCCESS")

            except Exception as e:
                print("EXCEPTION:", e)

            account.reopen_account()
            print("Reopening account: SUCCESS")

            print("Depositing ₹100.0 after reopen: SUCCESS")
            account.deposit(100.0)

            print("Balance after deposit:", f"₹{account.balance}")

        except Exception as e:
            print("EXCEPTION:", e)

        # Test 10: PIN Verification
        print("\n>>> Test 10: PIN Verification")
        try:
            account = Account(1009, "Frank Miller", 40, "Savings", 1500.0)
            accounts.append(account)

            print("Account:", account)

            account.set_pin("1234")
            print("Setting PIN 1234: SUCCESS")

            print("Withdrawing ₹200.0 with correct PIN: SUCCESS")
            account.withdraw(200.0, "1234")
            print("Balance:", f"₹{account.balance}")

            try:
                print(
                    "Attempting to withdraw ₹100.0 "
                    "with incorrect PIN (9999)"
                )
                account.withdraw(100.0, "9999")
                print("SUCCESS")

            except Exception as e:
                print("EXCEPTION:", e)

            try:
                account2 = Account(
                    1010, "No PIN User", 30, "Current", 1000.0
                )

                print(
                    "Attempting to withdraw ₹100.0 "
                    "without PIN set"
                )
                account2.withdraw(100.0, None)
                print("SUCCESS")

            except Exception as e:
                print("EXCEPTION:", e)

        except Exception as e:
            print("EXCEPTION:", e)

        # Test 11: All Accounts Summary
        print("\n>>> Test 11: All Accounts Summary")
        print()

        for account in accounts:
            print(account)

        print("=" * 60)
        print("TEST COMPLETED!")
        print("=" * 60)


if __name__ == "__main__":
    TestAccountExceptions.run_tests()
