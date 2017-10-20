class Transaction:

    def __init__(
        self,
        transaction_type,
        recipient_account_number='0000000',
        amount='000',
        sender_account_number='0000000',
        account_name='***'
    ):
        createacct = 'createacct'
        deleteacct = 'deleteacct'
        deposit = 'deposit'
        logout = 'logout'
        transfer = 'transfer'
        withdraw = 'withdraw'

        valid_transaction_types = {
            createacct: 'NEW',
            deleteacct: 'DEL',
            deposit: 'DEP',
            logout: 'EOS',
            transfer: 'XFR',
            withdraw: 'WDR'
        }

        if transaction_type not in valid_transaction_types:
            raise LookupError('Not a valid transaction type')

        if transaction_type is createacct or transaction_type is deleteacct:
            if recipient_account_number is '0000000' or account_name is '***':
                raise ValueError('Invalid account number or name')
            amount = '000'
            sender_account_number = '0000000'
        if transaction_type is deposit or transaction_type is withdraw:
            if recipient_account_number is '0000000' or account_name is '***' or amount is '000':
                raise ValueError('Invalid account number or name or amount')
            sender_account_number = '0000000'
        if transaction_type is transfer:
            if recipient_account_number is '0000000' \
                    or account_name is '***' \
                    or amount is '000' \
                    or sender_account_number is '0000000':
                raise ValueError('Invalid account number or name or amount')
        if transaction_type is logout:
            recipient_account_number = '0000000'
            amount = '000'
            sender_account_number = '0000000'
            account_name = '***'

        # Ensure amount is always at least 3 digits in length
        if 0 < int(amount) < 10:
            amount = '00' + amount
        elif 10 <= int(amount) < 100:
            amount = '0' + amount

        self.transaction_code = valid_transaction_types[transaction_type]
        self.recipient_account_number = recipient_account_number
        self.amount = amount
        self.sender_account_number = sender_account_number
        self.account_name = account_name

    def __str__(self):
        transaction_code = self.transaction_code
        recipient_account_number = self.recipient_account_number
        amount = self.amount
        sender_account_number = self.sender_account_number
        account_name = self.account_name
        return transaction_code + \
            ' ' + recipient_account_number + \
            ' ' + amount + \
            ' ' + sender_account_number + \
            ' ' + account_name