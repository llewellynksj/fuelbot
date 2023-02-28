# Local imports
import utils
import constants
import gsheets


def user_quits(user_input):
    """
    Checks if the user has input 'q' to quit
    """
    if user_input.lower() == "q" or user_input.lower() == "quit":
        utils.print_colour("Quitting....please wait...", constants.COLOR2)
        utils.delay(1.5)
        return True
    return False


def check_number_input(choice, max_num):
    """
    Validates the users input is between 1 and a max_num(param)
    """
    try:
        if int(choice) > max_num or int(choice) < 1:
            raise ValueError(
                f"Please enter a number between 1 and {max_num}"
            )
    except ValueError:
        print(f"Invalid data. Please enter a number between 1 and {max_num}")
        return False

    return True


def check_yes_no_input(user_input):
    """
    Checks users input is equal to 'y' or 'n'
    """
    if user_input.lower() == "y" or user_input.lower() == "n":
        return True
    elif user_input.lower() == "yes" or user_input.lower() == "no":
        return True
    else:
        print("Something went wrong. Please enter y or no.")
        return False


def check_is_digits(input_list):
    """
    Checks users input is a number
    """
    return all(answer.isdigit() for answer in input_list)


def check_username(username):
    """
    Data validation of the username input by the user
    Checks the string is a minimum of 6 characters
    Checks the username does not match any other usernames already logged
    """
    usernames = gsheets.logins.col_values(1)

    username_length = len(username)

    if username_length < 6:
        utils.print_colour(
            "Please enter at least 6 characters", constants.COLOR3)
        return False
    elif username in usernames:
        utils.print_colour(
            "Not available. Please try something else", constants.COLOR3)
        return False
    else:
        return True


def check_password(password):
    """
    Checks password is correct format
    """
    password_length = len(password)
    # code for checking if password contains integer from:
    # https://www.geeksforgeeks.org/password-validation-in-python/
    if not any(char.isdigit() for char in password):
        utils.print_colour(
            "You forgot to include a number! Try again", constants.COLOR3)
        return False
    if password_length < 6:
        utils.print_colour("That's too short! Try again", constants.COLOR3)
        return False
    return True


def check_login_details(username, password):
    """
    Checks the users inputted username and password matches
    the saved information in the worksheet.
    """
    usernames_list = gsheets.logins.col_values(1)
    users_dict = gsheets.logins.get_all_records()
    if username not in usernames_list:
        utils.print_colour("Username not found. Try again\n", constants.COLOR3)
        return False
    current_user = next(
        (x for x in users_dict if x['username'] == username))
    stored_password = current_user.get("password")
    if password == stored_password:
        utils.print_colour(
            "User account found. Please wait...\n", constants.COLOR1)
    else:
        utils.print_colour("Password incorrect. Try again\n", constants.COLOR3)
        return False
    return True


def check_nickname(nickname):
    """
    Validates that the vehicle nickname is unique
    """
    nickname_list = []
    nickname_list.append(gsheets.logins.col_values(3))
    nickname_list.append(gsheets.logins.col_values(4))
    nickname_list.append(gsheets.logins.col_values(5))

    if nickname in (x for sublist in nickname_list for x in sublist):
        utils.print_colour(
            "Not available. Please try something else", constants.COLOR3)
        return False
    return True


def user_conf(dictionary):
    """
    Checks the inputs passed in by the user are correct
    If user has made an error they can start again
    """
    utils.new_terminal()
    utils.print_colour(
        "\nPlease check the below details are correct", constants.COLOR1)
    for x in dictionary:
        print(x, ": ", dictionary[x])
    while True:
        is_correct = input("\nEnter 'y' for yes or 'n' to start again: ")
        if check_yes_no_input(is_correct):
            break
    if is_correct.lower() == "y" or is_correct.lower() == "yes":
        return True
    return False
