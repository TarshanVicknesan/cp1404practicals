from random import randint
from car import Car  # Assuming 'Car' class is in the same directory as this code.


class UnreliableCar(Car):
    """A variation of a car with random reliability."""

    def __init__(self, car_name, fuel_level, reliability_percent):
        """Initialize an UnreliableCar instance."""
        super().__init__(car_name, fuel_level)
        self.reliability_percent = reliability_percent

    def drive(self, distance_km):
        """Simulate a car drive with a chance of reliability failure."""
        random_chance = randint(1, 100)
        if random_chance >= self.reliability_percent:
            distance_km = 0
        distance_driven = super().drive(distance_km)
        return distance_driven
