from kivy.app import App
from kivy.lang import Builder


MILES_TO_KM = 1.60934


class ConvertMilesToKm(App):
    def build(self):
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_to_km.kv')
        return self.root

    def handle_increment(self, increment):
        self.root.ids.input_miles.text = str(int(self.root.ids.input_miles.text) + increment)
        if int(self.root.ids.input_miles.text) <= 0:
            self.root.ids.input_miles.text = "0"

    def handle_calculation(self):
        self.root.ids.output_kilometers.text = str(int(self.root.ids.input_miles.text) * MILES_TO_KM)


ConvertMilesToKm().run()
