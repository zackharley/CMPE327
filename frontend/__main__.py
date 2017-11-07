from frontend.frontend import Frontend
from sys import argv


def main():
    valid_accounts_file = argv[1]
    transaction_summary_file = argv[2]
    frontend = Frontend(valid_accounts_file)
    if transaction_summary_file:
        frontend.file(transaction_summary_file)
    else:
        frontend.terminal()


main()
