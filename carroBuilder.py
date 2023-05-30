from carro import *


class CarroBuilder:
    def __init__(self):
        self.carro = Carro()

    def set_modelo(self, modelo):
        self.carro.modelo = modelo

    def set_cor(self, cor):
        self.carro.cor = cor

    def set_motor(self, tipo):
        motor = Motor(tipo)
        self.carro.motor = motor

    def set_numero_portas(self, numero_portas):
        self.carro.numero_portas = numero_portas

    def set_ano_fabricacao(self, ano_fabricacao):
        self.carro.ano_fabricacao = ano_fabricacao

    def set_sistema_som(self, marca):
        sistema_som = SistemaSom(marca)
        self.carro.sistema_som = sistema_som

    def set_sistema_navegacao(self, sistema_navegacao):
        self.carro.sistema_navegacao = sistema_navegacao

    def get_carro(self):
        return self.carro
