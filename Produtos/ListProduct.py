#Produtos listados
import pandas as pd
import os
def DataProduct(funcao,nome = None,valor = None, quantidade = None,
                categoria = None,fabricante = None,especificacao = None,fornecedor_id = None):
    path = r"D:\Programacao\Python\Proj2\Produtos\lista_produtos.json"
    #verifica se o caminho já existe
    if os.path.exists(path) and os.path.getsize(path) > 0:
        #Lê um arquivo json
        df = pd.read_json(path)
        if df.empty:
            df = pd.DataFrame(columns=[
            "Nome",
            "Valor",
            "Quantidade",
            "Categoria",
            "Fabricante",
            "Especificacao",
            "Fornecedor_id"
        ])
    else:
        #Se não existir cria um novo
        df = pd.DataFrame(columns=[
            "Nome",
            "Valor",
            "Quantidade",
            "Categoria",
            "Fabricante",
            "Especificacao",
            "Fornecedor_id"
        ])
    if funcao == "Cadastro": 
        #Escreve no arquivo json
        if nome not in df["Nome"].values:
            #Adiciona uma nova linha com os valores
            df.loc[len(df)] = [nome,valor,quantidade,categoria,fabricante,especificacao,fornecedor_id]
            print(f"Produto {nome} cadastrado com sucesso")
        else:
            linha = df[df["Nome"] == nome].index[0]
            #Substitui o novo valor
            if df.loc[linha,"Valor"] != valor:
                df.loc[linha,"Valor"] = valor
                print("O valor mudou")
            if df.loc[linha,"Categoria"] != categoria:
                df.loc[linha,"Categoria"] = categoria
                print("A categoria mudou")
            if df.loc[linha,"Fabricante"] != fabricante:
                df.loc[linha,"Fabricante"] = fabricante
                print("O fabricante mudou")
            if df.loc[linha,"Especificacao"] != especificacao:
                df.loc[linha,"Especificacao"] = especificacao
                print("A Especificação mudou")
            if df.loc[linha,"Fornecedor_id"] != fornecedor_id:
                df.loc[linha,"Fornecedor_id"] = fornecedor_id
                print("O Fornecedor_id mudou")
            #Soma a quantidade com a já guardada
            df.loc[linha,"Quantidade"] += quantidade
            print(f"Houve um aumento de {quantidade} no produto {nome}")
    elif funcao == "Buscar":
        #Verifica se o nome está em alguma linha
        if nome in df["Nome"].values:
            #Obtém a linha em que o nome é encontrado
            linha = df[df["Nome"] == nome].index[0]
            return [df.loc[linha,"Valor"],df.loc[linha,"Quantidade"],
                    df.loc[linha,"Categoria"],df.loc[linha,"Fabricante"],
                    df.loc[linha,"Especificacao"],df.loc[linha,"Fornecedor_id"]]
        else:
            return False
    elif funcao == "Lista":
        for _,linha in df.iterrows():
            print(f"""{linha["Nome"]} | R${linha["Valor"]} | Qtd: {linha["Quantidade"]} 
                  | Cate: {linha["Categoria"]} | Fabri: {linha["Fabricante"]} | Espe: {linha["Especificacao"]}
                  | Fornecedor:{linha["Fornecedor_id"]}""")
    elif funcao == "Remover":
        #Verifica se o nome está em alguma linha
        if nome in df["Nome"].values:
            #Retorna a linha e o caminho
            return path
    #Salva o arquivo para não perder as modificações
    df.to_json(path, orient="records", indent=4)