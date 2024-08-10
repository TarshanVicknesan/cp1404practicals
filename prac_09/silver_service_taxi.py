"""
CP1404 Practical - silver_service_taxi.py
"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """A SilverServiceTaxi with flagfall."""

    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise SilverServiceTaxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return string with flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Calculate fare with flagfall."""
        return self.flagfall + super().get_fare()
