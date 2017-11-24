from backend.backend import Backend
from backend.test_harness import TestHarness

TEST_CASES = [
    {"transaction_type": "createacct", "account_number": "1234567", "name": "Rick"},
    {"transaction_type": "ggg", "account_number": "1234567", "name": "Rick"},
    {"transaction_type": "deposit", "account_number": "1234567", "name": "Rick"},
    {"transaction_type": "createacct", "account_number": "0000000", "name": "Rick"},
    {"transaction_type": "withdraw", "account_number": "1234567", "amount": "1000"},
    {"transaction_type": "jhskdjh", "account_number": "1234567", "amount": "1000"},
    {"transaction_type": "withdraw", "account_number": "0000000", "amount": "1000"},
    {"transaction_type": "withdraw", "account_number": "1234567", "amount": "9"},
    {"transaction_type": "withdraw", "account_number": "1234567", "amount": "99"}
]


def main():
    backend = Backend()
    if True:  # If test mode
        test_harness = TestHarness()
        for test in TEST_CASES:
            test_harness.test_transaction(**test)

    else:
        backend.run()


main()
