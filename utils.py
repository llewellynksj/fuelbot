import os

# Imports for Font and color
from pyfiglet import Figlet
from termcolor import colored

import time

# Global variables
title = Figlet(font="slant")


class Vehicle:
    """
    Creates the Vehicle class where vehicle objects will be added
    """
    def __init__(self, nickname, vehicle_type, make, model, fuel_type):
        self.nickname = nickname
        self.vehicle_type = vehicle_type
        self.make = make
        self.model = model
        self.fuel_type = fuel_type

    def confirmation(self):
        """
        Method that confirms the vehicle details are saved
        """
        print(f"{self.make} {self.model}: Nickname {self.nickname} saved")


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
    Creates a delay before the next
    """
    time.sleep(1.5)


def create_car_object():
    """
    
    """