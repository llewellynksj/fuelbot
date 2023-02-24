"""
Functions that rely mainly on access to the google worksheets
"""
# Imports to work with Google Sheets
import gspread
from google.oauth2.service_account import Credentials

import utils

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
fuel_sheet = SHEET.worksheet("add_fuel")
expenses_sheet = SHEET.worksheet("add_expenses")
final_fuel_sheet = SHEET.worksheet("complete_entry")


def update_worksheet_new_user(username, password):
    """
    Saves the username and password to google sheets
    """
    user_data = [username, password, "Empty", "Empty", "Empty"]
    utils.print_colour("Saving account information...\n", "cyan")
    logins.append_row(user_data)


def update_worksheet_vehicle(username, col_step, vehicle_nickname):
    """
    Saves the vehicle variable name (nickname) to the worksheet
    alongside the username and password
    """
    utils.print_colour("Saving vehicle to your account...\n", "cyan")
    utils.delay()
    current_user = logins.find(username)
    current_user_col = current_user.col + col_step
    logins.update_cell(current_user.row, current_user_col, vehicle_nickname)


def find_prev_odometer(current_odometer):
    """
    Uses the current odometer input to find and return the
    last odometer reading that was logged
    """
    location_current_odometer = fuel_sheet.find(current_odometer)
    prev_odometer = final_fuel_sheet.cell(
        location_current_odometer.row, location_current_odometer.col
        ).value
    return prev_odometer


def get_all_records(vehicle_choice):
    """
    Retrieves all previous entries for the selected vehicle
    name
    Returns a list
    """
    all_records = final_fuel_sheet.get_all_values()
    vehicle_records = [x for x in all_records if vehicle_choice in x]
    return vehicle_records
