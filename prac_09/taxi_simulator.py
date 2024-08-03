"""
CP1404 Practical - taxi_simulator.py
"""

from prac_06.car import Car
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Simulate taxi rides using Taxi and SilverServiceTaxi classes."""
    total_bill = 0
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    current_taxi = None

    print("Let's drive!")
    print(MENU)
    menu_choice = input(">>> ").lower()

    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available:")
            display_taxis(taxis)
            try:
                taxi_choice = int(input("Choose taxi: "))
                current_taxi = taxis[taxi_choice]
            except (IndexError, ValueError):
                print("Invalid taxi choice")
        elif menu_choice == "d":
            if current_taxi:
                current_taxi.start_fare()
                try:
                    distance_to_drive = float(input("Drive how far? "))
                    current_taxi.drive(distance_to_drive)
                    trip_cost = current_taxi.get_fare()
                    print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                    total_bill += trip_cost
                except ValueError:
                    print("Invalid input; please enter a number")
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")
        print(MENU)
        menu_choice = input(">>> ").lower()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display a list of taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def run_tests():
    """Run tests to demonstrate Car, Taxi, and SilverServiceTaxi classes."""
    bus = Car("Datsun", 180)
    bus.drive(30)
    print(f"fuel = {bus.fuel}, odo = {bus._odometer}")
    bus.drive(55)
    print(f"fuel = {bus.fuel}, odo = {bus._odometer}")
    print(bus)

    distance = int(input("Drive how far? "))
    while distance > 0:
        distance_travelled = bus.drive(distance)
        print(f"{bus} travelled {distance_travelled}")
        distance = int(input("Drive how far? "))

    t = Taxi("Prius 1", 100)
    t.drive(25)
    print(f"{t}, fare = {t.get_fare()}")
    t.start_fare()
    t.drive(40)
    print(f"{t}, fare = {t.get_fare()}")

    sst = SilverServiceTaxi("Limo", 100, 2)
    print(f"{sst}, fare = {sst.get_fare()}")
    sst.drive(10)
    print(f"{sst}, fare = {sst.get_fare()}")


main()
# Uncomment the following line to run tests
# run_tests()
