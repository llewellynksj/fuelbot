"""
Main script that runs all main functions
Defines class
"""
from rich.console import Console
from rich.table import Table

import utils
import checks
import gsheets

USER_ID = None
CURRENT_USER = None
VEHICLE1 = None
VEHICLE2 = None
VEHICLE3 = None


class Vehicle:
    """
    Creates the Vehicle class where vehicle objects will be added
    """
    def __init__(self, vehicle_type, make, model, fuel_type):
        self.vehicle_type = vehicle_type
        self.make = make
        self.model = model
        self.fuel_type = fuel_type


def main():
    """
    Prints the logo to the terminal and welcome message
    Triggers the function to display login options
    """
    utils.print_colour(utils.title.renderText("F u e l B o t"), "white")
    utils.print_colour("""Welcome to your Fuel Cost Analysis programme
                \nRegister an account & add your car details
                \nLog your fuel costs to view insights & trends\n""", "cyan")
    input("\nShall we get started? Hit Enter to continue")
    display_login_options()


def display_login_options():
    """
    Displays options to user to login or create account
    Takes user input and triggers relevant function
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

    if checks.check_number_input(user_login_choice):
        if int(user_login_choice) == 1:
            user_login()
        elif int(user_login_choice) == 2:
            create_account()
        elif int(user_login_choice) == 3:
            display_about()
        else:
            main()


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
        "Start by adding your car details (you can add up to 3 vehicles),"
        "\nand then each time you fill up your car you should add a fuel "
        "\nentry. This will record your odometer reading, the litres you've "
        "\ntopped up and the cost."
        "\nYou'll then be able to view your insights! This should help "
        "\nyou to budget and manage your costs.\n", "cyan")
    input("Press Enter to return to the menu")
    display_login_options()


def create_account():
    """
    Requests a username and password from the user
    Checks if the username and password are valid
    If validation returns true, displays confirmation to user
    and triggers function to update logins worksheet
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

    gsheets.update_worksheet_new_user(username, password)
    input("Press Enter to Login")
    user_login()


def user_login():
    """
    Requests user login and password
    Validates inputs and checks data against saved account
    information in logins worksheet.
    Triggers function to display saved vehicles on users account.
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

    display_users_vehicles(USER_ID)


def display_users_vehicles(username):
    """
    Retrieves the value of the users saved vehicles from the worksheet
    Displays vehicle names and requests a selection from the user
    """
    global VEHICLE1
    global VEHICLE2
    global VEHICLE3
    current_user = gsheets.logins.find(username)
    VEHICLE1 = gsheets.logins.cell(current_user.row, current_user.col+2).value
    VEHICLE2 = gsheets.logins.cell(current_user.row, current_user.col+3).value
    VEHICLE3 = gsheets.logins.cell(current_user.row, current_user.col+4).value
    utils.new_terminal()
    utils.print_colour(utils.title.renderText("V e h i c l e s"), "white")
    utils.print_colour(f"Account details for {username}", "cyan")
    utils.print_colour(
        f"""\nYour Vehicles:
        1. {VEHICLE1}
        2. {VEHICLE2}
        3. {VEHICLE3}
        """, "cyan")
    while True:
        utils.print_colour(
            "To ADD a vehicle please select an empty slot"
            "\nYou can add up to 3 vehicles"
            "\nPress q to quit", "magenta")
        vehicle_choice = input("\nEnter the number of your selection: ")
        if checks.user_quits(vehicle_choice):
            display_login_options()
        elif int(vehicle_choice) < 4 and int(vehicle_choice) > 0:
            if lookup_vehicle_cell(username, vehicle_choice):
                break
        else:
            print("Try again. Please select a number between 1 and 3.")


def lookup_vehicle_cell(username, vehicle_choice):
    """
    Takes the parameter of the users vehicle choice and checks
    it against the value of the cell in the worksheet.
    Triggers relevant function based on value of cell

    """
    if int(vehicle_choice) == 1:
        if VEHICLE1 == "Empty":
            add_vehicle(username, 2)
        else:
            vehicle_account_menu(VEHICLE1)
    if int(vehicle_choice) == 2:
        if VEHICLE2 == "Empty":
            add_vehicle(username, 3)
        else:
            vehicle_account_menu(VEHICLE2)
    if int(vehicle_choice) == 3:
        if VEHICLE3 == "Empty":
            add_vehicle(username, 4)
        else:
            vehicle_account_menu(VEHICLE3)
    else:
        return False


def add_vehicle(username, col_step):
    """
    Requests car details from user
    Updates login worksheet with new vehicle nickname
    Builds new object from Vehicle class
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
        if checks.check_yes_no_input(is_correct):
            break
    if is_correct == "y":
        utils.print_colour("Great!", "cyan")
        gsheets.update_worksheet_vehicle(username, col_step, nickname)
        nickname = Vehicle(vehicle_type, make, model, fuel_type)
        display_users_vehicles(username)
    elif is_correct == 'n':
        utils.print_colour("Okay let's try again...", "magenta")
        add_vehicle(username, col_step)


