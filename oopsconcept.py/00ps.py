class BankAccount:
    def __init__(self, account_name, balance):
        self.account_name = account_name
        self.balance = balance
    def deposit(self, amount):
        self.balance+=amount
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance-=amount
    def display(self):
        print(f"Account Name: {self.account_name}")
        print(f"Balance: {self.balance}")
class SavingsAccount(BankAccount):
    def __init__(self, account_name, balance,interest_rate):
        super().__init__(account_name, balance)
        self.interest_rate=interest_rate
    def calculate_interest(self):
        interest=self.balance*self.interest_rate/100
        self.balance+=interest
    def display(self):
        super().display()
        print(f"Interest Rate: {self.interest_rate}%")
a1 = SavingsAccount("Aisha", 1000, 5)
a1.deposit(500)
a1.calculate_interest()
a1.display()
