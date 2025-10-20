from bank_account import BankAccount
from database.database import setup_database,get_connection
def main():
    setup_database()

    print("Welcome to the SQLite Bank Simulator\n")

    while True:
        print("\n1. Create Account\n2. Login\n3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            acc = int(input("Enter new account number: "))
            pin = int(input("Set 4-digit PIN: "))
            initial = float(input("Enter initial deposit: "))
            try:
                BankAccount.create_account(acc, pin, initial)
                print("Account created successfully!")
            except:
                print("Account creation failed. Account number may already exist.")

        elif choice == '2':
            try:
                acc = int(input("Enter account number: "))
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute("SELECT 1 FROM accounts WHERE account_number=?", (acc,))
                result = cursor.fetchone()
                conn.close()
                if not result:
                    print("Error: Account not found. Please try again.\n")
                    continue  # Go back to main menu
                pin = int(input("Enter PIN: "))
                if BankAccount.authenticate(acc, pin):
                    print("Login successful.")
                    user_account = BankAccount(acc)
                    while True:
                        print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Logout")
                        op = input("Choose operation: ")

                        try:
                            if op == '1':
                                print(f"Balance: ${user_account.check_balance():.2f}")
                            elif op == '2':
                                amt = float(input("Enter amount to deposit: "))
                                user_account.deposit(amt)
                                print("Deposit successful.")
                                print(f"💰 Updated Balance: ${user_account.check_balance():.2f}")
                            elif op == '3':
                                amt = float(input("Enter amount to withdraw: "))
                                user_account.withdraw(amt)
                                print("Withdrawal successful.")
                                print(f"💰 Updated Balance: ${user_account.check_balance():.2f}")
                            elif op == '4':
                                break
                            else:
                                print("Invalid option.")
                        except Exception as e:
                            print(f"Error: {e}")
            except ValueError as ve:
                print(f"Login error: {ve}")
        elif choice == '3':
            print("Thank you for using the bank simulator.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
