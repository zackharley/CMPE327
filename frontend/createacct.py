class CreateAcct:
    # Creates an account in the QBASIC system
    def createacct(self, account_number=None, name=None):
        account_number_prompt = 'Please enter an account number to create: '
        name_prompt = 'Enter a name to associate with the account: '

        if (account_number and not name) or (not account_number and name):
            self.print_error('Must supply both an account number and a name')
            return

        if not account_number:
            account_number = self.get_new_account_number(account_number_prompt)
        if not name:
            name = self.get_name(name_prompt)

        if not self.is_valid_account_number(account_number, self.valid_accounts):
            self.print_error('Invalid account number')
            return
        if not self.is_valid_name(name):
            self.print_error('Invalid name')
            return

        self.print('Creating account ' + account_number + ' for ' + name)
        # Sets the properties for the transaction to be put in the transaction summary file
        self.transaction_manager.add(
            transaction_type='createacct',
            recipient_account_number=account_number,
            account_name=name
        )
