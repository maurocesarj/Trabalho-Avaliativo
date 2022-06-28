from classe_controle_produtos import *
from classe_compra import *

class Menu:
    def __init__(self):
        controle_produtos_mauro = Controle()

        # Iniciar menu
        while True:
            op = input('\n-=-=-=--=-= Informe a opção desejada -=-=-=--=-=\n1 | Cadastrar\n2 | Listar Produtos\n3 | Alterar Produto\n0 | Sair\n-=-= Sua Escolha: ')

            if op == '1':
                controle_produtos_mauro.cadastrar_produtos()
            elif op == '2':
                controle_produtos_mauro.listar_produtos()
            elif op == '3':
                controle_produtos_mauro.alterar_descricao()
            elif op == '0':
                break
            else:
                print('Entrada incorreta')