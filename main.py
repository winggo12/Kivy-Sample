from kivy.app import App

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.button import Button

from kivy.uix.image import Image
# Boxlayout is the App class

def callback(instance):
  print('The button <%s> is being pressed' % instance.text)

class BoxLayoutDemo(App):

  def build(self):
    superBox = BoxLayout(orientation='vertical')

    horizontalBox = BoxLayout(orientation='horizontal')

    button1 = Image(source='b1.jpg')

    button2 = Button(text='Hello world 1')
    button2.bind(on_press=callback)

    horizontalBox.add_widget(button1)

    horizontalBox.add_widget(button2)

    verticalBox = BoxLayout(orientation='vertical')

    button3 = Button(text="Three")

    button4 = Button(text="Four")

    verticalBox.add_widget(button3)

    verticalBox.add_widget(button4)

    superBox.add_widget(horizontalBox)

    superBox.add_widget(verticalBox)

    return superBox


  #button2.bind(state=callback)
# Instantiate and run the kivy app

if __name__ == '__main__':
  BoxLayoutDemo().run()

