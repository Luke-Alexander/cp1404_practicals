names = ["Luke", "Kyle", "Michael", "Ted", "Wade Wilson"]

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class MileConverter(App):
    def build(self):
        self.title = "Dynamic labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        return self.root

    def create_labels(self):
        for name in names:
            temp_label = Label(text=name)
            self.root.ids.dynamic_box.add_widget(temp_label)

MileConverter().run()



