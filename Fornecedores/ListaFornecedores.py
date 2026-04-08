#Fornecedores listados
import pandas as pd
from pathlib import Path
def DataProvider(funcao,nome_empresa = None,cnpj = None,telefone = None,
                email = None,endereco = None):
    path = Path(input("Digite o nome do arquivo JSON: "))
    json_file = Path(__file__).parent / path
    #verifica se o caminho já existe
    if not Path.exists(json_file):
        #Se não existir cria um novo
        df = pd.DataFrame(columns=[
        "Nome_Empresa",
        "CNPJ",
        "Telefone",
        "Email",
        "Endereco"
        ])
    elif Path(json_file).stat().st_size > 0:
        #Lê um arquivo json
        df = pd.read_json(json_file)
        if df.empty:
            df = pd.DataFrame(columns=[
            "Nome_Empresa",
            "CNPJ",
            "Telefone",
            "Email",
            "Endereco"
        ])   
    if funcao == "Cadastro": 
        #Escreve no arquivo json
        if nome_empresa not in df["Nome_Empresa"].values:
            #Adiciona uma nova linha com os valores
            df.loc[len(df)] = [nome_empresa,cnpj,telefone,email,endereco]
            print(f"\nProduto {nome_empresa} cadastrado com sucesso")
        else:
            linha = df[df["Nome_Empresa"] == nome_empresa].index[0]
            #Substitui o novo cnpj
            if df.loc[linha,"CNPJ"] != cnpj:
                df.loc[linha,"CNPJ"] = cnpj
                print("\nO cnpj mudou")
            if df.loc[linha,"Telefone"] != telefone:
                df.loc[linha,"Telefone"] = telefone
                print("\nO telefone mudou")
            if df.loc[linha,"Email"] != email:
                df.loc[linha,"Email"] = email
                print("\nO email mudou")
            if df.loc[linha,"Endereco"] != endereco:
                df.loc[linha,"Endereco"] = endereco
                print("\nO endereco mudou")
    elif funcao == "Buscar":
        #Verifica se o nome_empresa está em alguma linha
        if nome_empresa in df["Nome_Empresa"].values:
            #Obtém a linha em que o nome_empresa é encontrado
            linha = df[df["Nome_Empresa"] == nome_empresa].index[0]
            return [df.loc[linha,"CNPJ"],df.loc[linha,"Telefone"],
                    df.loc[linha,"Email"],df.loc[linha,"Endereco"]]
        else:
            return False
    elif funcao == "Lista":
        for _,linha in df.iterrows():
            print(f"""\nNome: {linha["Nome_Empresa"]} | CNPJ: {linha["CNPJ"]} | Telefone: {linha["Telefone"]} 
                  | Email: {linha["Email"]} | Endereço: {linha["Endereco"]}""")
    elif funcao == "Remover":
        #Verifica se o nome_empresa está em alguma linha
        if nome_empresa in df["Nome_Empresa"].values:
            #Retorna a linha e o caminho
            return json_file
    #Salva o arquivo para não perder as modificações
    df.to_json(json_file, orient="records", indent=4)