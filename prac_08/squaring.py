from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class SquareNumberApp(App):
    """App for squaring a user-provided number."""

    def build(self):
        """Set up the app window and load the KV file."""
        Window.size = (200, 100)
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        """Square the input value and display the result."""
        try:
            result = int(value) ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = "Invalid input"


SquareNumberApp().run()