def vehicle_account_menu(vehicle_choice):
    """
    Displays vehicle account menu choices to user
    Retrieves input selection from user and triggers relevant
    function.
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
        if checks.check_number_input(features_choice):
            if int(features_choice) == 1:
                check_first_entry(vehicle_choice)
            elif int(features_choice) == 2:
                add_expenses(vehicle_choice)
            elif int(features_choice) == 3:
                display_previous_entries(vehicle_choice)
            else:
                display_insights(vehicle_choice)
                break


def check_first_entry(vehicle_choice):
    """
    Checks with the user if this is the first fuel entry
    If yes, then triggers add_first_fuel function to get initial details
    and will not calculate an mpg
    If no, then triggers add_fuel which includes calc_mpg function
    """
    utils.print_colour(
        "\nIs this the first fuel entry for this vehicle?", "magenta"
        )
    while True:
        first_entry_choice = input("Enter 'y' or 'n': ")
        if checks.check_yes_no_input(first_entry_choice):
            break
    if first_entry_choice == "y":
        add_first_fuel(vehicle_choice)
    else:
        add_fuel(vehicle_choice)


def add_first_fuel(vehicle_choice):
    """
    Adds a fuel entry to the vehicle but excludes calculating
    the mpg as this is the first entry
    Updates fuel worksheet with entry
    """
    utils.print_colour(utils.title.renderText("+F u e l"), "white")
    utils.print_colour("\nIs this fuel entry for today?", "cyan")
    date_response = input("Enter 'y' for yes or 'n' for no: ")
    if date_response == "y":
        utils.print_colour(
            f"\nThanks. Todays date, {utils.get_today()}, is saved", "cyan")
        entry_date = utils.get_today()
    elif date_response == "n":
        entry_date = utils.get_entry_date()
    odometer = input("\nEnter your odometer reading: ")
    litres_in = float(input("Enter the number of litres in: "))
    cost_per_litre = float(input("Enter the cost per litre: £"))
    fuel_entry = [
        USER_ID,
        entry_date,
        vehicle_choice,
        odometer,
        litres_in,
        cost_per_litre
    ]
    gsheets.final_fuel_sheet.append_row(fuel_entry)
    utils.print_colour("Updating....", "magenta")
    utils.delay()
    utils.print_colour("Success! Your fuel entry has been added", "magenta")
    utils.print_colour(f"Going back to {vehicle_choice}'s Menu...", "magenta")
    utils.delay()
    vehicle_account_menu(vehicle_choice)


def add_fuel(vehicle_choice):
    """
    Adds a fuel entry to the vehicle
    Updates fuel worksheet with entry
    """
    utils.print_colour(utils.title.renderText("+F u e l"), "white")
    utils.print_colour("\nIs this fuel entry for today?", "cyan")
    date_response = input("Enter 'y' for yes or 'n' for no: ")
    if date_response == "y":
        utils.print_colour(
            f"\nThanks. Todays date, {utils.get_today()}, is saved", "cyan")
        entry_date = utils.get_today()
    elif date_response == "n":
        entry_date = utils.get_entry_date()
    current_odometer = input("Enter your odometer reading: ")
    litres_in = float(input("Enter the number of litres in: "))
    cost_per_litre = float(input("Enter the cost per litre: £"))
    fuel_entry = [
        USER_ID,
        entry_date,
        vehicle_choice,
        current_odometer,
        litres_in,
        cost_per_litre
    ]
    gsheets.fuel_sheet.append_row(fuel_entry)
    utils.print_colour("Updating....", "magenta")
    utils.delay()
    prev_odometer = gsheets.find_prev_odometer(current_odometer)
    mpg = utils.calc_mpg(int(current_odometer), int(prev_odometer), litres_in)
    fuel_entry.append(mpg)
    gsheets.final_fuel_sheet.append_row(fuel_entry)
    utils.print_colour("Success! Your fuel entry has been added", "magenta")
    utils.print_colour(f"Going back to {vehicle_choice}'s Menu...", "magenta")
    utils.delay()
    vehicle_account_menu(vehicle_choice)


def add_expenses(vehicle_choice):
    """
    Adds an expenses entry to the vehicle
    Updates expenses worksheet with entry
    """
    utils.print_colour(utils.title.renderText("+E X P E N S E S"), "white")
    entry_date = input("Please enter the date (dd/mm/yy): ")
    description = input("Enter a short description of the expense: ")
    expense_cost = input("Enter the total cost: £")
    expense_entry = [
        USER_ID,
        entry_date,
        vehicle_choice,
        description,
        expense_cost
    ]
    gsheets.expenses_sheet.append_row(expense_entry)
    utils.print_colour("Updating...", "magenta")
    utils.delay()
    utils.print_colour("Success! Your expense entry has been added", "magenta")
    utils.print_colour(f"Going back to {vehicle_choice}'s Menu...", "magenta")
    utils.delay()
    vehicle_account_menu(vehicle_choice)


def display_previous_entries(vehicle_choice):
    """
    Displays records attached to vehicle
    """
    utils.print_colour(utils.title.renderText("R E C O R D S"), "white")
    table = Table(title=f"{vehicle_choice} Records", header_style="dark_red")
    previous_entries = gsheets.get_all_records(vehicle_choice)

    table.add_column("Username", style="chartreuse4")
    table.add_column("Date", style="chartreuse4")
    table.add_column("Vehicle", style="chartreuse4")
    table.add_column("Odometer", style="chartreuse4")
    table.add_column("Litres in", style="chartreuse4")
    table.add_column("£ per litre", style="chartreuse4")
    table.add_column("MPG", style="chartreuse4")

    for entry in previous_entries:
        table.add_row(
            entry[0], entry[1], entry[2], entry[3],
            entry[4], entry[5], entry[6]
            )

    console = Console()
    console.print(table)

    input("Hit Enter to return to the menu")
    vehicle_account_menu(vehicle_choice)


def display_insights(vehicle_choice):
    """
    Displays insights on current records
    """
    utils.print_colour(utils.title.renderText("I N S I G H T S"), "white")
    utils.print_colour(
            """Please select one:
            1. Average Consumption
            2. Fuel Cost Trends
            3. Expenses Overview
            4. Quit
            """, "cyan")
    insights_choice = input("Enter the number of your selection: ")
    if checks.user_quits(insights_choice):
        display_login_options()
    if checks.check_number_input(insights_choice):
        if int(insights_choice) == 1:
            display_averages_all(vehicle_choice)
        elif int(insights_choice) == 2:
            calc_fuel_trends(vehicle_choice)
        elif int(insights_choice) == 3:
            calc_expense_trends(vehicle_choice)
        else:
            print("choice 4")


def display_averages_all(vehicle_choice):
    """
    Calculate averages
    """
    # Find average mpg
    mpg_full_list = utils.get_full_list(vehicle_choice, 6)
    average_mpg = utils.calc_average(mpg_full_list)
    # Find average cost per litre
    litre_cost_full_list = utils.get_full_list(vehicle_choice, 5)
    average_cost_litre = float(utils.calc_average(litre_cost_full_list))
    # Find average cost per week / day
    date_list = utils.get_dates(vehicle_choice)
    days = utils.get_days(date_list)
    weeks = days // 7
    total_spend = utils.calc_total_spend(vehicle_choice)

    average_cost_week = float(total_spend / weeks)
    average_cost_day = float(total_spend / days)

    average_weekly = "£" + str(average_cost_week)
    average_daily = "£" + str(average_cost_day)

    # Display table
    table = Table(title=f"{vehicle_choice} Averages", header_style="dark_red")
    # Table columns
    table.add_column("Average", style="chartreuse4")
    table.add_column("Fuel", style="chartreuse4")
    # Table rows
    table.add_row("MPG", str(average_mpg), "N/A")
    table.add_row("£ per litre", str(average_cost_litre))
    table.add_row("£ per month", str(average_mpg))
    table.add_row("£ per week", average_weekly)
    table.add_row("£ per day", average_daily)

    console = Console()
    console.print(table)

    input("Hit Enter to return to the menu")
    display_insights(vehicle_choice)


def calc_fuel_trends(vehicle_choice):
    """
    Calculate fuel trends
    """
    print("Calculate fuel trends")


def calc_expense_trends(vehicle_choice):
    """
    Calculate expense trends
    """
    table = Table(title=f"{vehicle_choice} Averages", header_style="dark_red")
    # Table columns
    table.add_column("Average", style="chartreuse4")
    table.add_column("Expenses", style="chartreuse4")
    # Table rows
    table.add_row("£ per month", )
    table.add_row("£ per week", )
    table.add_row("£ per day", )


main()
