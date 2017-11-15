from os import remove, path
from shared.models.account import Account

'''
The account file service class is responsible for creating the new Master Accounts file and the new Valid Accounts List file
'''
class AccountsFileService:
    @staticmethod
	# Gets the accounts from the accounts file
    def get_accounts_from_file(file_path):
        file = open(file_path, 'r')
        file_lines = file.readlines()
        file.close()

        accounts = {}

        for line in file_lines:
            account_fields = line.rstrip('\n').split(' ')
            account = Account(*account_fields)
            accounts.update({account.get_account_number(): account})

        return accounts

    @staticmethod
	# Creates the master accounts file
    def create_master_accounts_file(file_path, accounts):
        if path.isfile(file_path):
            remove(file_path)
        file = open(file_path, 'w+')
        file.writelines('\n'.join(map(lambda account: str(account), accounts)))
        file.close()

    @staticmethod
	# Creates a valid accounts file
    def create_valid_accounts_file(file_path, account_numbers):
        if path.isfile(file_path):
            remove(file_path)
        file = open(file_path, 'w+')
        file.writelines('\n'.join([*account_numbers, '0000000']))
        file.close()
