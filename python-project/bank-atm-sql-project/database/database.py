import sqlite3

def get_connection():
    return sqlite3.connect('bank.db')


def setup_database():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ACCOUNTS(
                    account_number INTEGER PRIMARY KEY,
                    pin INTEGER NOT NULL,
                    balance REAL NOT NULL)
                   ''')
    conn.commit()
    conn.close()

