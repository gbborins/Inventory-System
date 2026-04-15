from Estoque.EstoqueLista import DataStorage
import pandas as pd
def RemoveStorage():
    produto_id = input("Qual o ID do produto que irá ser excluído? ")
    #Envia o ID do produto para a lista
    caminho = DataStorage("Remover",produto_id)
    #Se o produto existir excluí o produto
    if caminho:
        df = pd.read_json(caminho)
        certeza = input(f"\n Você tem certeza que quer excluir o produto: {produto_id}, (y/n): ")
        if certeza.lower() == "y":
                df = df[df["Produto_ID"] != produto_id]
                print(f"\nO produto {produto_id} foi removido")
    else:
        print(f"\nNão foi possível achar o produto com o ID {produto_id}")
    df.to_json(caminho,orient="records", indent=4)