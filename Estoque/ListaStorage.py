#Fornecedores listados
import pandas as pd
from pathlib import Path
def DataStorage(funcao,produto_id = None,quantidade = None,origem = None,
                motivo = None):
    path = Path(input("Digite o nome do arquivo JSON: "))
    json_file = Path(__file__).parent / path
    #verifica se o caminho já existe
    if not Path.exists(json_file):
        #Se não existir cria um novo
        df = pd.DataFrame(columns=[
        "Product_ID",
        "Quantidade",
        "Origem",
        "Motivo"
        ])
    elif Path(json_file).stat().st_size > 0:
        #Lê um arquivo json
        df = pd.read_json(json_file)
        if df.empty:
            df = pd.DataFrame(columns=[
            "Product_ID",
            "Quantidade",
            "Origem",
            "Motivo"
        ])
    if funcao == "Cadastro": 
        #Escreve no arquivo json
        if produto_id not in df["Product_ID"].values:
            #Adiciona uma nova linha com os valores
            df.loc[len(df)] = [produto_id,quantidade,origem,motivo]
            print(f"\nProduto {produto_id} cadastrado com sucesso")
        else:
            linha = df[df["Product_ID"] == produto_id].index[0]
            #Substitui o novo quantidade
            if df.loc[linha,"Quantidade"] != quantidade:
                df.loc[linha,"Quantidade"] = quantidade
                print("\nO quantidade mudou")
            if df.loc[linha,"Origem"] != origem:
                df.loc[linha,"Origem"] = origem
                print("\nO origem mudou")
            if df.loc[linha,"Motivo"] != motivo:
                df.loc[linha,"Motivo"] = motivo
                print("\nO motivo mudou")
    elif funcao == "Buscar":
        #Verifica se o produto_id está em alguma linha
        if produto_id in df["Product_ID"].values:
            #Obtém a linha em que o produto_id é encontrado
            linha = df[df["Product_ID"] == produto_id].index[0]
            return [df.loc[linha,"Quantidade"],df.loc[linha,"Origem"],
                    df.loc[linha,"Motivo"]]
        else:
            return False
    elif funcao == "Lista":
        for _,linha in df.iterrows():
            print(f"""\nID: {linha["Product_ID"]} | Qtd: {linha["Quantidade"]} | Origem: {linha["Origem"]} 
                  | Motivo: {linha["Motivo"]}""")
    elif funcao == "Remover":
        #Verifica se o produto_id está em alguma linha
        if produto_id in df["Product_ID"].values:
            #Retorna a linha e o caminho
            return json_file
    #Salva o arquivo para não perder as modificações
    df.to_json(json_file, orient="records", indent=4)