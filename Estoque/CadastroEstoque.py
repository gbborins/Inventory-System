from Verify import verification
from Estoque import Storage
def Estoque():
    nome = input("Qual o nome do produto? ")
    #Verifica o valor e quantidade
    valor = verification.validation(float,"Qual o valor do produto? ")
    quantidade = verification.validation(int,"Qual a quantidade do produto? ")
    #Envia os valores para o leitora de excel para guardar os dados
    Storage.stock(nome,valor,quantidade)