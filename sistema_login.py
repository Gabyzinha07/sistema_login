import tkinter as tk
from tkinter import *
from tkinter import Label

janela = tk.Tk()

janela.title('Sistema de Login')

janela['bg'] = 'grey'

janela.rowconfigure(0, weight=1)
janela.columnconfigure([0, 1], weight=1)

label_informacoes = tk.Label(text = 'Informações de Login', borderwidth=2, relief='solid', background='pink')
label_informacoes.grid(row=0, column=0, padx=10, pady=10, sticky='nswe', columnspan=3)

label_nome = tk.Label(text='E-mail:', fg='white', bg='black')
label_nome.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

email = tk.Entry()
email.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)


label_senha = tk.Label(text='Senha:', fg='white', bg='black')
label_senha.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

label_mensagem = tk.Label(text='', fg='black', bg='grey')
label_mensagem.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=1)

senha = tk.Entry()
senha.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
senha["show"] = "*"


def autenticar():
    usuario = email.get()
    verificar_senha = senha.get()
    if usuario == 'Gabriellyalves401@gmail.com' and verificar_senha == '102030':
        label_mensagem['text'] = 'Autenticado'
    else:
        label_mensagem['text'] = 'Não autenticado'


botao = tk.Button(text='Autenticar', background='pink', command=autenticar)
botao.grid(row=5, column=1)

janela.mainloop()
