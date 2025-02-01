class Bank_account:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if self.balance<amount:
            print(f"{self.owner} you have not enough balance")
        else:
            self.balance-=amount

wallet=Bank_account("Sasha",500)
wallet.deposit(500)
wallet.withdraw(700)
wallet.withdraw(700)