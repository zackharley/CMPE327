class Login:

    def login(self):
        session_type = get_session_type()
        if is_valid_session_type(session_type):
            self.state.session_in_progress = True
        else:
            self.state.session_in_progress = False
            raise AssertionError('Invalid login type')


def get_session_type():
    session_type_prompt = 'Please enter a session type: '
    return input(session_type_prompt)


def is_valid_session_type(session_type):
    valid_session_types = ['agent', 'machine']
    return session_type in valid_session_types
