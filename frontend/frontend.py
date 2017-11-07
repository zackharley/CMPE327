from frontend.shared.custom_io import CustomIO
from frontend.createacct import CreateAcct
from frontend.deleteacct import DeleteAcct
from frontend.deposit import Deposit
from frontend.login import Login
from frontend.logout import Logout
from frontend.state import State
from frontend.transaction_manager.transaction_manager import TransactionManager
from frontend.transfer import Transfer
from frontend.withdraw import Withdraw
from frontend.shared.validators import Validators
from os import path

# A list of classes for the Frontend to inherit
Mixins = (
    CreateAcct,
    CustomIO,
    DeleteAcct,
    Deposit,
    Login,
    Logout,
    Transfer,
    Withdraw,
    Validators
)


# The main entry point for the frontend of the QBASIC application
# Each instance of the frontend has its own state and can be run
# in either terminal or file mode
class Frontend(*Mixins):

    def __init__(self, valid_accounts_file, input_file=None):
        self.commands = None
        self.state = State()
        self.transaction_manager = TransactionManager(input_file)
        self.valid_accounts_file = valid_accounts_file
        self.valid_accounts = None

    def file(self, input_file):
        self.state.is_file_mode = True
        self.state.input_file = input_file
        self.commands = self.get_commands_from_file(input_file)
        i = 0
        while i < len(self.commands):
            command = self.commands[i]
            if command in ['transfer']:
                self.handle_command(command, self.commands[i+1:i+4])
                i += 4
            elif command in ['createacct', 'deleteacct', 'deposit', 'withdraw']:
                self.handle_command(command, self.commands[i+1:i+3])
                i += 3
            elif command in ['login']:
                self.handle_command(command, [self.commands[i+1]])
                i += 2
            else:
                self.handle_command(command)
                i += 1

    def terminal(self):
        self.state.running = True
        self.print('Welcome to QBASIC! Please enter a command:')
        while self.state.running:
            command = self.get_command()
            self.handle_command(command)

    def get_command(self):
        return self.input('')

    @staticmethod
    def get_commands_from_file(input_file):
        dir_path = path.dirname(path.realpath(__file__))
        file_path = path.join(dir_path, '..', input_file)
        file = open(file_path, 'r')
        commands = file.readlines()
        file.close()
        for i in range(0, len(commands)):
            commands[i] = commands[i].strip('\n')
        return commands

    def handle_command(self, command, options=[]):
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
            if self.state.is_file_mode:
                self.print_command(command, options)

            if command in privileged_command_names and self.state.session_type == 'machine':
                self.print_error('You do not have the privileges to use this command.')
            elif not self.state.session_in_progress and command != 'login' and command != 'exit':
                self.print_error('Must login before using terminal')
            elif self.state.session_in_progress and command == 'login':
                self.print_error('You are already logged in!')
            else:
                response = valid_commands[command](*options)
        else:
            self.print('Invalid command!')

    # Util methods

    def exit(self):
        self.print('Goodbye!')
        self.state.running = False

    def print_state(self):
        state = {
            'session_in_progress': self.state.session_in_progress,
            'session_type': self.state.session_type,
            'running': self.state.running,
            'withdrawal_total': self.state.withdrawal_total
        }

        self.print('\n<==== START STATE ====>')
        for key, value in state.items():
            self.print(key + ': ' + str(value))
        self.print('<==== END STATE ====>\n')
