import os

# Imports to work with Google Sheets
import gspread
from google.oauth2.service_account import Credentials

# Imports for Font and color
from pyfiglet import Figlet
from termcolor import colored


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('fuelbot')

# Variables for spreadsheet worksheets
logins = SHEET.worksheet("logins")

# Global variables
title = Figlet(font="slant")


def print_colour(text, colour):
    """
    Using the termcolour import, prints text with the selected colour.
    """
    print(colored(text, colour))


def new_terminal():
    """
    Clears the current terminal and displays a new blank screen
    """
    # code taken from:
    # https://stackoverflow.com/questions/2084508/clear-terminal-in-python
    os.system('cls' if os.name == 'nt' else 'clear')


def create_account():
    """
    create account
    """
    print_colour(title.renderText("S i g n  U p"), "white")
    while True:
        print_colour(
            """Please choose a username that:
            - has a minimum of 6 characters
            - is unique
        """, "magenta")
        print_colour("Type q to quit and return to the menu", "magenta")
        username = input("Enter a unique username: ")
        if user_quits(username):
            display_login_options()
        elif check_username(username):
            break

    print_colour(f"Your username is {username}", "cyan")


def user_quits(user_input):
    """
    Checks if the user has input 'q' to quit
    Returns the user to the first menu
    """
    if user_input == "q":
        print_colour("Quitting....please wait...", "magenta")


def check_username(username):
    """
    Data validation of the username input by the user
    Checks the string is a minimum of 6 characters
    Checks the username does not match any other usernames already logged
    """
    


def display_about():
    """
    Displays the 'about' information to the user
    Returns user to the login menu when they hit Enter
    """
    print_colour(title.renderText("A b o u t"), "white")
    print_colour(
        "FuelBot is an analysis tool for tracking your spend on fuel."
        "\nYou can add fuel costs as and when you fill up your car."
        "\nYou will be able to view insights such as your average spend"
        "\nover the week or month, your average mpg, and trends in "
        "fuel prices.\n", "cyan")

    print_colour(
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
    new_terminal()
    print_colour(title.renderText("M e n u"), "white")
    print_colour(
        """Select from the below options:
        1. Login
        2. Create Account
        3. About
    """, "cyan")


def main():
    """
    Prints the programme logo to the terminal
    Prints welcome message
    """
    print_colour(title.renderText("F u e l B o t"), "white")
    print_colour("""Welcome to your Fuel Cost Analysis programme
                \nRegister an account & add your car details
                \nLog your fuel costs to view insights & trends\n""", "cyan")
    input("\nShall we get started? Hit Enter to continue")
    display_login_options()


display_about()
