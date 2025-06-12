from account import Account

class SavingsAccount(Account):
    limit = 1000

    def __init__(self, balannce):
        Account.__init__(self, balannce)

    def withdraw(self, amount):
        if amount < 1000:
            super().withdraw(amount)