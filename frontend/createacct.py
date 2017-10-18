from .shared.validators import is_valid_account_number, is_valid_name


class CreateAcct:

    def createacct(self):
        has_account_number = False
        has_name = False
        account_number_prompt = "Please enter an account number for the new account: "
        name_prompt = "Enter a name to associate with the account: "

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

        # add account to valid accounts file
        self.print('creating account ' + account_number + ' for ' + name)
