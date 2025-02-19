class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, acc_no, balance=0):
        self.accounts[acc_no] = balance

    def deposit(self, acc_no, amount):
        if acc_no in self.accounts:
            self.accounts[acc_no] += amount

    def withdraw(self, acc_no, amount):
        if acc_no in self.accounts and self.accounts[acc_no] >= amount:
            self.accounts[acc_no] -= amount

    def display(self, acc_no):
        if acc_no in self.accounts:
            print(f'Account {acc_no}: Balance {self.accounts[acc_no]}')