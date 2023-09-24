from silver_service_taxi import SilverServiceTaxi


def main():
    my_silver_taxi = SilverServiceTaxi("Hummer", 200, 4)
    my_silver_taxi.drive(18)
    print(my_silver_taxi)
    print(f"Fare: ${my_silver_taxi.get_fare():.2f}")


main()
