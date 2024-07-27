from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    def build(self):
        """Build the app and add labels to the layout."""
        self.root = Builder.load_file('dynamic_labels.kv')
        names = ["Alice", "Bob", "Charlie", "David", "Eve"]
        main_layout = self.root.ids.main
        for name in names:
            label = Label(text=name, font_size=24)
            main_layout.add_widget(label)
        return self.root


DynamicLabelsApp().run()
