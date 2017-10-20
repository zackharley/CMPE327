class CreateAcct:
    #Creates an account in the QBASIC system
    def createacct(self):
        account_number_prompt = "Please enter an account number to create: "
        name_prompt = 'Enter a name to associate with the account: '

        account_number = self.get_new_account_number(account_number_prompt)
        name = self.get_name(name_prompt)

        self.print('Creating account ' + account_number + ' for ' + name)
        #Sets the properties for the transaction to be put in the transaction summary file
        self.transaction_manager.add(
            transaction_type='createacct',
            recipient_account_number=account_number,
            account_name=name
        )
