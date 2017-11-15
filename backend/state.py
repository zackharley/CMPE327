'''
The state class holds the states of elements in the backend for each session.
This includes the accounts and the transactions from Master Account and Transaction Summary files.
'''
class State:

    def __init__(self):
        self.accounts = {}
        self.transactions = []

