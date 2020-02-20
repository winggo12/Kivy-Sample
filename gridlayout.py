from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
#from buttonmadafker import MyButton



def callback(instance):
    btn1.source = 'run_off.jpg'

class GridLayoutDemo(App):
    def build(self):
        layout = GridLayout(cols=2, rows=3)
        btn1 = Button(text='Hello1')
        layout.add_widget(btn1)
        btn1.bind(on_press=callback)

        layout.add_widget(Button(text='World 1'))
        layout.add_widget(Button(text='Hello 2'))
        layout.add_widget(Button(text='World 2'))
        layout.add_widget(Button(text='Hello 3'))
        layout.add_widget(Button(text='World 3'))

        return layout

if __name__ == '__main__':
    GridLayoutDemo().run()