from os import path
from .shared.custom_io import CustomIO
from .createacct import CreateAcct
from .deleteacct import DeleteAcct
from .deposit import Deposit
from .login import Login
from .logout import Logout
from .state import State
from .transfer import Transfer
from .withdraw import Withdraw

Mixins = (
    CreateAcct,
    CustomIO,
    DeleteAcct,
    Deposit,
    Login,
    Logout,
    Transfer,
    Withdraw
)


class Qbasic(*Mixins):

    def __init__(self, valid_accounts_file):
        self.state = State()
        self.valid_accounts = self.get_valid_accounts(valid_accounts_file)

    @staticmethod
    def file(input_file):
        print('Running in input mode')

    def terminal(self):
        self.state.running = True
        self.print('Welcome to QBASIC! Please enter a command:')
        while self.state.running:
            command = self.get_command()
            self.handle_command(command)

    def get_command(self):
        return self.input('')

    def handle_command(self, command):
        valid_commands = {
            'createacct': self.createacct,
            'deleteacct': self.deleteacct,
            'deposit': self.deposit,
            'exit': self.exit,
            'login': self.login,
            'logout': self.logout,
            'state': self.print_state,
            'transfer': self.transfer,
            'withdraw': self.withdraw
        }

        privileged_command_names = ('createacct', 'deleteacct')

        if command in valid_commands:
            if command in privileged_command_names and self.state.session_type == 'machine':
                self.print('You do not have the privileges to use this command.')
            elif not self.state.session_in_progress and command != 'login' and command != 'exit':
                self.print('Must login before using terminal')
            elif self.state.session_in_progress and command == 'login':
                self.print('You are already logged in!')
            else:
                response = valid_commands[command]()
        else:
            self.print('Invalid command!')

    @staticmethod
    def get_valid_accounts(valid_accounts_file):
        dir_path = path.dirname(path.realpath(__file__))
        file_path = path.join(dir_path, valid_accounts_file)
        file = open(file_path, 'r')
        valid_accounts = file.readlines()
        file.close()
        return valid_accounts

    # Util methods

    def exit(self):
        self.print('Goodbye!')
        self.state.running = False

    def print_state(self):
        state = {
            'session_in_progress': self.state.session_in_progress,
            'session_type': self.state.session_type,
            'running': self.state.running
        }

        self.print('\n<==== START STATE ====>')
        for key, value in state.items():
            self.print(key + ': ' + str(value))
            self.print('<==== END STATE ====>\n')
