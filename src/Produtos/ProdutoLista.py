#Produtos listados
import pandas as pd
from pathlib import Path
def DataProduct(funcao,nome = None,valor = None, quantidade = None,
                categoria = None,fabricante = None,especificacao = None,fornecedor_id = None):
    path = Path(input("Digite o nome do arquivo JSON: "))
    json_file = Path(__file__).parent / path
    #verifica se o caminho já existe
    if not Path.exists(json_file):
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
    elif Path(json_file).stat().st_size > 0:
        #Lê um arquivo json
        df = pd.read_json(json_file)
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
    if funcao == "Cadastro": 
        #Escreve no arquivo json
        if nome not in df["Nome"].values:
            #Adiciona uma nova linha com os valores
            df.loc[len(df)] = [nome,valor,quantidade,categoria,fabricante,especificacao,fornecedor_id]
            print(f"\nProduto {nome} cadastrado com sucesso")
        else:
            linha = df[df["Nome"] == nome].index[0]
            #Substitui o novo valor
            if df.loc[linha,"Valor"] != valor:
                df.loc[linha,"Valor"] = valor
                print("\nO valor mudou")
            if df.loc[linha,"Categoria"] != categoria:
                df.loc[linha,"Categoria"] = categoria
                print("\nA categoria mudou")
            if df.loc[linha,"Fabricante"] != fabricante:
                df.loc[linha,"Fabricante"] = fabricante
                print("\nO fabricante mudou")
            if df.loc[linha,"Especificacao"] != especificacao:
                df.loc[linha,"Especificacao"] = especificacao
                print("\nA Especificação mudou")
            if df.loc[linha,"Fornecedor_id"] != fornecedor_id:
                df.loc[linha,"Fornecedor_id"] = fornecedor_id
                print("\nO Fornecedor_id mudou")
            #Soma a quantidade com a já guardada
            df.loc[linha,"Quantidade"] += quantidade
            print(f"\nHouve um aumento de {quantidade} no produto {nome}")
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
            print(f"""\n{linha["Nome"]} | R${linha["Valor"]} | Qtd: {linha["Quantidade"]} 
                  | Cate: {linha["Categoria"]} | Fabri: {linha["Fabricante"]} | Espe: {linha["Especificacao"]}
                  | Fornecedor:{linha["Fornecedor_id"]}""")
    elif funcao == "Remover":
        #Verifica se o nome está em alguma linha
        if nome in df["Nome"].values:
            #Retorna a linha e o caminho
            return json_file
    #Salva o arquivo para não perder as modificações
    df.to_json(json_file, orient="records", indent=4)