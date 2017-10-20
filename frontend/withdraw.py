class Withdraw:
    
    #Withdraw an amount from a valid account in the QBASIC system
    def withdraw(self):
        account_number_prompt = 'Please enter the account number you wish to withdraw from: '
        amount_to_withdraw_prompt = 'Please enter an amount to withdraw, in cents: '

        account_number = self.get_account_number(account_number_prompt)
        amount_to_withdraw = self.get_amount(amount_to_withdraw_prompt)

        #Ensures that no more thatn $1,000 can be withdrawn from a single account in a single ATM session
        if self.state.withdrawal_total + int(amount_to_withdraw) > 100000 and self.state.session_type == 'machine':
            print('Unable to withdraw, insufficient funds in terminal.')
        else:
            self.state.withdrawal_total += int(amount_to_withdraw)
            # Creates the transaction record for the withdrawal         
            self.transaction_manager.add(
                transaction_type='withdraw',
                recipient_account_number=account_number,
                amount=amount_to_withdraw
            )
            self.print('Withdrawal successful!')
