# Functions that carry out validation checks
import utils
import gsheets


def user_quits(user_input):
    """
    Checks if the user has input 'q' to quit
    Returns the user to the first menu
    """
    if user_input == "q":
        utils.print_colour("Quitting....please wait...", "magenta")
        return True
    return False


def check_username(username):
    """
    Data validation of the username input by the user
    Checks the string is a minimum of 6 characters
    Checks the username does not match any other usernames already logged
    Returns False if validation is not valid
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
    Checks password
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
    Checks the users inputted username and password
    matches the saved information in the worksheet
    """
    usernames_list = gsheets.logins.col_values(1)
    # passwords_list = gsheets.logins.col_values(2)
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


def check_login_choice(choice):
    """
    Validates the users input from the login menu
    Triggers the relevant function
    """
    try:
        if int(choice) > 4 or int(choice) < 1:
            raise ValueError(
                "Please enter a number between 1 and 4"
            )
    except ValueError:
        print("Invalid data. Please enter a number between 1 and 4")
        return False
   
    return True
