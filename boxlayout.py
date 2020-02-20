from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image

class BoxLayoutDemo(App):

  def callback(instance):
    print('pressed')

  def build(self):
    layout = GridLayout(cols=2, rows=3)
    Btn1 = layout.add_widget(Button(text='132kV Interlock'))

    Btn2 = layout.add_widget(Button(text='400kV Interlock'))

    Btn3 = layout.add_widget(Button(text='Air Compressor'))

    Btn4 = layout.add_widget(Button(text='Delay Auto Reclose'))

    Btn5 = layout.add_widget(Button(text='Transformer Parallel'))

    Btn6 = layout.add_widget(Button(text='Generator Synchronization'))

    return layout
