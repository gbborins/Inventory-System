from Vendas.VendaLista import DataSale
import pandas as pd
def RemoveSale():
    cliente_id = input("Qual o ID do cliente que irá ser excluído? ")
    #Envia o ID do cliente para a lista
    caminho = DataSale("Remover",cliente_id)
    #Se o produto existir excluí o produto
    if caminho:
        df = pd.read_json(caminho)
        certeza = input(f"\n Você tem certeza que quer excluir o cliente: {cliente_id}, (y/n): ")
        if certeza.lower() == "y":
                df = df[df["Cliente_ID"] != cliente_id]
                print(f"\nO cliente {cliente_id} foi removido")
    else:
        print(f"\nNão foi possível achar o cliente com o ID {cliente_id}")
    df.to_json(caminho,orient="records", indent=4)