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


class Frontend(*Mixins):

    def __init__(self, valid_accounts_file):
        self.state = State()
        self.transaction_manager = TransactionManager()
        self.valid_accounts_file = valid_accounts_file
        self.valid_accounts = None

    def file(self, input_file):
        # To be finished for testing
        self.print('Running in input mode')

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
