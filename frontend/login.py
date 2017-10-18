class Login:

    def get_session_type(self):
        session_type_prompt = 'Please enter a session type: '
        return self.input(session_type_prompt)

    def login(self):
        login_in_progress = True
        while login_in_progress:
            session_type = self.get_session_type()
            if is_valid_session_type(session_type):
                self.state.session_in_progress = True
                self.state.session_type = session_type
                # Load valid accounts file
                login_in_progress = False

            else:
                self.logout()
                self.print('Invalid login type.')


def is_valid_session_type(session_type):
    valid_session_types = ['agent', 'machine']
    return session_type in valid_session_types
