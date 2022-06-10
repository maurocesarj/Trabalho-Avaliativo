from tkinter import *
import funcoes
from funcoes import *

#Função para a data de nascimento ter a barra(/)
def format_datanasc(event = None):
    text = entry_datanasc.get().replace("/", "").replace("", "")[:8]
    new_text = ""

    if event.keysym.lower() == "backspace": return

    for index in range(len(text)):

        if not text[index] in "0123456789": continue
        if index in [1, 3]:
            new_text += text[index] + "/"
        elif index == 4:
            new_text += text[index] + ""
        else:
            new_text += text[index]

    entry_datanasc.delete(0, "end")
    entry_datanasc.insert(0, new_text)

#função para o CPF conter ponto e traço (., -)
def format_cpf(event = None):
    text = entry_cpf.get().replace(".", "").replace("-", "")[:11]
    new_text = ""

    if event.keysym.lower() == "backspace": return

    for index in range(len(text)):

        if not text[index] in "0123456789": continue
        if index in [2, 5]:
            new_text += text[index] + "."
        elif index == 8:
            new_text += text[index] + "-"
        else:
            new_text += text[index]

    entry_cpf.delete(0, "end")
    entry_cpf.insert(0, new_text)

#Função para o Telefone conter limite de numeros
def format_telefone(event = None):
    text = entry_tel.get().replace(".", "").replace("-", "")[:11]
    new_text = ""

    if event.keysym.lower() == "backspace": return

    for index in range(len(text)):

        if not text[index] in "0123456789": continue
        if index in [1, 2]:
            new_text += text[index] + "."
        elif index == 6:
            new_text += text[index] + "-"
        else:
            new_text += text[index]

    entry_tel.delete(0, "end")
    entry_tel.insert(0, new_text)


# criação da janela, frame e suas configuraçõesw
root = Tk()
root.geometry("1280x768")
frame1 = Frame()
frame1.configure(bg="#5CE1E6")
ig = PhotoImage(file="back01.png")
igl = PhotoImage(file="bg02.png")
imagem_de_fundo = Label(frame1, text='Hello', foreground='black', image=ig).pack()


# frame 02
frame2 = Frame()
frame2.configure(bg="#5CE1E6")
root.bind('<Return>', lambda event:(funcoes.Cadastro.dados_login(entryUsername, entryPassword)))


# label
username = Label(frame1, text="Username",  font='Arial 13', foreground='Grey', bg="#FFFFFF")
username.place(x=465, y=290)
# Linha 01
linhaName = Label(frame1, text="________________________________",  font='Arial 13', foreground='Grey', bg="#FFFFFF")
linhaName.place(x=465, y=345)

password = Label(frame1, text="Password",  font='Arial 13', foreground='Grey', bg="#FFFFFF")
password.place(x=465, y=390)
# linha 02
linhaPassword = Label(frame1, text="________________________________",  font='Arial 13', foreground='Grey', bg="#FFFFFF")
linhaPassword.place(x=465, y=445)
# Botão Login
login = Button(frame1, text="Login", font='Arial 15', bg="#303030", foreground='white', bd=0, padx=97, pady=17, cursor="hand2", command=lambda: funcoes.Cadastro.dados_login(entryUsername, entryPassword, frame1, frame2))
login.place(x=512, y=525)

# Entry Username
entryUsername = Entry(frame1, font='Arial 14', foreground='#222222', bg='#FFFFFF', bd=0, width=27)
entryUsername.place(x=467, y=335)
# Entry Password
entryPassword = Entry(frame1, font='Arial 14', foreground='#222222', bg='#FFFFFF', bd=0, width=27, show="*")
entryPassword.place(x=467, y=435)
# showpassword
cv5=IntVar(value=0)
c1 = Checkbutton(frame1,text='Show Password',variable=cv5, onvalue=1,offvalue=0, bg="#FFFFFF", foreground="#303030", bd=0, command=lambda: funcoes.Cadastro.mostrar_senha(cv5, entryPassword))
c1.place(x=467, y=480)












# criação da tela de cadastro
imagem_de_fundo_frame02 = Label(frame2, text='Hello', foreground='black', image=igl).pack()

# label titulo Guia
titulo = Label(frame2, text='Dados Pessoais: ', foreground='white', font='Arial 14', bg="#303030")
titulo.place(x=310, y=120)

# label name
nome = Label(frame2, text='Nome:', foreground='white', font='Arial 14', bg="#303030")
nome.place(x=295 , y=160)
entry_nome = Entry(frame2, font='Arial 14', foreground='#222222', bg='#FFFFFF', bd=0, width=42)
entry_nome.place(x=360, y=160)

