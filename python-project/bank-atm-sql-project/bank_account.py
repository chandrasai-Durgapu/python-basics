from database.database import get_connection

class BankAccount:

    def __init__(self,account_number):
        self.account_number=account_number

    def get_account(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM accounts WHERE account_number=?", (self.account_number,))
        account = cursor.fetchone()
        conn.close()
        return account


    def check_balance(self):
        account = self.get_account()
        return account[2] if account else None

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        balance = self.check_balance()
        new_balance = balance + amount
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE accounts SET balance=? WHERE account_number=?", (new_balance, self.account_number))
        conn.commit()
        conn.close()

    def withdraw(self, amount):
        balance = self.check_balance()
        if amount <= 0:
            raise ValueError("Withdrawal must be positive.")
        if amount > balance:
            raise ValueError("Insufficient funds.")
        new_balance = balance - amount
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE accounts SET balance=? WHERE account_number=?", (new_balance, self.account_number))
        conn.commit()
        conn.close()

    @staticmethod
    def authenticate(account_number, pin):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM accounts WHERE account_number=? AND pin=?", (account_number, pin))
        result = cursor.fetchone()
        conn.close()
        return result is not None

    @staticmethod
    def create_account(account_number, pin, initial_balance=0.0):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO accounts VALUES (?, ?, ?)", (account_number, pin, initial_balance))
        conn.commit()
        conn.close()    