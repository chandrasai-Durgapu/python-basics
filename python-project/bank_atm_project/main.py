from atm import ATM
from bank_account import BankAccount

"""
main.py - Entry point for the Bank Simulator program.

This script initializes the ATM system, registers sample bank accounts,
prompts the user for login (account number and PIN), and provides options
to check balance, withdraw, deposit, or exit.

Files Required:
- bank_account.py: Contains the BankAccount class
- atm.py: Contains the ATM class"""

def bank_session():
    atm=ATM()
    acc1 = BankAccount(account_number=1234, pin=1111, balance=1000.0)
    acc2 = BankAccount(account_number=5678, pin=2222, balance=500.0)
    atm.register_account(acc1)
    atm.register_account(acc2)
    while True:
        try:
            acc_no = int(input("Enter your account number: "))
            # ✅ Check if account exists before asking for PIN
            if acc_no not in atm.registered_account:
                print("Error: Account not found. Please try again.\n")
                continue
            pin = int(input("Enter your PIN: "))
            
            user_account = atm.authenticate(acc_no, pin)
            atm.display_options(user_account)
            quit()
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Unexpected error: {e}")

#main execution of the project
if __name__ == "__main__":
    bank_session()
