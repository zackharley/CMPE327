from backend.backend import Backend
from backend.test_harness import TestHarness


def main():
    backend = Backend()
    if True:  # If test mode
        test_harness = TestHarness()
        test_harness.test_transaction("createacct", "1234567", name="Rick")
        test_harness.test_transaction("ggg", "1234567", name="Rick")
        test_harness.test_transaction("deposit", "1234567", name="Rick")
        test_harness.test_transaction("createacct", "0000000", name="Rick")
        test_harness.test_transaction("withdraw", "1234567", amount=1000)
    else:
        backend.run()


main()
