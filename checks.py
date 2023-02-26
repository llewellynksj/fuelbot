# Local imports
import utils
import gsheets


def user_quits(user_input):
    """
    Checks if the user has input 'q' to quit
    """
    if user_input == "q":
        utils.print_colour("Quitting....please wait...", "magenta")
        utils.delay()
        return True
    return False


def check_number_input(choice, max_num):
    """
    Validates the users input is between 1 and 4
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
    if user_input == "y" or user_input == "n":
        return True
    else:
        print("Something went wrong. Please enter y or no.")
        return False


def check_username(username):
    """
    Data validation of the username input by the user
    Checks the string is a minimum of 6 characters
    Checks the username does not match any other usernames already logged
    """
    usernames = gsheets.logins.col_values(1)

    username_length = len(username)

    if username_length < 6:
        utils.print_colour("Please enter at least 6 characters", "grey")
        return False
    elif username in usernames:
        utils.print_colour("Not available. Please try something else", "grey")
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
        utils.print_colour("You forgot to include a number! Try again", "grey")
        return False
    if password_length < 6:
        utils.print_colour("That's too short! Try again", "grey")
        return False
    return True


def check_login_details(username, password):
    """
    Checks the users inputted username and password matches
    the saved information in the worksheet.
    """
    usernames_list = gsheets.logins.col_values(1)
    users_dict = gsheets.logins.get_all_records()
    current_user = next(
        (x for x in users_dict if x['username'] == username)
    )
    if username not in usernames_list:
        utils.print_colour("Username not found. Try again\n", "grey")
        return False
    stored_password = current_user.get("password")
    if password == stored_password:
        utils.print_colour("User account found. Please wait...\n", "cyan")
    else:
        utils.print_colour("Password incorrect. Try again\n", "grey")
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
        utils.print_colour("Not available. Please try something else", "grey")
        return False
    return True
