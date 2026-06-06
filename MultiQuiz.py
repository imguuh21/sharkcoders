from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty, ListProperty, NumericProperty
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.recycleview import RecycleView


Quizes = [
    {"Título": "Quiz 1","Descrição": "Quiz sobre Python", "detalhes": "Detalhes completos da notícia 1..."},
    {"Título": "Quiz 2","Descrição": "Quiz sobre HTML", "detalhes": "Detalhes completos da notícia 2..."},
    {"Título": "Quiz 3","Descrição": "Quiz sobre Java", "detalhes": "Detalhes completos da notícia 3..."},
    {"Título": "Quiz 4","Descrição": "Quiz sobre Ethical hacking", "detalhes": "Detalhes completos da notícia 4..."}
]

pergunta_quiz_1 = [
    {
        "pergunta": "Quem foi o Criador do Python?",
        "respostas": ["Bill Gates","Elon Musk","Guido Van Rossum"],
        "correta": "Guido Van Rossum"
    },
    {
        "pergunta": "Qual ano Guido Van Rossum criou o Python?",
        "respostas": ["1996","1999","1989"],
        "correta": "1989"
    },
    {
        "pergunta": "Onde Guido Van Rossum está a trabalhar?",
        "respostas": ["Apple","Microsoft","Sony"],
        "correta": "Microsoft"
    }
]
pergunta_quiz_2 = [
    {
        "pergunta": "Quem foi o Criador do java?",
        "respostas": ["yukihiro matsumoto","James Arthur Gosling","Guido Van Rossum"],
        "correta": "Guido Van Rossum"
    },
    {
        "pergunta": "Qual ano James criou o java?",
        "respostas": ["1991","1999","1989"],
        "correta": "1991"
    },
    {
        "pergunta": "Qual Universidade ele Estudou?",
        "respostas": ["Calgary","TUM","Oxford"],
        "correta": "Calgary"
    }
]
pergunta_quiz_3 = [
    {
        "pergunta": "Quem foi o Criador do java?",
        "respostas": ["yukihiro matsumoto","James Arthur Gosling","Guido Van Rossum"],
        "correta": "Guido Van Rossum"
    },
    {
        "pergunta": "Qual ano James criou o java?",
        "respostas": ["1991","1999","1989"],
        "correta": "1991"
    },
    {
        "pergunta": "Qual Universidade ele Estudou?",
        "respostas": ["Calgary","TUM","Oxford"],
        "correta": "Calgary"
    }
]
pergunta_quiz_4 = [
    {
        "pergunta": "Quem criou o Ethical Hacking?",
        "respostas": ["John Patrick","Linus Torvalds","Graydon Hoare"],
        "correta": "John Patrick"
    }
]
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
          tela_detalhes.atualizar_conteudo(item)
          self.manager.current = 'detalhes'

class TelaDetalhes(Screen):
    quiz_atual = None
    def atualizar_conteudo(self, item):
            self.ids.titulo_quiz.text = item['Título']
            self.ids.detalhes_quiz.text = item['detalhes']

    def iniciar_quiz(self):
        if self.quiz_atual:
            tela_jogo = self.manager.get_screen("jogo")
            tela_jogo.preparar_jogo(self.quiz_atual['perguntas'])
            self.manager.current = 'jogo'
class TelaJogo(Screen):
    pergunta_texto = StringProperty("")
    opcoes = ListProperty([])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.perguntas_ativas = []
        self.index = 0
        self.pontuacao = 0

    def carregar_perguntas(self):
        if self.index < len(self.perguntas_ativas):
            dados = self.perguntas_ativas[self.index]
            self.pergunta_texto = dados ["pergunta"]
            respostas = dados["respostas"]
class ListaQuizes(RecycleView):
    pass

class Gerenciador(ScreenManager):
    pass

class Multiquiz(App):
    def build(self):
        return Gerenciador()
if __name__ == "__main__":

    Multiquiz().run()