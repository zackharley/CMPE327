from backend.backend import Backend
from backend.test_harness import TestHarness


def main():
    backend = Backend()
    if True: # If test mode
        test_harness = TestHarness()
        test_harness.create_account("1234567", "Rick")
    else:
        backend.run()


main()
