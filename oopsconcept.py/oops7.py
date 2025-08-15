class BankAccount:
    def __init__(self, account_name, balance=0):
        self.account_name = account_name
        self.balance = balance
    def deposit(self, amount):
        if amount<=0:
            print("Invalid amount")
        else:
            self.balance += amount
            # print(f"Deposited Amount is ${amount}")
    def withdraw(self, amount):
        if amount>self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            # print(f"Withdrawn Amount is ${amount}")
    def check_balance(self):
        return(f"Your current balance is ${self.balance}")
class SavingAccount(BankAccount):
    def __init__(self, account_name, balance=0, interest_rate=0.05):
        super().__init__(account_name, balance)
        self.interest_rate=interest_rate
    def calculate_interest(self):
        intrest=self.balance*self.interest_rate/100
        self.balance+=intrest
    def check_balance(self):
        super().check_balance()
        print(f"Saving Account Name- {self.account_name}, Your current balance is ${self.balance}, Interest Rate is {self.interest_rate}%")
class CurrentAccount(BankAccount):
    def __init__(self, account_name, balance=0, overdraft_limit=1000):
        super().__init__(account_name, balance)
        self.overdraft_limit=overdraft_limit
    def withdraw(self, amount):
        total_amount=self.balance + self.overdraft_limit
        if amount<=total_amount:
            self.balance -= amount
            # print(f"withdrawn Amount is ${amount}, Remaining balance is ${self.balance}")
        else:
            print("Withdrawal exceeds overdraft limit")
    def check_balance(self):
        super().check_balance()
        print(f"Current Account Name- {self.account_name}, Your current balance is ${self.balance}, Overdraft Limit: {self.overdraft_limit}")

c1=SavingAccount("shahid", 5000, 4)
d1=CurrentAccount("ilyas", 2000, 1000)
c1.deposit(500)
c1.calculate_interest()
d1.withdraw(2500)
c1.check_balance() 
d1.check_balance() 