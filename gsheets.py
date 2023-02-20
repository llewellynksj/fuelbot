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


def update_worksheet_logins(username, password):
    """
    Saves the username and password to google sheets
    """
    user_data = [username, password]
    utils.print_colour("Saving account information...\n", "cyan")
    logins.append_row(user_data)


def update_worksheet_vehicle(username, vehicle_nickname):
    """
    Saves the vehicle variable name (nickname) to the worksheet
    alongside the username and password
    """
    utils.print_colour("Saving vehicle to your account...\n", "cyan")
    utils.delay()
    current_user = logins.find(username)
    current_user_row = current_user.row
    current_user_col = current_user.col
    logins.update_cell(current_user_row, current_user_col+2, vehicle_nickname)
    
