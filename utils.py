# Imports
import os
import time
import re
from statistics import mean
from datetime import date
from datetime import datetime
from pyfiglet import Figlet
from termcolor import colored
from dateutil import relativedelta

# Local imports
import gsheets

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
    # https://bit.ly/3IVzcOk
    os.system('cls' if os.name == 'nt' else 'clear')


def delay():
    """
    Creates a delay before executing next code
    """
    time.sleep(1.5)


def get_today():
    """
    Gets todays date
    """
    todays_date = date.today()
    print_today = todays_date.strftime('%d/%m/%y')
    return print_today


def get_entry_date():
    """
    Requests date of fuel entry from user
    Returns date as the entry_date to be saved
    """
    while True:
        entry_date = input("Enter the date of this fuel entry (dd/mm/yy): ")
        # code to match the date taken from:
        # https://bit.ly/3kqGLD0
        match_date = re.match(
            r"^[0-3][0-9]['/'][0-1][0-9]['/'][1-2][0-9]$", entry_date
            )
        is_matched = bool(match_date)
        if is_matched is False:
            raise ValueError(
                "Invalid date format. Please try again using format dd/mm/yy"
                )
        else:
            break
        if is_matched is True:
            return str(entry_date)


def calc_mpg(current_odometer, prev_odometer, litres_in):
    """
    Calculates the mpg figure for fuel entry
    """
    mpg = ((float(current_odometer)
            - float(prev_odometer)) / litres_in) * 4.544
    return round(mpg, 2)


def get_list(vehicle_choice, list_index):
    """
    Gets totals from the worksheet and saves them in a list
    to be used in calculations for insights
    """
    vehicle_list = gsheets.get_all_records(gsheets.fuel_sheet, vehicle_choice)
    subject = [i[list_index] for i in vehicle_list]
    try:
        subject.remove("")
        subject = [float(i) for i in subject]
        return subject
    except ValueError:
        subject = [float(i) for i in subject]
        return subject


def calc_average(subject_list):
    """
    Takes the subjects totals list as a parameter and returns
    the average
    """
    average = mean(subject_list)
    return round(average, 2)


def calc_total_spend(vehicle_choice):
    """
    Calculates the total spend
    """
    vehicle_list = gsheets.get_all_records(gsheets.fuel_sheet, vehicle_choice)
    result = [float(i[5]) * float(i[4]) for i in vehicle_list]
    total_spend = sum(result)
    return total_spend


def get_dates(worksheet, vehicle_choice):
    """
    Retrieves dates from worksheet and converts to datetime objects
    Returns a list of datetime objects
    """
    vehicle_list = gsheets.get_all_records(worksheet, vehicle_choice)
    subject = [i[1] for i in vehicle_list]
    date_list = []
    for date_item in subject:
        date_list.append(datetime.strptime(date_item, "%d/%m/%y"))
    return date_list


def get_days(date_list):
    """
    Calculates number of days using the datetime object list
    """
    earliest_date = min(date_list)
    latest_date = max(date_list)
    # code from:
    # https://bit.ly/3xPI9Cr
    days = abs(earliest_date - latest_date).days
    return days


def get_months(date_list):
    """
    Calculates number of months using the datetime object list
    and relativedelta import
    """
    earliest_date = min(date_list)
    latest_date = max(date_list)
    # code from
    # https://bit.ly/3m0zBFX
    delta = relativedelta.relativedelta(latest_date, earliest_date)
    months = delta.months
    return months
