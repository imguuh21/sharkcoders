from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
class MyApp(App):
    def build(self):
        self.text_input = TextInput()

        layout = BoxLayout(orientation="vertical")
        layout.add_widget(Button(text='Botão 1'))
        layout.add_widget(Button(text="Botão 2"))
        return Label(text="Hello,Kivy")

MyApp().run()