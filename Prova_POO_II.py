
class Veiculo():
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
    def movimentar(self):
        print("O veículo está se movendo.")

class Carro(Veiculo):
    def movimentar(self):
        print(f'O carro {self.marca}, {self.modelo}, {self.ano}, {self.cor} está dirigindo.')
    
class Moto(Veiculo):
    def movimentar(self):
        print(f'A moto {self.marca}, {self.modelo}, {self.ano}, {self.cor} está acelerando.')

carro1 = Carro("Chevrolet", "Cruze", 2019, "Preto")
carro1.movimentar()
moto1 = Moto("Honda", "CB 500", 2020, "Vermelha")
moto1.movimentar()