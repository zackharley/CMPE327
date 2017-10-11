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
    DeleteAcct,
    Deposit,
    Login,
    Logout,
    Transfer,
    Withdraw
)


class Qbasic(*Mixins):

    def __init__(self):
        self.state = State()

    @staticmethod
    def file(input_file):
        print('Running in input mode')

    def terminal(self):
        self.state.running = True
        while self.state.running:
            command = Qbasic.get_command()
            self.handle_command(command)

    @staticmethod
    def get_command():
        qbasic_command_prompt = 'Please input a command: '
        return input(qbasic_command_prompt)

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
                print('You do not have the privileges to use this command.')
            elif not self.state.session_in_progress and not command == 'login':
                print('Must login before using terminal')
            elif self.state.session_in_progress and command == 'login':
                print('You are already logged in!')
            else:
                response = valid_commands[command]()
        else:
            print('Invalid command!')


    # Util methods

    def exit(self):
        print('Goodbye!')
        self.state.running = False

    def print_state(self):
        state = {
            'session_in_progress': self.state.session_in_progress,
            'session_type': self.state.session_type,
            'running': self.state.running
        }

        print('\n<==== START STATE ====>')
        for key, value in state.items():
            print(key + ': ' + str(value))
        print('<==== END STATE ====>\n')
