from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.recycleview import RecycleView
from kivy.properties import OptionProperty, ObjectProperty
from kivy.clock import Clock

noticias = [
    {"Título": "Notícia 1","Descrição": "Descrição Curta da Noticia 1", "detalhes": "Detalhes completos da notícia 1..."},
    {"Título": "Notícia 2","Descrição": "Descrição Curta da Noticia 2", "detalhes": "Detalhes completos da notícia 2..."},
    {"Título": "Notícia 3","Descrição": "Descrição Curta da Noticia 3", "detalhes": "Detalhes completos da notícia 3..."},
    {"Título": "Notícia 4","Descrição": "Descrição Curta da Noticia 4", "detalhes": "Detalhes completos da notícia 4..."},
    {"Título": "Notícia 5","Descrição": "Descrição Curta da Noticia 5", "detalhes": "Detalhes completos da notícia 5..."},
    {"Título": "Notícia 6","Descrição": "Descrição Curta da Noticia 6", "detalhes": "Detalhes completos da notícia 6..."},
    {"Título": "Notícia 7","Descrição": "Descrição Curta da Noticia 7", "detalhes": "Detalhes completos da notícia 7..."},
    {"Título": "Notícia 8","Descrição": "Descrição Curta da Noticia 8", "detalhes": "Detalhes completos da notícia 8..."},
    {"Título": "Notícia 9","Descrição": "Descrição Curta da Noticia 9", "detalhes": "Detalhes completos da notícia 9..."}
]

class TelaPrincipal(Screen):
    lista = ObjectProperty(None)

    def on_enter(self):
        Clock.schedule_once(lambda dt: self.carregar())

    def carregar(self):
        self.lista.data = []
        for item in noticias:
            noticia = {
                "text": f"{item["título"]}\n{item['descrição']}",
                "on_release": lambda x=item: self.abrir_detalhes(x)
            }
            self.lista.data.append(noticia)

    def abrir_detalhes(self,noticia):
        tela_detalhes = self.manager.get_screen('detalhes')
        tela_detalhes.atualizar_conteudo(noticia)
        self.manager.current = 'detalhes'

class TelaDetalhes(Screen):
    titulo = ObjectProperty(None)
    descrição = ObjectProperty(None)

    def atualizar(self,noticia):
        self.titulo.text = noticia['título']
        self.descrição.text = noticia['detalhes']

class ListaNoticias(RecycleView): pass

class Gerenciador(ScreenManager): pass

class NoticiasApp(App):
    def build(self): return Gerenciador()

NoticiasApp().run()