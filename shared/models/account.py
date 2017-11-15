from shared.validators import Validators

'''
The account class holds all information related to accounts and their properties.
This includes getter and setter methods.
'''
class Account:

    AGENT_SESSION_TYPE = 'agent'

    def __init__(self, account_number, balance, name):
        self.account_number = account_number
        self.balance = int(balance)
        self.name = name

    def __str__(self):
        return '{} {} {}'.format(self.account_number, self.balance, self.name)

    def get_account_number(self):
        return self.account_number

    def get_balance(self):
        return self.balance

    def get_name(self):
        return self.name

    def set_account_number(self, account_number):
        self.account_number = account_number

    def set_balance(self, balance):
        self.balance = int(balance)

    def set_name(self, name):
        self.name = name

    def deposit(self, amount):
        if Validators.is_valid_transaction_amount(amount, self.AGENT_SESSION_TYPE):
            self.balance += int(amount)
        else:
            raise ValueError('Invalid deposit amount')

    def withdraw(self, amount):
        if not Validators.is_valid_transaction_amount(amount, self.AGENT_SESSION_TYPE):
            raise ValueError('Invalid withdrawal amount')
        elif self.balance - int(amount) < 0:
            raise ValueError('Cannot process withdrawals that put the balance to less than $0')
        else:
            self.balance -= int(amount)


