class CreateAcct:

    def createacct(self):
        has_account_number = False
        has_name = False
        account_number_prompt = "Please enter an account number for the new account: "
        name_prompt = "Enter a name to associate with the account: "

        while not has_account_number:
            account_number = input(account_number_prompt)
            has_account_number = is_valid_account_number(account_number)
            if not has_account_number:
                print("Invalid account number")
        while not has_name:
            name = input(name_prompt)
            has_name = is_valid_name(name)
            if not has_name:
                print('Invalid name')

        # add account to valid accounts file
        print('creating account ' + account_number + ' for ' + name)


def is_valid_account_number(account_number):
    valid_account_number_length = 7

    if len(account_number) != valid_account_number_length:
        return False
    elif account_number[0] == 0:
        return False
    # elif account number already exists
    #     return False
    else:
        return True

def is_valid_name(name):
    valid_name_min_length = 3
    valid_name_max_length = 30
    if len(name) < valid_name_min_length || len(name) > valid_name_max_length:
        return False
    elif name[0] == ' ' or name[-1] == ' ':
        return False
    # elif name match alphanumeric
    else:
        return True