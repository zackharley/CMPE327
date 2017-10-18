from .shared.validators import is_valid_account_number, is_valid_transaction_amount


class Transfer:

    def transfer(self):
        has_recipient_account_number = False
        has_sender_account_number = False
        has_amount_to_withdraw = False
        recipient_account_number_prompt = 'Please enter the recipient account for this transfer: '
        sender_account_number_prompt = 'Please enter the sender account for this transfer: '
        amount_to_transfer_prompt = 'Please enter an amount to transfer, in cents: '

        while not has_recipient_account_number:
            recipient_account_number = self.input(recipient_account_number_prompt)
            has_recipient_account_number = is_valid_account_number(recipient_account_number, self.valid_accounts)
            if not has_recipient_account_number:
                self.print('Invalid account number')
        while not has_sender_account_number:
            sender_account_number = self.input(sender_account_number_prompt)
            has_sender_account_number = is_valid_account_number(sender_account_number, self.valid_accounts)
            if not has_sender_account_number:
                self.print('Invalid account number')
        while not has_amount_to_withdraw:
            amount_to_deposit = self.input(amount_to_transfer_prompt)
            has_amount_to_withdraw = is_valid_transaction_amount(amount_to_deposit, self.state.session_type)
            if not has_amount_to_withdraw:
                self.print('Invalid withdrawal amount')
        # update account balance
