# Import for clearing the terminal
import os

# Import for using delay function
import time

from statistics import mean
from datetime import date
import re

# Imports for Font and color
from pyfiglet import Figlet
from termcolor import colored

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
    # https://stackoverflow.com/questions/2084508/clear-terminal-in-python
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
        # https://www.adamsmith.haus/python/answers/how-to-check-if-a-string-matches-a-pattern-in-python
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
        return entry_date


def calc_mpg(current_odometer, prev_odometer, litres_in):
    """
    Calculates the mpg figure for fuel entry
    """
    mpg = ((float(current_odometer)
            - float(prev_odometer)) / litres_in) * 4.544
    return round(mpg, 2)


def get_totals(vehicle_choice, list_index):
    """
    Filetrs the worksheet by vehicle choice
    Gets totals from the worksheet and saves them in a list
    to be used in calculations for insights
    """
    all_list = gsheets.final_fuel_sheet.get_all_values()
    vehicle_list = [x for x in all_list if vehicle_choice in x]
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
    return average


def calc_total_spend():
    """
    Calculates the total spend 
    """
