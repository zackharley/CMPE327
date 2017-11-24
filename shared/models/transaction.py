# This class is the way to ensure that new transaction records are formatted properly and validated
# The constructor handles validation
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

        valid_transaction_codes = valid_transaction_types.values()

        if transaction_type not in valid_transaction_types and transaction_type not in valid_transaction_codes:
            raise LookupError('Not a valid transaction type: {}'.format(transaction_type))

        if transaction_type is (createacct or valid_transaction_types[createacct] or deleteacct or valid_transaction_types[deleteacct]):
            if recipient_account_number is '0000000':
                raise ValueError('Invalid account number')
            amount = '000'
            sender_account_number = '0000000'
        if transaction_type is (deposit or valid_transaction_types[deposit] or withdraw or valid_transaction_types[withdraw]):
            print(amount, recipient_account_number)
            if recipient_account_number is '0000000' or amount is '000':
                raise ValueError('Invalid account number or amount')
            sender_account_number = '0000000'
        if transaction_type is (transfer or valid_transaction_types[transfer]):
            if recipient_account_number is '0000000' \
                    or amount is '000' \
                    or sender_account_number is '0000000':
                raise ValueError('Invalid account number or amount')
        if transaction_type is (logout or valid_transaction_types[logout]):
            recipient_account_number = '0000000'
            amount = '000'
            sender_account_number = '0000000'
            account_name = '***'

        # Ensure amount is always at least 3 digits in length
        if 0 < int(amount) < 10:
            amount = '00' + amount
        elif 10 <= int(amount) < 100:
            amount = '0' + amount

        if transaction_type in valid_transaction_types:
            self.transaction_code = valid_transaction_types[transaction_type]
        elif transaction_type in valid_transaction_codes:
            self.transaction_code = transaction_type
        self.recipient_account_number = recipient_account_number
        self.amount = amount
        self.sender_account_number = sender_account_number
        self.account_name = account_name

    # Format transaction string: CCC AAAA MMMM BBBB NNNN
    def __str__(self):
        transaction_code = self.transaction_code
        recipient_account_number = self.recipient_account_number
        amount = self.amount
        sender_account_number = self.sender_account_number
        account_name = self.account_name
        return '{} {} {} {} {}'.format(
            transaction_code,
            recipient_account_number,
            amount,
            sender_account_number,
            account_name
        )

    def get_transaction_code(self):
        return self.transaction_code

    def get_recipient_account_number(self):
        return self.recipient_account_number

    def get_amount(self):
        return self.amount

    def get_sender_account_number(self):
        return self.sender_account_number

    def get_account_name(self):
        return self.account_name
