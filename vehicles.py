import utils
import checks
import gsheets


class Vehicle:
    """
    Creates the Vehicle class where vehicle objects will be added
    """
    def __init__(self, vehicle_type, make, model, fuel_type):
        self.vehicle_type = vehicle_type
        self.make = make
        self.model = model
        self.fuel_type = fuel_type


def add_vehicle(username):
    """
    Requests details from user to build vehicle object
    """
    nickname = input("Please enter a nickname for this vehicle: ")
    vehicle_type = input("What is your vehicle type (e.g. Car/Motorbike): ")
    make = input("What is the make of your vehicle: ")
    model = input("What is the model of your vehicle: ")
    fuel_type = input("What is the Fuel type (Petrol or Diesel): ")

    utils.print_colour("\nPlease check the below details are correct", "cyan")
    print(f"""\n
        Nickname: {nickname}
        Vehicle Type: {vehicle_type}
        Vehicle Make: {make}
        Vehicle Model: {model}
        Fuel Type: {fuel_type}
        """)
    while True:
        is_correct = input("\nEnter 'y' for yes or 'n' to start again: ")
        if checks.check_input(is_correct):
            break
    if is_correct == "y":
        utils.print_colour("Great!", "cyan")
        gsheets.update_worksheet_vehicle(username, nickname)
        nickname = Vehicle(vehicle_type, make, model, fuel_type)
        utils.delay()
        # display_user_menu(username)
    elif is_correct == 'n':
        utils.print_colour("Okay let's try again...", "magenta")
        add_vehicle(username)
