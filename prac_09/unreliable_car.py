"""
CP1404 Practical - unreliable_car.py
"""

from random import randint
from prac_09.car import Car


class UnreliableCar(Car):
    """A car that is unreliable."""

    def __init__(self, name, fuel, reliability):
        """Initialise UnreliableCar."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive based on reliability."""
        if randint(1, 100) >= self.reliability:
            distance = 0
        return super().drive(distance)
