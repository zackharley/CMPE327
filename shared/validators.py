import re


# A list of validators to determine whether a specific input meets the constraints of the system
class Validators:
    # Determine if an account number is valid
    @staticmethod
    def is_valid_account_number(account_number, valid_accounts):
        valid_account_number_length = 7

        if len(account_number) != valid_account_number_length:
            return False
        elif account_number[0] == '0':
            return False
        elif account_number not in valid_accounts:
            return False
        else:
            return True

    # Determines if an account number is valid to be created
    @staticmethod
    def is_valid_new_account_number(account_number, valid_accounts):
        valid_account_number_length = 7

        if len(account_number) != valid_account_number_length:
            return False
        elif account_number[0] == '0':
            return False
        elif account_number in valid_accounts:
            return False
        else:
            return True

    # Determines if a name is valid
    @staticmethod
    def is_valid_name(name):
        valid_name_min_length = 3
        valid_name_max_length = 30
        if len(name) < valid_name_min_length or len(name) > valid_name_max_length:
            return False
        elif name[0] == ' ' or name[-1] == ' ':
            return False
        elif not re.match('^[a-zA-Z0-9 ]+$', name):
            return False
        else:
            return True

    # Determines if a session is a valid session type
    @staticmethod
    def is_valid_session_type(session_type):
        valid_session_types = ['agent', 'machine']
        return session_type in valid_session_types

    # Determine if a transaction amount is valid
    # Calls the correct function based on the session_type
    @staticmethod
    def is_valid_transaction_amount(amount, session_type):
        if not amount.isdigit():
            return False

        if session_type == 'agent':
            return Validators.is_valid_agent_transaction_amount(amount)
        elif session_type == 'machine':
            return Validators.is_valid_machine_transaction_amount(amount)
        else:
            return False

    @staticmethod
    def is_valid_agent_transaction_amount(amount):
        valid_amount_agent_max = 99999999
        if 0 < int(amount) <= valid_amount_agent_max:
            return True
        else:
            return False

    @staticmethod
    def is_valid_machine_transaction_amount(amount):
        valid_amount_machine_max = 100000
        if 0 < int(amount) <= valid_amount_machine_max:
            return True
        else:
            return False

    @staticmethod
    def is_created_or_deleted_account(account_number, created_or_deleted_accounts):
        return account_number in created_or_deleted_accounts
