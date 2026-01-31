import MultiQuiz
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty, ListProperty,OptionProperty, ObjectProperty
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.recycleview import RecycleView

Quizes = [
    {"Título": "Quiz 1","Descrição": "Quiz sobre Python", "detalhes": "Detalhes completos da notícia 1..."},
    {"Título": "Quiz 2","Descrição": "Quiz sobre HTML", "detalhes": "Detalhes completos da notícia 2..."},
    {"Título": "Quiz 3","Descrição": "Quiz sobre Java", "detalhes": "Detalhes completos da notícia 3..."},
    {"Título": "Quiz 4","Descrição": "Quiz sobre Ethical hacking", "detalhes": "Detalhes completos da notícia 4..."}
]
class TelaPrincipal(Screen):
    lista = ObjectProperty(None)

    def on_enter(self):
        Clock.schedule_once(lambda dt: self.carregar())


    def carregar(self):
        self.lista.data = []
        for item in Quizes:
            Quiz = {
                "text": f"{item["Título"]}\n{item['Descrição']}",
                "on_release": lambda x=item: self.abrir_detalhes(x)
            }
            self.lista.data.append(Quiz)

            def abrir_detalhes(self, noticia):
                tela_detalhes = self.manager.get_screen('detalhes')
                tela_detalhes.atualizar_conteudo(noticia)
                self.manager.current = 'detalhes'

class TelaDetalhes(Screen):
    titulo = ObjectProperty(None)
    descricao = ObjectProperty(None)

    def atualizar(self, noticia):
            self.titulo.text = noticia['título']
            self.descrição.text = noticia['detalhes']

class ListaQuizes(RecycleView): pass

class Gerenciador(ScreenManager): pass

class NoticiasApp(App):
    def build(self): return Gerenciador()

MultiQuiz.App().run()