from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty, ListProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label

#dados do quiz
perguntas = [
    {
        "pergunta":"Qual a capital de Portugal?",
        "respostas": ["Lisboa","Porto","Madrid"],
        "correta": "Lisboa"
    },
    {
        "pergunta":"Qual o Menor País do Mundo?",
        "respostas": ["Afeganistão","Angola","Vaticano"],
        "correta": "Vaticano"
    },
    {
        "pergunta":"Quantos Países tem como lingua oficial o Português?",
        "respostas": ["5","12","9"],
        "correta": "9"
    }
]

class QuizLayout(BoxLayout):
    pergunta_texto = StringProperty("")
    opcoes = ListProperty([])
    pontuacao = NumericProperty(0)
    index = NumericProperty(0)

    def on_kv_post(self, base_widget):
        self.carregar_proxima()

    def carregar_proxima(self):
        if self.index < len(perguntas):
            pergunta_atual = perguntas[self.index]
            self.pergunta_texto = pergunta_atual["pergunta"]
            self.opcoes = pergunta_atual["respostas"]

        else:
            self.pergunta_texto = "Fim do Quiz!"
            self.opcoes = []
            self.ids.resposta1.disabled = True
            self.ids.resposta2.disabled = True
            self.ids.resposta3.disabled = True

    def responder(self,resposta_escolhida):
        correta = perguntas[self.index]["correta"]
        if resposta_escolhida == correta:
            self.pontuacao += 1
            self.mostrar_popup("Certo!", "resposta correta!")
        else:
            self.mostrar_popup("Errado", f"A resposta correta era:{correta}")

        self.index += 1
        self.carregar_proxima()

    def mostrar_popup(self,titulo,mensagem):
        popup = Popup(title=titulo,
                      content=Label(text=mensagem),
                       size_hint=(None,None), size=(300,200))
        popup.open()
class QuizApp(App):
    def build(self):
        return QuizLayout()

QuizApp().run()