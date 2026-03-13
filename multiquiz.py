from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.recycleview import RecycleView


Quizes = [
    {"Título": "Quiz 1","Descrição": "Quiz sobre Python", "detalhes": "Perguntas sobre Python"},
    {"Título": "Quiz 2","Descrição": "Quiz sobre HTML", "detalhes": "Perguntas sobre HTML"},
    {"Título": "Quiz 3","Descrição": "Quiz sobre Java", "detalhes": "Perguntas sobre Java"},
    {"Título": "Quiz 4","Descrição": "Quiz sobre Ethical hacking", "detalhes": "Perguntas sobre Segurança"}
]


class TelaPrincipal(Screen):

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

    def atualizar_conteudo(self, item):

        self.ids.titulo.text = item["Título"]

        self.ids.descricao.text = item["detalhes"]



class ListaQuizes(RecycleView):
    pass


class Gerenciador(ScreenManager):
    pass



class Multiquiz(App):

    def build(self):
        return Gerenciador()



if __name__ == "__main__":
    Multiquiz().run()