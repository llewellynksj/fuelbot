import os

# Imports for Font and color
from pyfiglet import Figlet
from termcolor import colored

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


def search_dict(search_element, name, dict_list):
    """
    Searched the list passed in as a parameter
    Returns result
    """
    return [x for x in dict_list if x[search_element] == name]
    