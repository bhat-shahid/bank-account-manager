class BankAccount:
    def __init__(self, account_name, balance=0):
        self.account_name = account_name
        self.balance=balance
    def deposit(self, amount):
        self.balance+=amount
        print(f"deposit : {amount}")
    def withdrawn(self, amout):
        if self.balance>=amout:
            self.balance-=amout
            print(f"withdrawn : {amout}")
        else:
            print("insufficient balance")
    def display_blance(self):
        print(f"Account Holder is {self.account_name}, and balance is {self.balance}")


bankingDetails=BankAccount("shahid")
bankingDetails.deposit(2000)
bankingDetails.withdrawn(500)
bankingDetails.withdrawn(600)
bankingDetails.display_blance() 