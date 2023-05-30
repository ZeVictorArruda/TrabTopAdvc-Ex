from ConfiguracaoCarro import *
from CarroBuilder import *

configuracao_carro = ConfiguracaoCarro()
configuracao_carro.set_configuracao("Esportivo")

# Chamada do construtor abaixo apenas para testar Singleton
configuracao_carro2 = ConfiguracaoCarro()

builder = CarroBuilder()
builder.set_modelo("Sedan")
builder.set_cor("Vermelho")
builder.set_motor("2.0")
builder.set_numero_portas(4)
builder.set_ano_fabricacao(2022)
builder.set_sistema_som("Alto-falantes premium")
builder.set_sistema_navegacao("GPS integrado")

carro = builder.get_carro()
carro.configuracao = configuracao_carro.get_configuracao()

print(carro.imprimirDados())