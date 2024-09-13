from tkinter import *

#* Função de click no botão de digito
def botao_click(texto):
    if texto == 'C':
        apagar_visor()
    elif texto == '<-':
        apagar_ultimo()
    elif texto in '+-*/':
        if visor.get() == '' or visor.get()[-1] in '+-*/':
            return
        visor.insert(END, texto)
    else:
        visor.insert(END, texto)

#* Função para apagar o visor
def apagar_visor():
    visor.delete(0, END)


#* Função para apagar o ultimo digito do visor
def apagar_ultimo():
    texto = visor.get()
    if texto:
        visor.delete(len(texto) - 1, END)

#* Função para validar se o caractere digitado é um número
def validar_entrada(digito):
    return digito in '0123456789.-+()*/%'



#* Criando os botoes
def criar_botao(texto,comando=None):
    if comando is None:
        comando = lambda: botao_click(texto)
    return  Button(janela, text=texto, width=5, height=2, font=('courier', 20, 'bold'), bg='black', fg='orange', command=lambda: botao_click(texto))

#* função para ajuste dos parentesis
def ajustar_parentesis():
    texto = visor.get()
    if texto.count('(') <= texto.count(')'):
        visor.insert(END, '(')
    else:
        visor.insert(END, ')')


#* Função para calcular
def botão_igualdade():
    try:
        texto = visor.get()
        resultado = eval(texto)
        visor.delete(0, END)
        visor.insert(0, resultado)
    except:
        visor.delete(0, END)
        visor.insert(0, 'Erro')

#* Criando a janela
janela = Tk()
janela.title("TUA CALK")
janela.configure(bg='#282828')

#* Criando o visor onde mostrará os números
visor_validado = (janela.register(validar_entrada), '%S')
visor = Entry(janela,validate='key', validatecommand=visor_validado, borderwidth=5, font=('courier', 20, 'bold'),bg='lightblue', fg='black', justify=RIGHT, width=15, relief=RIDGE)
#? colocando um foco no visor para poder digitar o primeiro número
visor.focus_set()
visor.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#* Criando os botões de operações
# botão de apagar visor
botõesde_operações = ['C','<-','%','/','*','+','-']
for i, botao in enumerate(botõesde_operações):
    criar_botao(botao).grid(row=i // 4 + 1, column=i % 4)

# botão de parentheses
botão_parentheses = Button(janela, text='()', width=5, height=2, font=('courier', 20, 'bold'), bg='black', fg='orange', command=lambda: ajustar_parentesis()).grid(row=2, column=3)


#* Criando os outros botoes númericos
botões = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0', '.']
for i, botao in enumerate(botões):
    criar_botao(botao).grid(row=i // 4 + 4, column=i % 4)

# botão de igual
botão_igual = Button(janela, text='=', width=5, height=2, font=('courier', 20, 'bold'), bg='orange', fg='black', command=botão_igualdade).grid(row=6, column=3)


janela.mainloop()