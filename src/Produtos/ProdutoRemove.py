from Produtos.ProdutoLista import DataProduct
import pandas as pd
def remove_produto():
    nome = input("Qual o nome do produto que vai ser excluído? ")
    #Envia o nome do produto para a lista
    caminho = DataProduct("Remover",nome)
    #Se o produto existir excluí o produto
    if caminho:
        df = pd.read_json(caminho)
        certeza = input(f"\n Você tem certeza que quer excluir o produto: {nome}, (y/n): ")
        if certeza.lower() == "y":
                df = df[df["Nome"] != nome]
                print(f"\nO produto {nome} foi removido")
    else:
        print(f"\nNão foi possível achar o produto com nome {nome}")
    df.to_json(caminho,orient="records", indent=4)