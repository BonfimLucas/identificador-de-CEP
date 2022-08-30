#Lucas Bonfim
#29/08/2022
#API com o intuito de consultar os dados de um local com base no endereço do cliente.


#Bibliotecas utilizadas, pprint para organizar de forma clara as informaçoes.
#Biblioteca requests com o intuito de consultar com base na url.
import pprint
import requests

#inputs feitos para o cliente preencher os dados utilizando uf, cidade e nome da rua que deseja.
uf = str(input("Digite a sigla da unidade federativa onde se encontra a residência ou imovel: "))
cidade = str(input("Digite o nome da cidade onde se encontra a residência ou imovel: "))
logradouro = str(input("Digite o endereço do imovel:  ")) 


print("Abaixo estão os resultados de sua consulta: ")


link = f'https://viacep.com.br/ws/{uf}/{cidade}/{logradouro}/json/'
buscar = requests.get(link)
consultar = buscar.json()

#comando utilizado para mostrar os dados da consulta.
pprint.pprint(consultar)
