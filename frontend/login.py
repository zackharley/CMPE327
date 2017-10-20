from os import path


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
                self.valid_accounts = get_valid_accounts(self.valid_accounts_file)
                login_in_progress = False

            else:
                self.logout()
                self.print('Invalid login type.')

        self.print('Logged in as ' + session_type)


def get_valid_accounts(valid_accounts_file):
    dir_path = path.dirname(path.realpath(__file__))
    file_path = path.join(dir_path, valid_accounts_file)
    file = open(file_path, 'r')
    valid_accounts = file.readlines()
    file.close()
    for i in range(0, len(valid_accounts)):
        valid_accounts[i] = valid_accounts[i].strip('\n')
    return valid_accounts


def is_valid_session_type(session_type):
    valid_session_types = ['agent', 'machine']
    return session_type in valid_session_types