# Cpf
cpf = Label(frame2, text='CPF:', foreground='white', font='Arial 14', bg="#303030")
cpf.place(x=295 , y=190)
entry_cpf = Entry(frame2, font='Arial 14', foreground='#222222', bg='#FFFFFF', bd=0, width=17)
entry_cpf.place(x=360, y=190)
entry_cpf.bind("<KeyRelease>", format_cpf)

# telefone
tel = Label(frame2, text='Telefone:', foreground='white', font='Arial 14', bg="#303030")
tel.place(x=525 , y=190)
entry_tel = Entry(frame2, font='Arial 14', foreground='#222222', bg='#FFFFFF', bd=0, width=18)
entry_tel.place(x=614, y=190)
entry_tel.bind("<KeyRelease>", format_telefone)

# Sexo masculino
cv1=IntVar(value=0)
c1 = Checkbutton(frame2,variable=cv1, onvalue=1,offvalue=0, bg="#303030", bd=0, command=lambda: funcoes.Cadastro.masculinoClicado(cv1))
c1.place(x=840, y=160)

masculino= Label(frame2, text='Masculino', foreground='white', font='Arial 14', bg="#303030")
masculino.place(x=865 , y=157)

# Sexo feminino
c2 = Checkbutton(frame2,variable=cv1, onvalue=0,offvalue=0, bg="#303030", bd=0)
c2.place(x=970, y=160)

feminino= Label(frame2, text='Feminino', foreground='white', font='Arial 14', bg="#303030")
feminino.place(x=995 , y=157)

# label preencher espaço
espaco = Label(frame2, text='aaaaaa', font='Arial 13', foreground="#505050", bg="#505050", width=30)
espaco.place(x=826, y=190)

# data de nascimento
datanas = Label(frame2, text='Data de Nasc:', foreground='white', font='Arial 14', bg="#303030")
datanas.place(x=295 , y=220)
entry_datanasc = Entry(frame2, font='Arial 14', foreground='#222222', bg='#FFFFFF', bd=0, width=18)
entry_datanasc.place(x=425, y=222)
entry_datanasc.bind("<KeyRelease>", format_datanasc)

# label preencher espaço
espaco2 = Label(frame2, text='aaaaaa', font='Arial 13', foreground="#505050", bg="#505050", width=52)
espaco2.place(x=630, y=222)


# botao sair
sair = Button(frame2, text="Sair", font='Arial 15', bg="#505050", foreground='white', bd=0, padx=97, pady=17, cursor="hand2", command=lambda: funcoes.Cadastro.sair(frame2, frame1))
sair.place(x=400, y=490)

# botao gravar dados
gravar = Button(frame2, text="Gravar Dados", font='Arial 15', bg="#505050", foreground='white', bd=0, padx=70, pady=17, cursor="hand2", command=lambda: funcoes.Cadastro.gravar_dados(entry_nome, c1, entry_cpf, entry_tel, entry_datanasc, entry_rua, entry_bairro, entry_cidade, entry_numero, entry_uf))
gravar.place(x=670, y=490)

# label Endereço Guia
titulo2 = Label(frame2, text='Endereço: ', foreground='white', font='Arial 14', bg="#303030")
titulo2.place(x=310, y=280)

# label Rua
rua = Label(frame2, text='Rua:', foreground='white', font='Arial 14', bg="#303030")
rua.place(x=312, y=320)
entry_rua = Entry(frame2, font='Arial 14', foreground='#222222', bg='#FFFFFF', bd=0, width=50)
entry_rua.place(x=360, y=321)

# Bairro
bairro = Label(frame2, text='Bairro:', foreground='white', font='Arial 14', bg="#303030")
bairro.place(x=295, y=350)
entry_bairro = Entry(frame2, font='Arial 14', foreground='#222222', bg='#FFFFFF', bd=0, width=16)
entry_bairro.place(x=360, y=350)

# cidade
cidade = Label(frame2, text='Cidade:', foreground='white', font='Arial 14', bg="#303030")
cidade.place(x=541, y=350)
entry_cidade = Entry(frame2, font='Arial 14', foreground='#222222', bg='#FFFFFF', bd=0, width=27)
entry_cidade.place(x=614, y=350)

# label N°
numero = Label(frame2, text='N° :', foreground='white', font='Arial 14', bg="#303030")
numero.place(x=917, y=320)
entry_numero = Entry(frame2, font='Arial 14', foreground='#222222', bg='#FFFFFF', bd=0, width=14)
entry_numero.place(x=954, y=320)

# label uf
uf = Label(frame2, text='UF :', foreground='white', font='Arial 14', bg="#303030")
uf.place(x=915, y=350)
entry_uf = Entry(frame2, font='Arial 14', foreground='#222222', bg='#FFFFFF', bd=0, width=14)
entry_uf.place(x=954, y=350)

frame1.pack()
frame2.pack()
root.resizable(False, False)
root.mainloop()