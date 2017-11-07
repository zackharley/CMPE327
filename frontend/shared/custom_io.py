# The custom I/O class is responsible receiving all input from the terminal and making sure that it is valid.
# It is also responsible for formatting all output to the terminal window.
class CustomIO:

    # Gets the inputted account number, and calls the validators class to make sure that the account number is legal
    def get_account_number(self, prompt):
        has_account_number = False
        while not has_account_number:
            account_number = self.input(prompt)
            has_account_number = self.is_valid_account_number(account_number, self.valid_accounts)
            if not has_account_number:
                self.print("Invalid account number")
            else:
                return account_number
    
    # Gets the inputted amount, and calls the validators class to make sure that amount is legal
    def get_amount(self, prompt):
        has_amount = False
        while not has_amount:
            amount = self.input(prompt)
            has_amount = self.is_valid_transaction_amount(amount, self.state.session_type)
            if not has_amount:
                self.print('Invalid amount')
            else:
                return amount
 
    # Gets the inputted account name, and calls the validators class to make sure that account name is legal
    def get_name(self, prompt):
        has_name = False
        while not has_name:
            name = self.input(prompt)
            has_name = self.is_valid_name(name)
            if not has_name:
                self.print('Invalid name')
            else:
                return name
    
    # Gets the inputted new account number, and calls the validators class to make sure that the new account number
    # is legal
    def get_new_account_number(self, prompt):
        has_account_number = False
        while not has_account_number:
            account_number = self.input(prompt)
            has_account_number = self.is_valid_new_account_number(account_number, self.valid_accounts)
            if not has_account_number:
                self.print('Invalid account number')
            else:
                return account_number

    def input(self, prompt):
        self.update_logger_suffix()

        full_prompt = prompt + '\n' + self.state.logger_suffix if prompt else self.state.logger_suffix
        return input(full_prompt)

    def print(self, text, prefix=''):
        if self.state.is_file_mode and prefix == '':
            prefix += 'INFO: '
        print(prefix + text)

    def print_command(self, command, options):
        prefix = 'COMMAND: '
        options_string = '[' + ','.join(options) + ']'
        text = 'RUNNING: "' + command + '" with options ' + options_string
        self.print(text, prefix)

    def print_error(self, text):
        prefix = 'ERROR: '
        self.print(text, prefix)

    # Updates the suffix in the terminal window    
    def update_logger_suffix(self):
        self.state.logger_suffix = self.state.session_type + ' > ' if self.state.session_type else '> '
