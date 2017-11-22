from backend.transaction_management_service import TransactionManagementService
from shared.custom_io import CustomIO
from backend.state import State
from shared.models.transaction import Transaction

Mixins = (
    CustomIO,
    TransactionManagementService
)


class TestHarness(*Mixins):

    def __init__(self):
        self.state = State()

    def after_test(self):
        self.state = State()

    def create_account(self, account_number, name):
        transaction = Transaction(# put stuff here)
        self.handle_transaction(transaction)
        self.after_test()

    def withdraw(self):
        # Test it here
        self.after_test()
