class pessoa:
    def __init__(self,altura,cabelo,olhos,idade):

        self.altura = float(input(altura))
        self.cabelo = cabelo
        self.olhos = olhos
        self.idade = int(input(idade))

    def altura(self):
        print(self.altura)


