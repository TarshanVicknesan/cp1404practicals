from unreliable_car import UnreliableCar


def main():
    """Test the behavior of UnreliableCars."""

    # Create UnreliableCar instances with varying reliability
    reliable_car = UnreliableCar("Reliable", 100, 80)
    unreliable_car = UnreliableCar("Unreliable", 100, 20)

    # Perform multiple driving attempts and display results
    for i in range(1, 12):
        print(f"Driving attempt {i} km:")
        print(f"{reliable_car.name} drove {reliable_car.drive(i)} km")
        print(f"{unreliable_car.name} drove {unreliable_car.drive(i)} km")

    # Display the final state of the cars
    print(reliable_car)
    print(unreliable_car)


main()
