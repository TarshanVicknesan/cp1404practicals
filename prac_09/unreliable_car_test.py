"""
CP1404 Practical - unreliable_car_test.py
"""

from prac_09.unreliable_car import UnreliableCar


def main():
    """Test UnreliableCar."""
    good_car = UnreliableCar("Mostly Good", 100, 90)
    bad_car = UnreliableCar("Dodgy", 100, 9)

    # attempt to drive the cars many times and output distances driven
    for i in range(1, 12):
        print(f"Attempting to drive {i}km:")
        print(f"{good_car.name:12} drove {good_car.drive(i):2}km")
        print(f"{bad_car.name:12} drove {bad_car.drive(i):2}km")

    print(good_car)
    print(bad_car)


main()
