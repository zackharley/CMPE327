from backend.transaction_management_service import TransactionManagementService
from shared.custom_io import CustomIO
from backend.state import State
from shared.models.transaction import Transaction
from shared.models.account import Account

Mixins = (
    CustomIO,
    TransactionManagementService
)


class TestHarness(*Mixins):
    def __init__(self):
        self.state = initialize_state()

    def after_test(self):
        self.state = initialize_state()

    def test_transaction(self, transaction_type, account_number, name='***', amount='000'):
        try:
            transaction = Transaction(transaction_type, recipient_account_number=account_number, account_name=name, amount=amount)
            print('START TESTING TRANSACTION:', transaction)
            self.handle_transaction(transaction)
            print('FINISH TESTING TRANSACTION:', transaction, '\n')
        except LookupError as e:
            print('ERROR:', e, '\n')
        except ValueError as e:
            print('ERROR:', e, '\n')
        except AttributeError as e:
            print('ERROR:', e, '\n')
        self.after_test()


def initialize_state():
    state = State()
    account_number = '1234567'
    balance = '200000'
    name = 'Rick'
    account = Account(account_number, balance, name)
    state.accounts.update({account_number: account})
    return state
