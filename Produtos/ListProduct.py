#Produtos listados
import pandas as pd
import os
def DataProduct(funcao,nome = None,valor = None, quantidade = None,
                categoria = None,fabricante = None,especificacao = None):
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
    if funcao == "Cadastro": 
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
    elif funcao == "Buscar":
        if nome in df["Nome"].values:
            linha = df[df["Nome"] == nome].index[0]
            return [df.loc[linha,"Valor"],df.loc[linha,"Quantidade"],
                    df.loc[linha,"Categoria"],df.loc[linha,"Fabricante"],df.loc[linha,"Especificacao"]]
        else:
            return False
    elif funcao == "Lista":
        for i, linha in df.iterrows():
            print(f"""{linha["Nome"]} | R${linha["Valor"]} | Qtd: {linha["Quantidade"]} | Cate: {linha["Categoria"]} | Fabri: {linha["Fabricante"]} | Espe: {linha["Especificacao"]}""")
    #Salva o arquivo para não perder as modificações
    df.to_json(r"D:\Programacao\Python\Proj2\Produtos\lista.json", orient="records", indent=4)