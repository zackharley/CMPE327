class Transfer:
    
    # Transfer an amount between two a valid accounts in the QBASIC system
    def transfer(self, sender_account_number=None, recipient_account_number=None, amount_to_transfer=None):
        sender_account_number_prompt = 'Please enter the sender account for this transfer: '
        recipient_account_number_prompt = 'Please enter the recipient account for this transfer: '
        amount_to_transfer_prompt = 'Please enter an amount to transfer, in cents: '

        if missing_some_inputs(recipient_account_number, sender_account_number, amount_to_transfer):
            self.print_error('Must supply a recipient account number, a sender account number, and an amount to transfer.')
            return
        
        if not sender_account_number:
            sender_account_number = self.get_sender_account_number(sender_account_number_prompt, recipient_account_number)
        if not recipient_account_number:
            recipient_account_number = self.get_account_number(recipient_account_number_prompt)
        if not amount_to_transfer:
            amount_to_transfer = self.get_amount(amount_to_transfer_prompt)

        if self.is_created_or_deleted_account(sender_account_number, self.state.created_or_deleted_accounts):
            self.print_error('Can\'t perform operations on newly created or deleted accounts')
            return           
            
        if self.is_created_or_deleted_account(recipient_account_number, self.state.created_or_deleted_accounts):
            self.print_error('Can\'t perform operations on newly created or deleted accounts')
            return            
            
        if not self.is_valid_transaction_amount(amount_to_transfer, self.state.session_type):
            print('Invalid transaction amount')
            return
            
        if not self.is_valid_account_number(sender_account_number, self.valid_accounts):
            print('Invalid sender account number')
            return
        
        if not self.is_valid_account_number(recipient_account_number, self.valid_accounts):
            print('Invalid recipient account number')
            return
     
        # Creates the transaction record for the withdrawal         
        self.transaction_manager.add(
            transaction_type='transfer',
            recipient_account_number=recipient_account_number,
            amount=amount_to_transfer,
            sender_account_number=sender_account_number
        )

        self.print('Transfer successful!')

    # Validates that the sender and the recipient account numbers are identical
    def get_sender_account_number(self, prompt, recipient_account_number):
        has_sender_account_number = False
        while not has_sender_account_number:
            sender_account_number = self.get_account_number(prompt)
            if not recipient_account_number == sender_account_number:
                return sender_account_number


def missing_some_inputs(*inputs):
    inputs_have_none_value = False
    inputs_have_non_none_value = False
    for value in inputs:
        if value is not None:
            inputs_have_non_none_value = True
        else:
            inputs_have_none_value = True

    if inputs_have_none_value and inputs_have_non_none_value:
        return True
    else:
        return False
