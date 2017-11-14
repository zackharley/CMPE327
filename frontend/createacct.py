from shared.validators import Validators

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

        if not Validators.is_valid_new_account_number(account_number, self.valid_accounts):
            self.print_error('Invalid account number')
            return
        if not Validators.is_valid_name(name):
            self.print_error('Invalid name')
            return
        if self.is_created_or_deleted_account(account_number, self.state.created_or_deleted_accounts):
            self.print_error('Can\'t perform operations on newly created or deleted accounts')
            return
        
        self.state.created_or_deleted_accounts.append(account_number)
        
        self.print('Creating account ' + account_number + ' for ' + name)
        # Sets the properties for the transaction to be put in the transaction summary file
        self.transaction_manager.add(
            transaction_type='createacct',
            recipient_account_number=account_number,
            account_name=name
        )
