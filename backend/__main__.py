from backend.backend import Backend
from backend.test_harness import TestHarness


def main():
    backend = Backend()
    if True: # If test mode
        test_harness = TestHarness()
        test_harness.test_create_account("createacct", "1234567", "Rick")
        #test_harness.test_create_account("ggg", "1234567", "Rick")
        #test_harness.test_create_account("deposit", "1234567", "Rick")
        #test_harness.test_create_account("createacct", "0000000", "Rick")



    else:
        backend.run()


main()
