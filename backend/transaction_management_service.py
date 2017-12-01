from shared.models.account import Account
from shared.validators import Validators

'''
The transaction management service class complete all transaction listed within the Transaction Summary file.
This also includes validation before transactions are completed.
'''


class TransactionManagementService:
    # Handles all transactions
    def handle_transactions(self, transactions):
        for transaction in transactions:
            self.handle_transaction(transaction)

        # Handles an individual transaction

    def handle_transaction(self, transaction):
        valid_transactions = {
            'DEL': self.delete_account,
            'DEP': self.deposit,
            'NEW': self.create_account,
            'WDR': self.withdraw,
            'XFR': self.transfer
        }

        transaction_code = transaction.get_transaction_code()

        options = []
        if transaction_code in valid_transactions:
            options = get_options_from_transaction(transaction)
        if len(options) > 0:
            self.print('Handling transaction - {}'.format(transaction))
            try:
                valid_transactions[transaction_code](*options)
            except ValueError as e:
                self.print_error(str(e))

            # Creates an account and updates accounts file

    def create_account(self, account_number, name):
        balance = 0
        new_account = Account(account_number, balance, name)

        self.state.accounts.update({account_number: new_account})

    # Deletes an account and updates accounts file
    def delete_account(self, account_number, name):
        account_to_delete = self.state.accounts[account_number]
        if account_to_delete.get_name() != name:
            self.print_error('Account name does not match transaction account name')
        account_to_delete.set_balance(0)

    # Deposits funds to an account
    def deposit(self, account_number, amount):
        account = self.state.accounts[account_number]
        if isinstance(account, Account):
            account.deposit(amount)

        # Transfers funds between two accounts

    def transfer(self, recipient_account_number, sender_account_number, amount):
        sender_account = self.state.accounts[sender_account_number]
        recipient_account = self.state.accounts[recipient_account_number]
        if isinstance(sender_account, Account) and isinstance(recipient_account, Account):
            sender_account.withdraw(amount)
            recipient_account.deposit(amount)

        # Withdraws funds from an account

    def withdraw(self, account_number, amount):
        account = self.state.accounts[account_number]
        if isinstance(account, Account):
            account.withdraw(amount)


# Gets the full transaction information and returns it
def get_options_from_transaction(transaction):
    transaction_code = transaction.get_transaction_code()
    recipient_account_number = transaction.get_recipient_account_number()
    amount = transaction.get_amount()
    sender_account_number = transaction.get_sender_account_number()
    account_name = transaction.get_account_name()

    if transaction_code == 'DEL':
        options = [recipient_account_number, account_name]
    elif transaction_code == 'DEP':
        options = [recipient_account_number, amount]
    elif transaction_code == 'NEW':
        options = [recipient_account_number, account_name]
    elif transaction_code == 'WDR':
        options = [recipient_account_number, amount]
    elif transaction_code == 'XFR':
        options = [recipient_account_number, sender_account_number, amount]
    else:
        options = []

    return options
