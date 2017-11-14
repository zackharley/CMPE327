from backend.accounts_file_service import AccountsFileService
from backend.state import State
from backend.transaction_file_service import TransactionFileService
from backend.transaction_management_service import TransactionManagementService
from shared.custom_io import CustomIO
from os import path

Mixins = (
    CustomIO,
    TransactionManagementService
)


class Backend(*Mixins):

    MASTER_ACCOUNTS_FILE_PATH = path.join(path.dirname(path.realpath(__file__)), '..', 'shared', 'master_accounts_file.txt')
    TRANSACTION_FILES_DIRECTORY = path.join(path.dirname(path.realpath(__file__)), '..', 'frontend', 'sessions')
    VALID_ACCOUNTS_FILE_PATH = path.join(path.dirname(path.realpath(__file__)), '..', 'shared', 'valid_accounts_file.txt')

    def __init__(self):
        self.state = State()

    def run(self):
        self.state.accounts = AccountsFileService.get_accounts_from_file(self.MASTER_ACCOUNTS_FILE_PATH)
        self.state.transactions = TransactionFileService.get_transactions_from_directory(self.TRANSACTION_FILES_DIRECTORY)
        self.handle_transactions(self.state.transactions)
        AccountsFileService.create_master_accounts_file(self.MASTER_ACCOUNTS_FILE_PATH, self.state.accounts.values())
        AccountsFileService.create_valid_accounts_file(self.VALID_ACCOUNTS_FILE_PATH, self.state.accounts.keys())

        # Reset state
        self.state = State()

