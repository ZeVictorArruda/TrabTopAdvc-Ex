class Carro:
    def __init__(self):
        self.modelo = None
        self.cor = None
        self.motor = None
        self.numero_portas = None
        self.ano_fabricacao = None
        self.sistema_navegacao = None

    def imprimirDados(self):
        print("Dados do carro:")
        print(f"Modelo: {self.modelo};\nCor: {self.cor};\nMotor: {self.motor.tipo};\nNº Portas: {self.numero_portas};")
        print(f"Ano: {self.ano_fabricacao}\nNavegação: {self.sistema_navegacao}")


# o motor será passado através da classe motor
class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

    def get_tipo(self):
        return self.tipo


# o sistemade som será passado através da classe SistemaSom
class SistemaSom:
    def __init__(self, marca):
        self.marca = marca

    def get_marca(self):
        return self.marca
