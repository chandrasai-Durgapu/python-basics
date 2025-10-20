from bank_account import BankAccount
class ATM:
    """
    ATM class that will register bank accounts and authenticate pin 
    and allow the user to withdraw amount and deposit amount"""

    def __init__(self):
        self.registered_account={}

    def register_account(self, account: BankAccount):
        """Registers a new bank account into the ATM system."""
        self.registered_account[account.account_number] = account


    def authenticate(self, account_number: int, pin: int):
        """Authenticates a user by account number and PIN."""
        print(f"[DEBUG] Registered accounts: {list(self.registered_account.keys())}")
        account = self.registered_account.get(account_number)

        if account is None:
            
            raise ValueError("Account not found... and Bank Account is not registered with Bank")
        
        if pin == account.pin:
            print("Login Successful")
            return account
        else:
            raise ValueError("Invalid PIN")
        
    
    def display_options(self, account: BankAccount):
        while True:
            print("""Select the correct option: 
            1. Check your Balance 
            2. Withdraw
            3. Deposit
            4. Exit      
            """)

            choice = int(input("Enter your choice: "))
            if choice == 1:
                print(f"Your balance is: ${account.check_balance():.2f}")
            elif choice == 2:
                amount = float(input("Enter amount to withdraw: "))
                account.with_draw(amount)
            elif choice == 3:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            elif choice == 4:
                print("Thank you for using the ATM.")
                break
            else:
                print("Invalid choice. Try again.")      

