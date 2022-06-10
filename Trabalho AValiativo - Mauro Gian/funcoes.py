from tkinter import *

class Cadastro():
    # salvar dados do login
    def dados_login(entry1, entry2, frame, framenovo):
        global armazenar_nome
        armazenar_nome = entry1.get()
        global armazenar_senha
        armazenar_senha = entry2.get()
        visible = 1
        if visible:
            frame.pack_forget()
            visible = 0
            framenovo.pack()

    # mostrar a senha
    def mostrar_senha(variavel, entry):
        if (variavel.get() == 1):
            entry.config(show='')
        else:
            entry.config(show='*')


    def sair(frame, framenovo):
        visible = 1
        if visible:
            frame.pack_forget()
            visible = 0
            framenovo.pack()

    def masculinoClicado(var):
        masculino = var
        if masculino == 1:
            global sexo
            sexo = 'masculino'
            print('hello')
        else:
            pass


    def gravar_dados(nome, sexo, cpf, telefone, datadenasci, rua, bairro, cidade, numero, uf):
        global nome_usu
        nome_usu = nome.get()

        if sexo == 1:
            sexo_usu = 'Masculino'
        else:
            sexo_usu = 'Feminino'


        global cpf_usu
        cpf_usu = cpf.get()

        global telefone_usu
        telefone_usu = telefone.get()

        global datanasci_usu
        datanasci_usu = datadenasci.get()

        global rua_usu
        rua_usu = rua.get()

        global bairro_usu
        bairro_usu = bairro.get()

        global cidade_usu
        cidade_usu = cidade.get()

        global numero_usu
        numero_usu = numero.get()

        global uf_usu
        uf_usu = uf.get()

        print('===== DADOS USUARIO: =====\n'
              f'NOME: {nome_usu}\n'
              f'CPF: {cpf_usu}\n'
              f'SEXO: {sexo_usu}\n'
              f'TELEFONE: {telefone_usu}\n'
              f'DATA NASC: {datanasci_usu}\n'
              f'===== ENDEREÇO: ====='
              f'RUA: {rua_usu}\n'
              f'BAIRRO: {bairro_usu}\n'
              f'CIDADE: {cidade_usu}\n'
              f'ESTADO: {uf_usu}\n'
              f'NUMERO: {numero_usu}\n')





