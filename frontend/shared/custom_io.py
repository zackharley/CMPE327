class CustomIO:

    def input(self, prompt):
        self.update_logger_suffix()

        full_prompt = prompt + '\n' + self.state.logger_suffix if prompt else self.state.logger_suffix
        return input(full_prompt)

    def print(self, text):
        print(text)

    def update_logger_suffix(self):
        self.state.logger_suffix = self.state.session_type + ' > ' if self.state.session_type else '> '
