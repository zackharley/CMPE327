from glob import glob
from shared.models.transaction import Transaction
from os import path, remove

EOS_LINE = 'EOS 0000000 000 0000000 ***'


class TransactionFileService:

    @staticmethod
    def get_transactions_from_directory(directory_path):
        file_paths = glob(path.join(directory_path, '*.txt'))
        file_lines = get_array_of_file_lines(file_paths)
        transactions = transform_transaction_file_lines_into_transactions(file_lines)
        delete_old_transaction_summaries(file_paths)
        return transactions


def get_array_of_file_lines(file_paths):
    all_file_lines = []
    for file_path in file_paths:
        file = open(file_path, 'r')
        file_lines = file.readlines()
        all_file_lines.extend(map(lambda line: line.rstrip('\n'), file_lines))
        file.close()
    return all_file_lines


def transform_transaction_file_lines_into_transactions(file_lines):
    transactions = []
    filtered_file_lines = filter(lambda line: line != EOS_LINE, file_lines)
    for file_line in filtered_file_lines:
        transaction_attributes = file_line.split(' ')
        transactions.append(Transaction(*transaction_attributes))
    eos_attributes = EOS_LINE.split(' ')
    transactions.append(Transaction(*eos_attributes))
    return transactions

def delete_old_transaction_summaries(file_paths):
    for file_path in file_paths:
        if path.isfile(file_path):
            remove(file_path)

    


