# Import for clearing the terminal
import os

# Import for using delay function
import time

from statistics import mean

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
