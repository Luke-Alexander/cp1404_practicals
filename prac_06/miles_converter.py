from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934


class MileConverter(App):
    def build(self):
        self.title = "Mile Converter"
        self.root = Builder.load_file('miles_converter.kv')
        return self.root

    def convert(self):
        kms = self.input_value()
        result = kms * MILES_TO_KM
        self.root.ids.output_label.text = "{} kilometres".format(str(result))

    def handle_increment(self, increment):
        self.root.ids.mile_input.text = str(self.input_value() + increment)

    def input_value(self):
        try:
            miles = float(self.root.ids.mile_input.text)
            return miles
        except ValueError:
            return 0

MileConverter().run()