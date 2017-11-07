from hashlib import md5
from os import path
from time import time
from frontend.transaction_manager.transaction import Transaction
import re

# The transaction manager handles all interactions with Transaction Summary files.
# This class also handles interactions with the list of transactions for a particular session,
# allowing a user to add to or reset the collection of transactions.
class TransactionManager:

    def __init__(self, input_file=None):
        self.input_file = input_file
        self.transactions = []

    def add(
        self,
        transaction_type,
        recipient_account_number=None,
        amount=None,
        sender_account_number=None,
        account_name=None
    ):
        args = {}

        if transaction_type:
            args['transaction_type'] = transaction_type
        if recipient_account_number:
            args['recipient_account_number'] = recipient_account_number
        if amount:
            args['amount'] = amount
        if sender_account_number:
            args['sender_account_number'] = sender_account_number
        if account_name:
            args['account_name'] = account_name

        try:
            transaction = Transaction(**args)
            self.transactions.append(transaction)
        except LookupError:
            print('Invalid transaction type')
        except ValueError as e:
            print(str(e))
            print('Invalid transaction information provided')

    def reset(self):
        self.transactions = []

    # Creates a new transaction summary file
    def summarize(self):
        timestamp = int(time())
        hashed_transactions = md5('\n'.join(str(self.transactions)).encode('utf-8')).hexdigest()
        file_suffix = transform_filename(self.input_file) if self.input_file else hashed_transactions
        filename = 'summary_' + str(timestamp) + '.' + file_suffix + '.txt'
        dir_path = path.dirname(path.realpath(__file__))
        file_path = path.join(dir_path, '..', 'sessions', filename)

        file = open(file_path, 'w+')
        for index, transaction in enumerate(self.transactions):
            file.write(str(transaction))
            if index is not len(self.transactions) - 1:
                file.write('\n')
        file.close()


def transform_filename(filename):
    print(type(filename))
    regexp_string = r'(\w+)(?=\.input\.txt)'
    return re.search(regexp_string, filename).group(1)
