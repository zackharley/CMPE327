from .shared.validators import is_valid_account_number, is_valid_name


class DeleteAcct:

    def deleteacct(self):
        has_account_number = False
        has_name = False
        account_number_prompt = "Please enter an account number to delete: "
        name_prompt = "Enter the name associated with this account: "

        while not has_account_number:
            account_number = self.input(account_number_prompt)
            has_account_number = is_valid_account_number(account_number, self.valid_accounts)
            if not has_account_number:
                self.print("Invalid account number")
        while not has_name:
            name = self.input(name_prompt)
            has_name = is_valid_name(name)
            if not has_name:
                self.print('Invalid name')

        # if account exists:
        #     delete account
        # else:
        #     print('Unable to delete account')
        self.state.running = False
