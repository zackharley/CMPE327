import random
from sys import argv

MAX_AGENT_AMOUNT = 99999999
MAX_MACHINE_AMOUNT = 100000


class InputFile:
    def __init__(self, valid_accounts):
        self.commands = []
        self.session_type = None
        self.valid_accounts = valid_accounts

    def __str__(self):
        return '\n'.join(self.commands)

    def add_command(self, command):
        if command == 'login':
            self.commands.append(command)
            self.session_type = generate_session_type()
            self.commands.append(self.session_type)
        elif command == 'logout':
            self.commands.append(command)
        elif command == 'withdraw':
            self.commands.append(command)
            account_number = self.valid_accounts[random.randint(0, len(self.valid_accounts) - 1)]
            self.commands.append(account_number)
            if self.session_type == 'machine':
                self.commands.append(str(random.randint(1, MAX_MACHINE_AMOUNT)))
            elif self.session_type == 'agent':
                self.commands.append(str(random.randint(1, MAX_AGENT_AMOUNT)))
        elif command == 'deposit':
            self.commands.append(command)
            account_number = self.valid_accounts[random.randint(0, len(self.valid_accounts) - 1)]
            self.commands.append(account_number)
            if self.session_type == 'machine':
                self.commands.append(str(random.randint(1, MAX_MACHINE_AMOUNT)))
            elif self.session_type == 'agent':
                self.commands.append(str(random.randint(1, MAX_AGENT_AMOUNT)))
        elif command == 'transfer':
            self.commands.append(command)
            sender_account_number = self.valid_accounts[random.randint(0, len(self.valid_accounts) - 1)]
            self.commands.append(sender_account_number)
            remaining_valid_account_numbers = [account_number for account_number in self.valid_accounts if account_number != sender_account_number]
            recipient_account_number = remaining_valid_account_numbers[random.randint(0, len(remaining_valid_account_numbers) - 1)]
            self.commands.append(recipient_account_number)
            if self.session_type == 'machine':
                self.commands.append(str(random.randint(1, MAX_MACHINE_AMOUNT)))
            elif self.session_type == 'agent':
                self.commands.append(str(random.randint(1, MAX_AGENT_AMOUNT)))
        elif command == 'createacct':
            self.commands.append(command)
            account_number = generate_account_number(self.valid_accounts)
            self.valid_accounts.append(account_number)
            self.commands.append(account_number)
            self.commands.append('Zack')
        elif command == 'deleteacct':
            self.commands.append(command)
            account_number = self.valid_accounts[random.randint(0, len(self.valid_accounts) - 1)]
            self.valid_accounts.remove(account_number)
            self.commands.append(account_number)
            self.commands.append('Zack')


def generate_account_number(existing_accounts):
    account_number_length = 7
    account_number = str(random.randint(1, 9))
    for i in range(1, account_number_length):
        account_number += str(random.randint(0, 9))
    return account_number if account_number not in existing_accounts else generate_account_number(existing_accounts)


def generate_session_type():
    index = random.randint(0, 1)
    return ['agent', 'machine'][index]


DEFAULT_COMMANDS = ['deposit', 'transfer', 'withdraw']


def generate_command(session_type):
    other_commands = ['createacct', 'deleteacct'] if session_type == 'agent' else []
    commands = [*DEFAULT_COMMANDS, *other_commands]
    index = random.randint(0, len(commands) - 1)
    return commands[index]


def generate_random_input_file():
    valid_accounts_path = argv[1]
    valid_accounts_file = open(valid_accounts_path, 'r')
    valid_accounts = valid_accounts_file.readlines()
    valid_accounts.pop()  # remove the account number 0000000
    for i in range(0, len(valid_accounts)):
        valid_accounts[i] = valid_accounts[i].strip('\n')

    file = InputFile(valid_accounts)
    file.add_command('login')
    number_of_commands = random.randint(1, 5)
    for i in range(number_of_commands):
        command = generate_command(file.session_type)
        file.add_command(command)

    file.add_command('logout')
    return file


print(generate_random_input_file())
