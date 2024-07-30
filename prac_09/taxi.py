"""
CP1404 Practical
"""

from prac_09.car import Car


class Taxi(Car):
    """Specialised Car with fare costs."""

    price_per_km = 1.23

    def __init__(self, name, fuel):
        """Initialise Taxi with name and fuel."""
        super().__init__(name, fuel)
        self.current_fare_distance = 0

    def __str__(self):
        """Return string with fare details."""
        return f"{super().__str__()}, {self.current_fare_distance}km on current fare, ${self.price_per_km:.2f}/km"

    def get_fare(self):
        """Calculate fare."""
        return round(self.price_per_km * self.current_fare_distance, 1)

    def start_fare(self):
        """Reset fare distance."""
        self.current_fare_distance = 0

    def drive(self, distance):
        """Drive and update fare distance."""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven
