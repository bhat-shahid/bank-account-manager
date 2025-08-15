class BankAccount:
    def __init__(self, account_name, balance=0):
        self.account_name = account_name
        self.balance = balance
    def deposit(self, amount):
        if amount<=0:
            print("Deposit amount must be positive.")
        else:
            self.balance+=amount
            print(f"Deposited ${amount}. New balance is ${self.balance}.")
    def withdraw(self, amount):
        if amount<=0:
            print("Withdrawal amount must be positive.")
        elif amount>self.balance:
            print("Insufficient funds.")
        else:
            self.balance-=amount
            print(f"Withdrew ${amount}. New balance is ${self.balance}.")
            
    def display(self):
        print(f"Account Holder:{self.account_name}")
        print(f"Current Balance: {self.balance}")
account1 = BankAccount("Shahid Ayoub")
account1.display()
account1.deposit(1000)
account1.withdraw(300)
account1.withdraw(800)
account1.deposit(-50)
account1.withdraw(-100)
account1.display()