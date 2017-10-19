from frontend.shared.validators import Validators


class CustomIO:

    def get_account_number(self, prompt):
        has_account_number = False
        while not has_account_number:
            account_number = self.input(prompt)
            has_account_number = Validators.is_valid_account_number(account_number, self.valid_accounts)
            if not has_account_number:
                self.print("Invalid account number")
            else:
                return account_number

    def get_amount(self, prompt):
        has_amount = False
        while not has_amount:
            amount = self.input(prompt)
            has_amount = Validators.is_valid_transaction_amount(amount, self.state.session_type)
            if not has_amount:
                self.print('Invalid amount')
            else:
                return amount

    def get_name(self, prompt):
        has_name = False
        while not has_name:
            name = self.input(prompt)
            has_name = Validators.is_valid_name(name)
            if not has_name:
                self.print('Invalid name')
            else:
                return name

    def get_new_account_number(self, prompt):
        has_account_number = False
        while not has_account_number:
            account_number = self.input(prompt)
            has_account_number = Validators.is_valid_new_account_number(account_number, self.valid_accounts)
            if not has_account_number:
                self.print("Invalid account number")
            else:
                return account_number

    def input(self, prompt):
        self.update_logger_suffix()

        full_prompt = prompt + '\n' + self.state.logger_suffix if prompt else self.state.logger_suffix
        return input(full_prompt)

    def print(self, text):
        print(text)

    def update_logger_suffix(self):
        self.state.logger_suffix = self.state.session_type + ' > ' if self.state.session_type else '> '
