from classe_controle_produtos import *

class Compra:
    def __init__(self):
        self.quant_produtos = []

    def comprar_estoque(self, vetor):
        vetor = Controle.cadastrar_produtos().self.lista_de_produtos.cod
        cod_produto = str(input('Digite o COD do produto que deseja comprar: '))
        for i in range(len(vetor)):
            if cod_produto[i] == vetor[i]:
                print('hello')



