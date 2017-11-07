class Withdraw:
    
    # Withdraw an amount from a valid account in the QBASIC system
    def withdraw(self, account_number=None, amount_to_withdraw=None):
        account_number_prompt = 'Please enter the account number you wish to withdraw from: '
        amount_to_withdraw_prompt = 'Please enter an amount to withdraw, in cents: '

        if (account_number and not amount_to_withdraw) or (not account_number and amount_to_withdraw):
            self.print_error('Must supply both an account number and an amount to withdraw.')
            return

        if not account_number:
            account_number = self.get_account_number(account_number_prompt)
        if not amount_to_withdraw:
            amount_to_withdraw = self.get_amount(amount_to_withdraw_prompt)

        if not self.is_valid_transaction_amount(amount_to_withdraw, self.state.session_type):
            print('Invalid transaction amount')
            return
        
        if not self.is_valid_account_number(account_number, self.valid_accounts):
            print('Invalid account number')
            return


        if self.is_created_or_deleted_account(account_number, self.state.created_or_deleted_accounts):
            self.print_error('Can\'t perform operations on newly created or deleted accounts')
            return
        
        # Ensures that no more than $1,000 can be withdrawn from a single account in a single ATM session
        if self.state.withdrawal_total + int(amount_to_withdraw) > 100000 and self.state.session_type == 'machine':
            self.print('Unable to withdraw, insufficient funds in terminal.')
        else:
            self.state.withdrawal_total += int(amount_to_withdraw)
            # Creates the transaction record for the withdrawal         
            self.transaction_manager.add(
                transaction_type='withdraw',
                recipient_account_number=account_number,
                amount=amount_to_withdraw
            )
            self.print('Withdrawal successful!')
