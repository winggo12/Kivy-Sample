from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior


class MyButton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(MyButton, self).__init__(**kwargs)
        self.source = 'run_off.jpg'
        self.size_hint_x = 0.4
        self.width = 50
        self.height = 50
        self.allow_stretch = True

    def on_press(self):
        self.source = 'run_on.jpg'
        self.size_hint_x = 0.4
        self.width = 50
        self.height = 50
        self.allow_stretch = True

    def on_release(self):
        self.source = 'run_off.jpg'
        self.size_hint_x = 0.4
        self.width = 50
        self.height = 50
        self.allow_stretch = True

class SampleApp(App):
    def build(self):
        return MyButton()


SampleApp().run()