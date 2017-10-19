class State:

    def __init__(self):
        self.command_in_progress = False
        self.logger_suffix = ''
        self.running = False
        self.session_in_progress = False
        self.session_type = None
        self.withdrawal_total = 0
