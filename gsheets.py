import utils


# Imports to work with Google Sheets
import gspread
from google.oauth2.service_account import Credentials

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
usernames_list = logins.col_values(1)
passwords_list = logins.col_values(2)


def update_worksheet_logins(username, password):
    """
    Saves the username and password to google sheets
    """
    user_data = [username, password]

    utils.print_colour("Saving account information...\n", "cyan")
    logins.append_row(user_data)


def get_updated_worksheet():
    """
    Retrieves the most up-to-date version of the logins worksheet
    """
    print("hi")
