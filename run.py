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


def print_login_options():
    """
    Displays options to user to login or create account
    """
    new_terminal()
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
    print_colour("""Welcome to your Fuel Cost Analysis programme\n
                \nRegister an account & add your car details
                \nLog your fuel costs to view insights & trends\n""", "cyan")
    input("\nShall we get started? Hit Enter to continue")
    print_login_options()


main()
