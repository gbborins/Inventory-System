#Produtos listados
import pandas as pd
import os
def DataProduct(nome,valor, quantidade,categoria,fabricante,especificacao):
    path = r"D:\Programacao\Python\Proj2\Produtos\lista.json"
    #verifica se o caminho já existe
    if os.path.exists(path) and os.path.getsize(path) > 0:
        #Lê um arquivo json
        df = pd.read_json(path)
    else:
        #Senão existir cria um novo
        df = pd.DataFrame(columns=[
            "Nome",
            "Valor",
            "Quantidade",
            "Categoria",
            "Fabricante",
            "Especificacao"
        ])
        #Escreve no arquivo json
    if nome not in df["Nome"].values:
        #Adiciona uma nova linha com os valores
        df.loc[len(df)] = [nome,valor,quantidade,categoria,fabricante,especificacao]
        print(f"Produto {nome} cadastrado com sucesso")
    else:
        linha = df[df["Nome"] == nome].index[0]
        #Substitui o novo valor
        if df.loc[linha,"Valor"] != valor:
            print("O valor mudou")
            df.loc[linha,"Valor"] = valor
        #Soma a quantidade com a já guardada
        df.loc[linha,"Quantidade"] += quantidade
        print(f"Houve um aumento de {quantidade} no produto {nome}")
    #Salva o arquivo para não perder as modificações
    df.to_json(r"D:\Programacao\Python\Proj2\Produtos\lista.json", orient="records", indent=4)