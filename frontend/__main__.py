from .qbasic import Qbasic
from sys import argv


def main():
    valid_accounts_file = argv[1]
    qbasic = Qbasic(valid_accounts_file)
    qbasic.terminal()
    # qbasic.file() <-- Use this for testing


main()
