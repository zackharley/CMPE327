import re


class Validators:
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

    @staticmethod
    def is_valid_transaction_amount(amount, session_type):
        if session_type == 'agent':
            return Validators.is_valid_agent_transaction_amount(amount)
        elif session_type == 'machine':
            return Validators.is_valid_machine_transaction_amount(amount)
        else:
            return False


    @staticmethod
    def is_valid_agent_transaction_amount(amount):
        valid_amount_agent_max = 99999999
        return 0 < int(amount) <= valid_amount_agent_max


    @staticmethod
    def is_valid_machine_transaction_amount(amount):
        valid_amount_machine_max = 100000
        return 0 < int(amount) <= valid_amount_machine_max
