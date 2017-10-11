class Logout:
    def logout(self):
        self.state.session_in_progress = False
        self.state.session_type = None
        # create transaction summary file
