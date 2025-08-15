import json
import os

def save_accounts(accounts):
    with open('accounts.json', 'w', encoding='utf-8') as f:
        json.dump(accounts, f, indent=4)
        print("Accounts saved successfully.")

def load_accounts():
    if not os.path.exists('accounts.json'):
        return {}
    try:
        with open('accounts.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except (ValueError, json.JSONDecodeError):
        return {}

class BankAccount:
    def __init__(self, account_name, balance):
        self.account_name = account_name
        self.balance=balance
    def deposit(self, amount):
        if amount <=0:
            print("Invalid amount")
        else:
            self.__balance+=amount
            print(f"Deposited ₹{amount}")
    def withdraw(self, amount):
        if amount<=0:
            print("Invalid amount")
        elif amount>self.balance:
            print("Insufficient balance")
        else:
            self.__balance-=amount
            print(f"Withdrew ₹{amount}")
    def get_balance(self):
        return self.__balance
  