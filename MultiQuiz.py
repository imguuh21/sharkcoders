import MultiQuiz
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.recycleview import RecycleView


Quizes = [
    {"Título": "Quiz 1","Descrição": "Quiz sobre Python", "detalhes": "Detalhes completos da notícia 1..."},
    {"Título": "Quiz 2","Descrição": "Quiz sobre HTML", "detalhes": "Detalhes completos da notícia 2..."},
    {"Título": "Quiz 3","Descrição": "Quiz sobre Java", "detalhes": "Detalhes completos da notícia 3..."},
    {"Título": "Quiz 4","Descrição": "Quiz sobre Ethical hacking", "detalhes": "Detalhes completos da notícia 4..."}
]

pergunta_quiz_1 = ({{
    "pergunta":"Quem foi o Criador do Python?",
    "respostas":["Bill Gates","Elon Musk","Guido Van Rossum"],
    "correta": "Guido Van Rossum"
},{
    "pergunta":"Qual ano Guido Van Rossum criou Python?",
    "respostas":""
}
})

class TelaPrincipal(Screen):
    lista = ObjectProperty(None)

    def on_enter(self):
        Clock.schedule_once(lambda dt: self.carregar())


    def carregar(self):
        self.ids.lista_quizes.data = [
            {
                "text": f"{item['Título']}\n{item['Descrição']}",
                "on_release": lambda x=item: self.abrir_detalhes(x)
            } for item in Quizes
        ]

    def abrir_detalhes(self, item):
          tela_detalhes = self.manager.get_screen('detalhes')
          tela_detalhes.atualizar_conteudo
          self.manager_current = 'detalhes'

class TelaDetalhes(Screen):
    def atualizar_conteudo(self, item):
            self.ids.text = item['título']
            self.ids.text = item['detalhes']

class ListaQuizes(RecycleView):
    pass

class Gerenciador(ScreenManager):
    pass

class Multiquiz(App):
    def build(self):
        return Gerenciador()
if __name__ == "__main__":
    MultiQuiz.App().run()