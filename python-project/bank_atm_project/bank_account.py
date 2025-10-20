class BankAccount:
    def __init__(self, account_number:int, pin:int, balance: float):
        self.account_number=account_number
        self.pin=pin
        self.balance=balance

    def check_balance(self):
        return self.balance
    
    def deposit(self,amount: float):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        else:
            self.balance= self.balance + amount
            print(f"the total amount is: {self.balance}")


    def with_draw(self,amount: float):
        if amount>0:
            if amount <= self.balance:
                self.balance=self.balance-amount 
                print(f"Withdrawn successfully. New balance: ${self.balance:.2f}")  
            else:
                raise ValueError("Amount cannot be greater than Balance") 
        else:
            raise ValueError("you cannot withdraw negative amount")   

     