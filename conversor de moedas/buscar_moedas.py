
#? módulo responsável por buscar os dados das moedas para implementar no código conversor.

import requests
import json

#* função que busca todos os nomes de todas as moedas


def listar_moedas():
    requests.get("https://economia.awesomeapi.com.br/json/all")
    moedas = requests.get("https://economia.awesomeapi.com.br/json/all").json()
    return list(moedas.keys())


#* função que mostra informações da moeda:

def pegar_valor_moeda():
    #* pegando o valor de todas as moedas:
    moedas = requests.get("https://economia.awesomeapi.com.br/json/all").json()
    #* criando uma lista para armazenar as informações das moedas:
    informa_moedas = []

    #* percorrendo a lista de moedas:
    for moeda in moedas:
        #* criando uma lista para armazenar as informações da moeda:
        info_moeda = []
        #* pegando apenas os nomes e valores das moedas:
        nome_moeda = moeda
        valor_moeda = moedas[moeda]['bid']

        #* colocando os dados da moeda na lista:
        info_moeda.append(nome_moeda)
        info_moeda.append(valor_moeda)

        #*organizando os dados da moeda:
        informa_moedas.append(info_moeda)

    #* organizando os dados das moedas com valor após nome 
    informa_moedas.sort(key=lambda x: x[1], reverse=True)

    #* mostrando os dados das moedas:
    return informa_moedas

def exibir_moedas(textbox, informa_moedas):
    # Adicionando cabeçalho à textbox
    textbox.insert("end", "Moeda   | Valor (R$)\n")
    textbox.insert("end", "--------------------\n")
    
    # Exibindo os dados das moedas na textbox
    for moeda in informa_moedas:
        nome = moeda[0]
        valor = moeda[1]
        # Formatando e adicionando o texto à textbox
        textbox.insert("end", f"{nome:<7} | {valor:>9}\n")