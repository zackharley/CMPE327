class DeleteAcct:

    def deleteacct(self):
        account_number_prompt = "Please enter an account number to delete: "
        name_prompt = "Enter the name associated with this account: "

        account_number = self.get_account_number(account_number_prompt)
        name = self.get_name(name_prompt)

        if account_number in self.valid_accounts:
            self.transaction_manager.add(
                transaction_type='createacct',
                recipient_account_number=account_number,
                account_name=name
            )
            self.print('Account deletion request completed')
        else:
            self.print('Unable to delete account')