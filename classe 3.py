class Livro:
    def __init__(self,Título,autor,páginas):
        self.titulo = Título
        self.autor = autor
        self.paginas = páginas

    def mostrar(self):
        print(f"Titulo: {self.titulo}")
        print(f"autor: {self.autor}")
        print(f"paginas:{self.paginas}")

Livro1 = Livro("a biblioteca da meia noite","matt haig",308)
Livro1.mostrar()
Livro2 = Livro("os contos mais arrepiantes de howard philipes lovecraft","h.p.lovecraft","570")
Livro2.mostrar()
Livro3 = Livro("o Senhor dos a""Anéis","Tolkien","1280")
class biblioteca:
    def __init__(self):
        self.colecao = []

    def adicionar_livro(self,Livro):
        self.colecao.append(Livro)

    def listar_livros(self):
        if not self.colecao:
            print("a biblioteca está vazia")
        else:
            print("\nlista de livros na biblioteca")
        for livro in self.colecao:
            livro.mostrar()
            print("\n")
    def contar_Livros(self):
        return len(self.colecao)

minha_biblioteca = biblioteca()

minha_biblioteca.adicionar_livro(Livro1)
minha_biblioteca.adicionar_livro(Livro2)
minha_biblioteca.adicionar_livro(Livro3)

minha_biblioteca.listar_livros()