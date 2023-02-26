# Imports
from rich.console import Console
from rich.table import Table

# Local imports
import utils
import checks
import gsheets

# Global variables
user_id = None
vehicle1 = None
vehicle2 = None
vehicle3 = None


class Vehicle:
    """
    Creates the Vehicle class where vehicle objects will be added
    """
    def __init__(self, vehicle_type, make, model, fuel_type):
        self.vehicle_type = vehicle_type
        self.make = make
        self.model = model
        self.fuel_type = fuel_type

    def __str__(self):
        return f"This {self.vehicle_type} is a {self.make} {self.model}"


def main():
    """
    Entry point; prints logo and welcome message
    """
    utils.new_terminal()
    utils.print_colour(utils.title.renderText("F u e l B o t"), "white")
    utils.print_colour("""Welcome to your Fuel Cost Analysis programme
                \nRegister an account & add your car details
                \nLog your fuel costs to view insights & trends\n""", "cyan")
    input("\nShall we get started? Hit Enter to continue")
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
        if checks.check_number_input(user_login_choice, 4):
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
    Checks inputs are valid
    """
    utils.new_terminal()
    utils.print_colour(utils.title.renderText("S i g n  U p"), "white")
    # Request username and validate:
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
    # Request password and validate:
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
    # Update worksheet:
    gsheets.update_worksheet_new_user(username, password)
    input("Press Enter to Login")
    user_login()


def user_login():
    """
    Requests user login and password
    Validates inputs and checks data against worksheet
    """
    global user_id
    utils.new_terminal()
    utils.print_colour(utils.title.renderText("L o g i n"), "white")
    while True:
        utils.print_colour(
            "Enter your username and password below"
            "\nPress q to quit and go back to the menu\n", "cyan")
        username = input("Enter your username: \n")
        user_id = username
        if checks.user_quits(username):
            display_login_options()
        password = input("\nEnter your password: \n")
        if checks.user_quits(password):
            display_login_options()
        utils.print_colour("Searching....please wait...", "magenta")
        utils.delay()
        if checks.check_login_details(username, password):
            break
    display_users_vehicles(user_id)


def display_users_vehicles(username):
    """
    Retrieves the value of the users saved vehicles from the worksheet
    Displays vehicle names and requests a selection from the user
    """
    global vehicle1
    global vehicle2
    global vehicle3
    current_user = gsheets.logins.find(username)
    vehicle1 = gsheets.logins.cell(current_user.row, current_user.col+2).value
    vehicle2 = gsheets.logins.cell(current_user.row, current_user.col+3).value
    vehicle3 = gsheets.logins.cell(current_user.row, current_user.col+4).value
    utils.new_terminal()
    utils.print_colour(utils.title.renderText("V e h i c l e s"), "white")
    utils.print_colour(f"Account details for {username}", "cyan")
    utils.print_colour(
        f"""\nYour Vehicles:
        1. {vehicle1}
        2. {vehicle2}
        3. {vehicle3}
        """, "cyan")
    utils.print_colour(
        "To ADD a vehicle please select an empty slot"
        "\nYou can add up to 3 vehicles"
        "\nPress q to quit", "magenta")
    while True:
        vehicle_choice = input("\nEnter the number of your selection: ")
        if checks.user_quits(vehicle_choice):
            display_login_options()
        elif checks.check_number_input(vehicle_choice, 3):
            lookup_vehicle_cell(username, vehicle_choice)
            break


def lookup_vehicle_cell(username, vehicle_choice):
    """
    Takes the parameter of the users vehicle choice and checks
    it against the value of the cell in the worksheet.
    """
    if int(vehicle_choice) == 1:
        if vehicle1 == "Empty":
            add_vehicle(username, 2)
        else:
            vehicle_account_menu(vehicle1)
    if int(vehicle_choice) == 2:
        if vehicle2 == "Empty":
            add_vehicle(username, 3)
        else:
            vehicle_account_menu(vehicle2)
    if int(vehicle_choice) == 3:
        if vehicle3 == "Empty":
            add_vehicle(username, 4)
        else:
            vehicle_account_menu(vehicle3)
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

    while True:
        utils.print_colour(
            "Please choose a NICKNAME for your vehicle that is UNIQUE", "cyan")
        nickname = input("\nEnter a nickname for this vehicle: ")
        utils.print_colour("Checking database, please wait...", "magenta")
        utils.delay()
        if checks.user_quits(username):
            display_login_options()
        elif checks.check_nickname(nickname):
            break

    utils.print_colour(
        f"\nVehicle's nickname is confirmed: {nickname}\n", "cyan")
    vehicle_type = input("What is your vehicle type (e.g. Car/Motorbike): ")
    make = input("What is the make of your vehicle: ")
    model = input("What is the model of your vehicle: ")
    fuel_type = input("What is the Fuel type (Petrol or Diesel): ")
    utils.new_terminal()
    # Checks the user inputs are correct:
    utils.print_colour("\nPlease check the below details are correct", "cyan")
    print(f"""
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
    if is_correct.lower() == "y" or is_correct.lower() == "yes":
        utils.print_colour("Great!", "cyan")
        gsheets.update_worksheet_vehicle(username, col_step, nickname)
        nickname = Vehicle(vehicle_type, make, model, fuel_type)
        display_users_vehicles(username)
    elif is_correct.lower() == 'n' or is_correct.lower() == "no":
        utils.print_colour("Okay let's try again...", "magenta")
        add_vehicle(username, col_step)


