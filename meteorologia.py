from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
DADOS_CLIMA = {
    "lisboa": {"temp": "22ºC", "condicao":  "Sol"},
    "porto": {"temp":  "19º", "condicao": "nublado"},
    "estoril": {"temp": "12ºC", "condicao":  "ventania"},
    "faro": {"temp": "26ºC", "condicao":  "Sol"}}



class TelaClima(BoxLayout):
    resultado = StringProperty("insira uma cidade e carregue em pesquisar")

    def buscar_clima(self):
        cidade = self.ids.entrada.text.lower().strip()
        if cidade in DADOS_CLIMA:
           clima = DADOS_CLIMA[cidade]
           self.resultado = f"{cidade.title}: {clima['temp']} - {clima['condicao']}"
        else:
            self.resultado = f"clima para '{cidade.title()} ' não encontrado."

class ClimaApp(App):
    def build(self):
        return TelaClima()

ClimaApp().run()