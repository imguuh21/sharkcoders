class carro:
    def __init__(self,marca,modelo,motor):
        self.marca = marca
        self.modelo = modelo
        self.num_rodas = 4
        self.motor = motor

    def mostra_marca(self):
            print(self.marca)


    def mostra_modelo(self):
        print(self.modelo)

    def mostra_motor(self):
        print(self.motor)

    def alterar_motor(self,motor):
        self.motor = motor