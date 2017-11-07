class Deposit:
    # Deposit an amount to a valid account in the QBASIC system
    def deposit(self, account_number=None, amount_to_deposit=None):
        account_number_prompt = 'Please enter the account number you wish to deposit to: '
        amount_to_deposit_prompt = 'Please enter an amount to deposit, in cents: '

        if (account_number and not amount_to_deposit) or (not account_number and amount_to_deposit):
            self.print_error('Must supply both an account number and an amount to deposit.')
            return

        if not account_number:
            account_number = self.get_account_number(account_number_prompt)
        if not amount_to_deposit:
            amount_to_deposit = self.get_amount(amount_to_deposit_prompt)
 
        # Creates the transaction record for the deposit
        self.transaction_manager.add(
            transaction_type='deposit',
            recipient_account_number=account_number,
            amount=amount_to_deposit
        )

        self.print('Deposit successful!')
