from glob import glob
from shared.models.transaction import Transaction
from os import path, remove

EOS_LINE = 'EOS 0000000 000 0000000 ***'

'''
Responsible for reading and formatting Transaction Summary files for back-office use.
'''
class TransactionFileService:

    @staticmethod
	# Gets all transactions from a directory pointing to a file
    def get_transactions_from_directory(directory_path):
        file_paths = glob(path.join(directory_path, '*.txt'))
        file_lines = get_array_of_file_lines(file_paths)
        transactions = transform_transaction_file_lines_into_transactions(file_lines)
        delete_old_transaction_summaries(file_paths)
        return transactions

# Get an array of the lines within the file
def get_array_of_file_lines(file_paths):
    all_file_lines = []
    for file_path in file_paths:
        file = open(file_path, 'r')
        file_lines = file.readlines()
        all_file_lines.extend(map(lambda line: line.rstrip('\n'), file_lines))
        file.close()
    return all_file_lines

# Transforms the array of file lines into seperate transactions
def transform_transaction_file_lines_into_transactions(file_lines):
    transactions = []
    filtered_file_lines = filter(lambda line: line != EOS_LINE, file_lines)
    for file_line in filtered_file_lines:
        transaction_attributes = file_line.split(' ')
        transactions.append(Transaction(*transaction_attributes))
    eos_attributes = EOS_LINE.split(' ')
    transactions.append(Transaction(*eos_attributes))
    return transactions

# Deletes the old transaction summary files
def delete_old_transaction_summaries(file_paths):
    for file_path in file_paths:
        if path.isfile(file_path):
            remove(file_path)

    


