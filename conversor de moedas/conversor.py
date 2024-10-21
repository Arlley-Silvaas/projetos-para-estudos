#* coisas a serem implementadas no código:
    #* criar uma interface para o conversor.
    #* Na interface terá uma saudação para o usuário.
    #* Abaixo dessa saudação,uma instrução para digitar o valor que será convertido e a moeda que será convertida.
    #* Na interface terá um "menu" de opções para a escolha da moeda para conversão.
    #* Após a escolha da moeda que será convertida, terá uma entrada para digitar o valor que será convertido.
    #? Abaixo dos dois,uma instrução de escolher no "menu" a moeda para qual será feita a conversão.
    #? Após a escolha da moeda,ao lado do "menu" de moedas,terá um espaço onde mostrará o valor atual da moeda.
    #? Abaixo do valor atual,terá um botão para converter o valor.
    #? Após o botão,terá um visor onde mostrará o valor convertido.
    #? Para finalizar,deverá ter um agradecimento por utilizar o conversor e uma mensagem de despedida.


import customtkinter

#* configurando a janela:
customtkinter.set_appearance_mode("Dark-Blue")  # Modes: "System" (standard), "Dark", "Light"
#? o comando acima define o tema da janela,para que o texto da janela seja mais legivel.

#* criando a janela
janela = customtkinter.CTk()
janela.title("Conversor de Moedas")
#janela.geometry("600x400")
#janela.resizable(False, False)

#* Saudação:
saudacao = customtkinter.CTkLabel(janela, text="Seja bem-vindo(a) ao conversor de moedas!", font=("ds-digital", 20),text_color="cyan")
saudacao.grid(row=0, column=0,padx=10, pady=10,columnspan=6)

#* instrução:
instrucao1 = customtkinter.CTkLabel(janela, text="Por favor, selecione abaixo a moeda que será convertida. Após isso, digite o valor desejado para conversão:", font=("ds-digital", 16))
instrucao1.grid(row=1, column=0, padx=10, pady=10,columnspan=6)

#* Chamando módulo que contém os dados das moedas disponíveis:
from buscar_moedas import *

#* menu onde será feita a escolha da moeda para conversão:
menu_entrada = customtkinter.CTkComboBox(janela, values=listar_moedas(),font=("ds-digital", 16))
menu_descolha_entrada = customtkinter.CTkLabel(janela, text="Moeda de origem:", font=("ds-digital", 16), text_color="orange")
menu_descolha_entrada.grid(row=2, column=0, pady=10)
menu_entrada.grid(row=2, column=1, pady=10)

#* colocando o espaço que o usuário vai digitar o valor que será convertido:
entrada = customtkinter.CTkEntry(janela)
entrada_descolha = customtkinter.CTkLabel(janela, text="Valor:", font=("ds-digital", 16), text_color="orange")
entrada_descolha.grid(row=2, column=2)
entrada.grid(row=2, column=3)

#* instrução para escolher a moeda para qual será feita a conversão:
instrucao2 = customtkinter.CTkLabel(janela, text="Por favor, selecione abaixo para qual moeda será feita a conversão:", font=("ds-digital", 16))
instrucao2.grid(row=3, column=0, padx=10, pady=10,columnspan=6)

#* menu onde será feita a escolha da moeda para qual será feita a conversão:
menu_saida = customtkinter.CTkComboBox(janela, values=listar_moedas(),font=("ds-digital", 16))
menu_descolha = customtkinter.CTkLabel(janela, text="Moeda de destino:", font=("ds-digital", 16), text_color="orange")
menu_descolha.grid(row=4, column=0, pady=10)
menu_saida.grid(row=4, column=1, pady=10)

#* caixa on terá o valor de todas as moedas:
informacoes_moedas = customtkinter.CTkLabel(janela, text="informações das moedas:", font=("ds-digital", 16), text_color="magenta")
informacoes_moedas.grid(row=5, column=1, pady=10)

#* criando uma caixa na janela para mostrar as informações das moedas:
caixa_moedas = customtkinter.CTkTextbox(janela, width=300, height=310 ,font=("ds-digital", 16))
caixa_moedas.grid(row=5, column=2, pady=10)

#mostrando na caixa o nome e valor das moedas:
exibir_moedas(caixa_moedas, pegar_valor_moeda())







janela.mainloop()
