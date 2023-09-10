from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """ MilesConverterApp is a Kivy App for converting miles to kilometres """

    def build(self):
        """ Build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def calculate_conversion(self):
        """ Perform the conversion calculation """
        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def update_miles(self, change):
        """
        Handle up/down button press to update miles and recalculate
        :param change: The amount to change
        """
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.calculate_conversion()

    def get_validated_miles(self):
        """
        Get the miles from the text input widget and convert to float
        :return: 0 if there's an error, otherwise the float value of the text input
        """
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesConverterApp().run()
