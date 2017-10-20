class Transfer:
    
    #Transfer an amount between two a valid accounts in the QBASIC system
    def transfer(self):
        recipient_account_number_prompt = 'Please enter the recipient account for this transfer: '
        sender_account_number_prompt = 'Please enter the sender account for this transfer: '
        amount_to_transfer_prompt = 'Please enter an amount to transfer, in cents: '

        recipient_account_number = self.get_account_number(recipient_account_number_prompt)
        sender_account_number = self.get_sender_account_number(sender_account_number_prompt, recipient_account_number)
        amount_to_transfer = self.get_amount(amount_to_transfer_prompt)

        # Creates the transaction record for the withdrawal         
        self.transaction_manager.add(
            transaction_type='transfer',
            recipient_account_number=recipient_account_number,
            amount=amount_to_transfer,
            sender_account_number=sender_account_number
        )

        self.print('Transfer successful!')

        #Validates that the sender and the reciepent account numbers are identical
    def get_sender_account_number(self, prompt, recipient_account_number):
        has_sender_account_number = False
        while not has_sender_account_number:
            sender_account_number = self.get_account_number(prompt)
            if not recipient_account_number == sender_account_number:
                return sender_account_number
