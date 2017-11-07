class DeleteAcct:
    # Delete an existing account in the QBASIC system
    def deleteacct(self, account_number=None, name=None):
        account_number_prompt = 'Please enter an account number to delete: '
        name_prompt = 'Enter the name associated with this account: '

        if (account_number and not name) or (not account_number and name):
            self.print_error('Must supply both an account number and a name')
            return

        if not account_number:
            account_number = self.get_account_number(account_number_prompt)
        if not name:
            name = self.get_name(name_prompt)
        
        # Checks if the account is valid, then creates the transaction record
        if account_number in self.valid_accounts:
            self.transaction_manager.add(
                transaction_type='createacct',
                recipient_account_number=account_number,
                account_name=name
            )
            self.print('Account deletion request completed')
        else:
            self.print('Unable to delete account')
