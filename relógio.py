from tkinter import *
import tkinter as tk
import os
from time import strftime

root = Tk()
root.title("Relógio")
root.geometry("500x300")
root.resizable(False, False)
root.config(bg="black")

def pegar_saudacao():
    nome_usuario = os.getlogin()
    saudacao_hora = verificar_hora(strftime("%H:%M:%S"))
    saudacao.config(text=f"Bem vindo(a), {nome_usuario}, {saudacao_hora}", fg="cyan", font=("ds-digital", 12))

def pegar_data():
    data_atual = strftime("%a %d %B %Y")
    data.config(text=data_atual)

def verificar_hora(hora):
    horario = atualizar_hora()
    if hora < '12:00:00':
        return 'Bom dia!'
    elif hora < '18:00:00':
        return 'Boa tarde!'
    else:
        return 'Boa noite!'

def atualizar_hora():
    hora_atual = strftime("%H:%M:%S")
    hora.config(text=hora_atual)
    root.after(1000, atualizar_hora)

saudacao = Label(root, font=("ds-digital", 18), bg="black", fg="cyan")
saudacao.pack()
data = Label(root, font=("ds-digital", 13), bg="black", fg="cyan")
data.pack()
hora = tk.Label(root, font=("ds-digital", 40), bg="black", fg="cyan")
hora.pack()

pegar_saudacao()
pegar_data()
atualizar_hora()

root.mainloop()