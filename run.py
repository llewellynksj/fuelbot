import utils
import checks
import gsheets

USER_ID = None


class Vehicle:
    """
    Creates the Vehicle class where vehicle objects will be added
    """
    def __init__(self, vehicle_type, make, model, fuel_type):
        self.vehicle_type = vehicle_type
        self.make = make
        self.model = model
        self.fuel_type = fuel_type


def add_fuel(vehicle_choice):
    """
    Adds a fuel entry to the vehicle
    """
    global USER_ID
    utils.print_colour(utils.title.renderText("A d d  F u e l"), "white")
    entry_date = input("Please enter the date (dd/mm/yy): ")
    odometer = input("\nEnter your odometer reading: ")
    litres_in = input("Enter the number of litres in: ")
    cost_per_litre = input("Enter the cost per litre : £")
    fuel_entry = [
        USER_ID,
        entry_date,
        vehicle_choice,
        odometer,
        litres_in,
        cost_per_litre
        ]
    gsheets.fuel_sheet.append_row(fuel_entry)
    utils.print_colour("Updating....", "magenta")
    utils.delay()
    utils.print_colour("Success! Your fuel entry has been added", "magenta")
    utils.delay()
    vehicle_account_menu(vehicle_choice)


def vehicle_account_menu(vehicle_choice):
    """
    Displays vehicle account menu choices to user
    Gets selection choice from user
    """
    utils.new_terminal()
    utils.print_colour(utils.title.renderText("M e n u"), "white")
    utils.print_colour(f"{vehicle_choice}", "cyan")
    while True:
        utils.print_colour(
            """Please select one:
            1. Add Fuel
            2. Add Expenses
            3. View previous entries
            4. View Insights
            """, "cyan")
        utils.print_colour("Enter q to quit", "magenta")
        features_choice = input("Enter the number of your selection: ")
        if checks.user_quits(features_choice):
            display_login_options()
        break

    if checks.check_choice(features_choice):
        if int(features_choice) == 1:
            add_fuel(vehicle_choice)
        elif int(features_choice) == 2:
            print("number 2)")
        elif int(features_choice) == 3:
            print("number 3")
        else:
            print("choice 4")


def check_vehicle_cell(username, vehicle_choice):
    """
    Takes the parameter of the users vehicle choice
    and checks it against the value of the cell in the worksheet
    """
    if vehicle_choice is None:
        add_vehicle(username)
    else:
        vehicle_account_menu(vehicle_choice)
    return True


def add_vehicle(username):
    """
    Requests details from user to build vehicle object
    """
    utils.new_terminal()
    utils.print_colour(utils.title.renderText("A d d"), "white")
    nickname = input("\nPlease enter a nickname for this vehicle: ")
    vehicle_type = input("What is your vehicle type (e.g. Car/Motorbike): ")
    make = input("What is the make of your vehicle: ")
    model = input("What is the model of your vehicle: ")
    fuel_type = input("What is the Fuel type (Petrol or Diesel): ")

    utils.print_colour("\nPlease check the below details are correct", "cyan")
    print(f"""\n
        Nickname: {nickname}
        Vehicle Type: {vehicle_type}
        Vehicle Make: {make}
        Vehicle Model: {model}
        Fuel Type: {fuel_type}
        """)
    while True:
        is_correct = input("\nEnter 'y' for yes or 'n' to start again: ")
        if checks.check_input(is_correct):
            break
    if is_correct == "y":
        utils.print_colour("Great!", "cyan")
        gsheets.update_worksheet_vehicle(username, nickname)
        nickname = Vehicle(vehicle_type, make, model, fuel_type)
        return nickname
    elif is_correct == 'n':
        utils.print_colour("Okay let's try again...", "magenta")
        add_vehicle(username)


def display_vehicle_menu(username, vehicle1, vehicle2, vehicle3):
    """
    menu
    """
    utils.new_terminal()
    utils.print_colour(utils.title.renderText("V e h i c l e s"), "white")
    utils.print_colour(f"Account details for {username}", "cyan")
    utils.print_colour(
        f"""\nYour Vehicles:
        1. {vehicle1}
        2. {vehicle2}
        3. {vehicle3}
        """, "cyan")
    while True:
        utils.print_colour(
            "If you would like to add a vehicle please select an empty slot"
            "\nYou can add up to 3 vehicles"
            "\nPress q to quit", "magenta")
        vehicle_choice = input("\nEnter the number of your selection: ")
        if checks.user_quits(vehicle_choice):
            display_login_options()
        elif int(vehicle_choice) == 1:
            if check_vehicle_cell(username, vehicle1):
                break
        elif int(vehicle_choice) == 2:
            if check_vehicle_cell(username, vehicle2):
                break
        elif int(vehicle_choice) == 3:
            if check_vehicle_cell(username, vehicle3):
                break
        else:
            print("Try again. Please select a number between 1 and 3.")


