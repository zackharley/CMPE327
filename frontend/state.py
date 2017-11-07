class State:

    # The state class holds the states of elements in the frontend for each session.
    # These variables are used to continuously loop through commands
    def __init__(self):
        self.input_file = None
        self.is_file_mode = False
        # The suffix in the terminal window
        self.logger_suffix = ''
        # True if the program is running
        self.running = False
        # True when logged in, False when logged out
        self.session_in_progress = False
        # The session type is either agent or machine
        self.session_type = None
        # The total amount withdrawed in one session
        self.withdrawal_total = 0
        # An array tracking all the created or deleted accounts
        self.created_or_deleted_accounts = []