def vehicle_account_menu(vehicle_choice):
    """
    Displays vehicle account menu choices to user
    Retrieves input selection
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
            display_users_vehicles(user_id)
        if checks.check_number_input(features_choice, 4):
            if int(features_choice) == 1:
                add_fuel(vehicle_choice)
            elif int(features_choice) == 2:
                add_expenses(vehicle_choice)
            elif int(features_choice) == 3:
                display_records_menu(vehicle_choice)
            else:
                display_insights_menu(vehicle_choice)
                break


def add_fuel(vehicle_choice):
    """
    Adds a fuel entry to the vehicle
    Updates fuel worksheet with entry
    """
    utils.new_terminal()
    utils.print_colour(utils.title.renderText("+F u e l"), "white")
    fuel_dict = {}
    utils.print_colour("\nIs this fuel entry for today?", "cyan")
    date_response = input("Enter 'y' for yes or 'n' for no: ")
    if date_response.lower() == "y" or date_response.lower() == "yes":
        utils.print_colour(
            f"\nTodays date, {utils.get_today()}, is saved", "cyan")
        fuel_dict['Date'] = utils.get_today()
    elif date_response == "n":
        fuel_dict['Date'] = utils.get_entry_date()
    fuel_dict['Odometer'] = input("Enter your odometer reading: ")
    fuel_dict['Litres'] = float(input("Enter the number of litres in: "))
    fuel_dict['Cost'] = float(input("Enter the cost per litre: £"))
    # Check for user to confirm details:
    if checks.user_conf(fuel_dict):
        utils.print_colour("Great! One more question...", "magenta")
    else:
        utils.print_colour("Okay let's try again...", "magenta")
        add_fuel(vehicle_choice)
    # Create list with user inputs:
    fuel_entry = [
        user_id,
        fuel_dict['Date'],
        vehicle_choice,
        fuel_dict['Odometer'],
        fuel_dict['Litres'],
        fuel_dict['Cost']
    ]
    # Check if this is the first fuel entry
    # If not first entry calculate mpg:
    utils.print_colour(
        "Is this the FIRST fuel entry for this vehicle?"
        "\nPlease note if you select 'y' mpg stats will be reset", "magenta")
    while True:
        first_input = input("Enter 'y' or 'n': ")
        if checks.check_yes_no_input(first_input):
            if first_input.lower() == "y" or first_input.lower() == "yes":
                break
            elif first_input.lower() == "n" or first_input.lower() == "no":
                try:
                    prev_odometer = gsheets.find_prev_odometer(vehicle_choice)
                    mpg = utils.calc_mpg(
                        fuel_dict['Odometer'],
                        prev_odometer,
                        fuel_dict['Litres'])
                    fuel_entry.append(mpg)
                    break
                except IndexError:
                    utils.print_colour(
                        "Invalid! No other records are found for this vehicle."
                        "Please select 'y' as this is your first entry",
                        "magenta")
    # Add entry to worksheet:
    utils.print_colour("Updating....", "magenta")
    utils.delay()
    gsheets.fuel_sheet.append_row(fuel_entry)
    utils.print_colour("Success! Your fuel entry has been added", "magenta")
    utils.print_colour(f"Going back to {vehicle_choice}'s Menu...", "magenta")
    utils.delay()
    vehicle_account_menu(vehicle_choice)


def add_expenses(vehicle_choice):
    """
    Adds an expenses entry to the vehicle
    Updates expenses worksheet with entry
    """
    utils.new_terminal()
    utils.print_colour(utils.title.renderText("+E X P E N S E S"), "white")
    expenses = {}
    utils.print_colour("\nIs this expenses entry for today?", "cyan")
    date_response = input("Enter 'y' for yes or 'n' for no: ")
    if date_response.lower() == "y" or date_response.lower() == "yes":
        utils.print_colour(
            f"\nTodays date, {utils.get_today()}, is saved", "cyan")
        expenses['Date'] = utils.get_today()
    elif date_response == "n":
        expenses['Date'] = utils.get_entry_date()
    expenses['Description'] = input("Enter a short description: ")
    expenses['Cost'] = input("Enter the total cost: £")
    # Check for user to confirm details:
    if checks.user_conf(expenses):
        utils.print_colour("Great!", "cyan")
    else:
        utils.print_colour("Okay let's try again...", "magenta")
        add_expenses(vehicle_choice)
    # Create list with user inputs
    expense_entry = [
        user_id,
        expenses['Date'],
        vehicle_choice,
        expenses['Description'],
        expenses['Cost']
    ]
    gsheets.expenses_sheet.append_row(expense_entry)
    utils.print_colour("Updating...", "magenta")
    utils.delay()
    utils.print_colour("Success! Your expense entry has been added", "magenta")
    utils.print_colour(f"Going back to {vehicle_choice}'s Menu...", "magenta")
    utils.delay()
    vehicle_account_menu(vehicle_choice)


def display_records_menu(vehicle_choice):
    """
    Displays records options to user for specific vehicle
    """
    utils.new_terminal()
    utils.print_colour(utils.title.renderText("R E C O R D S"), "white")
    utils.print_colour(
            """Please select one:
            1. Fuel
            2. Expenses
            """, "cyan")
    utils.print_colour("Hit q to quit and return to the menu\n", "magenta")
    records_choice = input("Enter the number of your selection: ")
    if checks.user_quits(records_choice):
        vehicle_account_menu(vehicle_choice)
    if checks.check_number_input(records_choice, 2):
        if int(records_choice) == 1:
            display_fuel_records(vehicle_choice)
        elif int(records_choice) == 2:
            display_expense_records(vehicle_choice)


def display_fuel_records(vehicle_choice):
    """
    Retrieves all fuel records from the worksheet and displays
    them in a table
    """
    utils.new_terminal()
    utils.print_colour(utils.title.renderText("R E C O R D S"), "white")
    previous_entries = gsheets.get_all_records(
        gsheets.fuel_sheet, vehicle_choice)
    # Display table
    table = Table(
        title=f"{vehicle_choice} Fuel Records", header_style="magenta")

    table.add_column("Date", style="cyan1")
    table.add_column("Vehicle", style="cyan1")
    table.add_column("Odometer", style="cyan1")
    table.add_column("Litres in", style="cyan1")
    table.add_column("£ per litre", style="cyan1")
    table.add_column("MPG", style="cyan1")

    for entry in previous_entries:
        table.add_row(
            entry[1], entry[2], entry[3],
            entry[4], entry[5], entry[6])

    console = Console()
    console.print(table)

    input("Hit Enter to return to the menu")
    display_records_menu(vehicle_choice)


def display_expense_records(vehicle_choice):
    """
    Retrieves all expenses from the worksheet and displays
    them in a table
    """
    utils.new_terminal()
    utils.print_colour(utils.title.renderText("R E C O R D S"), "white")
    previous_entries = gsheets.get_all_records(
        gsheets.expenses_sheet, vehicle_choice)
    # Display table 
    table = Table(title=f"{vehicle_choice} Expense Records", header_style="magenta")

    table.add_column("Date", style="cyan1")
    table.add_column("Vehicle", style="cyan1")
    table.add_column("Description", style="cyan1")
    table.add_column("Cost £", style="cyan1")

    for entry in previous_entries:
        table.add_row(entry[1], entry[2], entry[3], entry[4])

    console = Console()
    console.print(table)

    input("Hit Enter to return to the menu")
    display_records_menu(vehicle_choice)


def display_insights_menu(vehicle_choice):
    """
    Displays insights on current records
    """
    utils.new_terminal()
    utils.print_colour(utils.title.renderText("I N S I G H T S"), "white")
    utils.print_colour(
            """Please select one:
            1. Fuel
            2. Expenses
            """, "cyan")
    utils.print_colour("Hit q to quit and return to the menu\n", "magenta")
    insights_choice = input("Enter the number of your selection: ")
    if checks.user_quits(insights_choice):
        vehicle_account_menu(vehicle_choice)
    if checks.check_number_input(insights_choice, 2):
        if int(insights_choice) == 1:
            display_fuel_insights(vehicle_choice)
        elif int(insights_choice) == 2:
            display_expense_insights(vehicle_choice)


def display_fuel_insights(vehicle_choice):
    """
    Calculate averages and displays to user in a table
    """
    utils.new_terminal()
    utils.print_colour(utils.title.renderText("I N S I G H T S"), "white")
    spend = utils.calc_total_spend(vehicle_choice)
    odometer_list = utils.get_list(vehicle_choice, 3)
    if len(odometer_list) < 2:
        utils.print_colour(
            "Oops something went wrong! You haven't entered enough data to be"
            "\nable to show stats. Try again.", "magenta")
        utils.delay()
        vehicle_account_menu(vehicle_choice)
    total_distance = utils.calc_distance(odometer_list)
    date_list = utils.get_dates(gsheets.fuel_sheet, vehicle_choice)
    days = utils.get_days(date_list)
    weeks = days // 7
    months = utils.get_months(date_list)

    avg_cost_month = round(spend / months, 2)
    avg_cost_week = round(spend / weeks, 2)
    avg_cost_day = round(spend / days, 2)
    avg_distance_month = round(total_distance / months, 2)
    avg_distance_week = round(total_distance / weeks, 2)
    avg_distance_day = round(total_distance / days, 2)

    averages = {
        'mpg': utils.calc_average(utils.get_list(vehicle_choice, 6)),
        'cost_litre': utils.calc_average(utils.get_list(vehicle_choice, 5)),
        'cost_day': "£" + str(avg_cost_day),
        'cost_week': "£" + str(avg_cost_week),
        'cost_month': "£" + str(avg_cost_month),
        'distance_day': str(avg_distance_day) + " miles",
        'distance_week': str(avg_distance_week) + " miles",
        'distance_month': str(avg_distance_month) + " miles"
    }

    # Display table
    table = Table(title=f"{vehicle_choice} Averages", header_style="magenta")
    table.add_column("", style="cyan1")
    table.add_column("Average", style="cyan1")
    table.add_row("MPG", str(averages["mpg"]))
    table.add_row("£ per litre", str(averages["cost_litre"]))
    table.add_row("£ per month", averages["cost_month"])
    table.add_row("£ per week", averages["cost_week"])
    table.add_row("£ per day", averages["cost_day"])
    table.add_row("Miles per month", averages["distance_month"])
    table.add_row("Miles per week", averages["distance_week"])
    table.add_row("Miles per day", averages["distance_day"])

    console = Console()
    console.print(table)

    utils.print_colour(
        "\nIf you see N/A, there is not currently enough data available",
        "magenta")
    input("Hit Enter to return to the menu")
    display_insights_menu(vehicle_choice)


def display_expense_insights(vehicle_choice):
    """
    Calculate averages and displays to user in a table
    """
    utils.new_terminal()
    utils.print_colour(utils.title.renderText("I N S I G H T S"), "white")
    cost_list = gsheets.expenses_sheet.col_values(5)
    cost_list.remove("cost")
    conv_cost_list = [float(x) for x in cost_list]
    spend = sum(conv_cost_list)

    date_list = utils.get_dates(gsheets.expenses_sheet, vehicle_choice)
    if len(date_list) < 2:
        utils.print_colour(
            "Oops something went wrong! You haven't entered enough data to be"
            "\nable to show stats. Try again.", "magenta")
        utils.delay()
        vehicle_account_menu(vehicle_choice)
    days = utils.get_days(date_list)
    weeks = days // 7
    months = utils.get_months(date_list)

    average_cost_month = round(spend / months, 2)
    average_cost_week = round(spend / weeks, 2)
    average_cost_day = round(spend / days, 2)

    expense_averages = {
        'per_day': "£" + str(average_cost_day),
        'per_week': "£" + str(average_cost_week),
        'per_month': "£" + str(average_cost_month)
    }

    # Display Table
    table = Table(title=f"{vehicle_choice} Averages", header_style="magenta")

    table.add_column("", style="cyan1")
    table.add_column("Average", style="cyan1")

    table.add_row("£ per month", expense_averages['per_month'])
    table.add_row("£ per week", expense_averages['per_week'])
    table.add_row("£ per day", expense_averages['per_day'])

    console = Console()
    console.print(table)

    utils.print_colour(
        "\nIf you see N/A, there is not currently enough data available",
        "magenta")
    view_records = input(
        "\nWould you like to see the full records of your expenses? (y/n): ")
    while True:
        if checks.check_yes_no_input(view_records):
            break
    if view_records.lower() == "y" or view_records.lower() == "yes":
        utils.print_colour("Great! Stand by...", "cyan")
        utils.delay()
        display_expense_records(vehicle_choice)
    elif view_records.lower() == 'n' or view_records.lower() == "no":
        utils.print_colour("Okay, let's go back to the menu...", "magenta")
        utils.delay()
        display_insights_menu(vehicle_choice)


main()
