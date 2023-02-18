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


def main():
    """
    Prints the programme logo to the terminal
    Prints welcome message
    """
    print(colored(title.renderText("F u e l B o t"), 'cyan'))
    print("Welcome to this fuel cost analysis programme\n")
    print("\nABOUT\n")
    print("Register an account & add your car details")
    print("Log your fuel costs to view insights and trends\n")
    print("Shall we get started? (Press Enter)")


main()
