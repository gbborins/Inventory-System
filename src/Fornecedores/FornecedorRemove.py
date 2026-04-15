from Fornecedores.FornecedorLista import DataProvider
import pandas as pd
def remove_provider():
    nome_empresa = input("Qual o nome da empresa que vai ser excluída? ")
    #Envia o nome da empresa para a lista
    caminho = DataProvider("Remover",nome_empresa)
    #Se a empresa existir excluí o produto
    if caminho:
        df = pd.read_json(caminho)
        certeza = input(f"\n Você tem certeza que quer excluir a empresa: {nome_empresa}, (y/n): ")
        if certeza.lower() == "y":
                df = df[df["Nome_Empresa"] != nome_empresa]
                print(f"\nA empresa {nome_empresa} foi removida")
    else:
        print(f"\nNão foi possível achar a empresa com nome {nome_empresa}")
    df.to_json(caminho,orient="records", indent=4)