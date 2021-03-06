class Logout:
    
    #Logout of a session in the QBASIC system, change the state properties and call the transaction manager to create the transaction summary file
    def logout(self):
        self.state.session_in_progress = False
        self.state.session_type = None
        self.transaction_manager.add(transaction_type='logout')
        self.transaction_manager.summarize()
        self.transaction_manager.reset()
        self.print('You have been logged out!')
