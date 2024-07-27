from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """App to convert miles to kilometers."""

    def build(self):
        """Load the KV file."""
        self.title = "Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def convert_miles_to_km(self):
        """Convert miles to kilometers and display the result."""
        value = self.get_validated_miles()
        self.root.ids.output_label.text = str(value * MILES_TO_KM)

    def change_miles_value(self, change):
        """Update miles value and recalculate."""
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.convert_miles_to_km()

    def get_validated_miles(self):
        """Validate and return miles input."""
        try:
            return float(self.root.ids.input_miles.text)
        except ValueError:
            return 0


MilesConverterApp().run()
