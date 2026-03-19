from Estoque.ListaStorage import DataStorage
def BuscarEstoque():
    produto_id = input("Qual o ID do produto? ")
    #Envia o ID do produto para a lista
    produto = DataStorage("Buscar",produto_id)
    #Se o produto_id existir mostra os dados
    if produto:
        print(f"\nO produto {produto_id} tem os seguintes dado: ")
        print(f"\nQtd: {produto[0]} | Origem: {produto[1]} | Motivo: {produto[2]}")
    else:
        print(f"\nNão foi possível achar o produto com ID {produto_id}")