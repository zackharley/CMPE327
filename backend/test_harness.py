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

    def test_create_account(self, transaction_type, account_number, name):
        transaction = Transaction(transaction_type ,recipient_account_number=account_number, account_name=name)
        self.handle_transaction(transaction)
        self.after_test()

    def withdraw(self):
        # Test it here
        self.after_test()