def user_login():
    """
    Login
    """
    global USER_ID
    utils.new_terminal()
    utils.print_colour(utils.title.renderText("L o g i n"), "white")
    while True:
        utils.print_colour(
            "Enter your username and password below"
            "\nPress q to quit and go back to the menu\n", "cyan")
        username = input("Enter your username: \n")
        USER_ID = username
        password = input("\nEnter your password: \n")
        utils.print_colour("Searching....please wait...", "magenta")
        utils.delay()
        if checks.user_quits(username):
            display_login_options()
        elif checks.user_quits(password):
            display_login_options()
        elif checks.check_login_details(username, password):
            break

    current_user = gsheets.logins.find(username)
    vehicle1 = gsheets.logins.cell(current_user.row, current_user.col+2).value
    vehicle2 = gsheets.logins.cell(current_user.row, current_user.col+3).value
    vehicle3 = gsheets.logins.cell(current_user.row, current_user.col+4).value
    display_vehicle_menu(username, vehicle1, vehicle2, vehicle3)


def create_account():
    """
    Requests a username and password from the user
    Checks if the username and password are valid
    If validation returns true, displays confirmation to user
    """
    utils.new_terminal()
    utils.print_colour(utils.title.renderText("S i g n  U p"), "white")
    while True:
        utils.print_colour(
            """Please choose a USERNAME that:
            - has a minimum of 6 characters
            - is unique
        """, "magenta")
        utils.print_colour("Hit q to quit and return to the menu\n", "magenta")
        username = input("Enter a unique username: \n")
        if checks.user_quits(username):
            display_login_options()
        elif checks.check_username(username):
            break
    utils.print_colour(f"\nYour username is confirmed: {username}\n", "cyan")

    while True:
        utils.print_colour(
            """Please choose a PASSWORD that:
            - has a minimum of 6 characters
            - contains at least 1 number
        """, "magenta")
        utils.print_colour("Hit q to quit and return to the menu\n", "magenta")
        password = input("Enter your password: \n")
        if checks.user_quits(password):
            display_login_options()
        elif checks.check_password(password):
            break
    utils.print_colour(f"\nYour password is confirmed: {password}\n", "cyan")

    gsheets.update_worksheet_logins(username, password)
    input("Press Enter to Login")
    user_login()


def display_about():
    """
    Displays the 'about' information to the user
    Returns user to the login menu when they hit Enter
    """
    utils.new_terminal()
    utils.print_colour(utils.title.renderText("A b o u t"), "white")
    utils.print_colour(
        "FuelBot is an analysis tool for tracking your spend on fuel."
        "\nYou can add fuel costs as and when you fill up your car."
        "\nYou will be able to view insights such as your average spend"
        "\nover the week or month, your average mpg, and trends in "
        "fuel prices.\n", "cyan")

    utils.print_colour(
        "Start by adding your car details (you can add more than 1 vehicle),"
        "\nand then each time you fill up your car you should add a fuel "
        "\nentry. This will record your odometer reading, the litres you've "
        "\ntopped up and the cost."
        "\nYou'll then be able to view your insights! This should help "
        "\nyou to budget and manage your costs.\n", "cyan")
    input("Press Enter to return to the menu")
    display_login_options()


def display_login_options():
    """
    Displays options to user to login or create account
    """
    utils.new_terminal()
    utils.print_colour(utils.title.renderText("M e n u"), "white")
    while True:
        utils.print_colour(
            """Select from the below options:
            1. Login
            2. Create Account
            3. About
            4. Quit
        """, "cyan")
        user_login_choice = input("Enter the number of your selection: ")
        break

    if checks.check_choice(user_login_choice):
        if int(user_login_choice) == 1:
            user_login()
        elif int(user_login_choice) == 2:
            create_account()
        elif int(user_login_choice) == 3:
            display_about()
        else:
            main()


def main():
    """
    Prints the programme logo to the terminal
    Prints welcome message
    """
    utils.print_colour(utils.title.renderText("F u e l B o t"), "white")
    utils.print_colour("""Welcome to your Fuel Cost Analysis programme
                \nRegister an account & add your car details
                \nLog your fuel costs to view insights & trends\n""", "cyan")
    input("\nShall we get started? Hit Enter to continue")
    display_login_options()


main()
