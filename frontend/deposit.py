from .shared.validators import is_valid_account_number, is_valid_transaction_amount


class Deposit:

    def deposit(self):
        has_account_number = False
        has_amount_to_deposit = False
        account_number_prompt = 'Please enter the account number you wish to deposit to: '
        amount_to_deposit_prompt = 'Please enter an amount to deposit, in cents: '
        while not has_account_number:
            account_number = self.input(account_number_prompt)
            has_account_number = is_valid_account_number(account_number, self.valid_accounts)
            if not has_account_number:
                self.print('Invalid account number')
        while not has_amount_to_deposit:
            amount_to_deposit = self.input(amount_to_deposit_prompt)
            has_amount_to_deposit = is_valid_transaction_amount(amount_to_deposit, self.state.session_type)
            if not has_amount_to_deposit:
                self.print('Invalid deposit amount')
        # update account balance
