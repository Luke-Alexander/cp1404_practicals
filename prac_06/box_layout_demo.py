from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def clear(self):
        self.root.ids.input_box.text = ""

    def handle_greet(self):
        self.root.ids.display_box.text = "Hello {}".format(self.root.ids.input_box.text)



BoxLayoutDemo().run()
