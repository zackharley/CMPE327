from frontend.frontend import Frontend
from sys import argv


def main():
    valid_accounts_file = argv[1]
    frontend = Frontend(valid_accounts_file)
    frontend.terminal()
    # frontend.file() <-- Use this for testing


main()
