#Fornecedores listados
import pandas as pd
import os
def DataProvider(funcao,nome_empresa = None,cnpj = None,telefone = None,
                email = None,endereco = None):
    path = r"D:\Programacao\Python\Proj2\Fornecedores\lista_fornecedores.json"
    #verifica se o caminho já existe
    if os.path.exists(path) and os.path.getsize(path) > 0:
        #Lê um arquivo json
        df = pd.read_json(path)
        if df.empty:
            df = pd.DataFrame(columns=[
            "Nome_Empresa",
            "CNPJ",
            "Telefone",
            "Email",
            "Endereco"
        ])
    else:
        #Se não existir cria um novo
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
            print(f"Produto {nome_empresa} cadastrado com sucesso")
        else:
            linha = df[df["Nome_Empresa"] == nome_empresa].index[0]
            #Substitui o novo cnpj
            if df.loc[linha,"CNPJ"] != cnpj:
                df.loc[linha,"CNPJ"] = cnpj
                print("O cnpj mudou")
            if df.loc[linha,"Telefone"] != telefone:
                df.loc[linha,"Telefone"] = telefone
                print("O telefone mudou")
            if df.loc[linha,"Email"] != email:
                df.loc[linha,"Email"] = email
                print("O email mudou")
            if df.loc[linha,"Endereco"] != endereco:
                df.loc[linha,"Endereco"] = endereco
                print("O endereco mudou")
    elif funcao == "Buscar":
        #Verifica se o nome_empresa está em alguma linha
        if nome_empresa in df["Nome_Empresa"].values:
            #Obtém a linha em que o nome_empresa é encontrado
            linha = df[df["Nome_Empresa"] == nome_empresa].index[0]
            return [df.loc[linha,"CNPJ"],df.loc[linha,"Telefone"],
                    df.loc[linha,"Email"],df.loc[linha,"endereco"]]
        else:
            return False
    elif funcao == "Lista":
        for _,linha in df.iterrows():
            print(f"""{linha["Nome_Empresa"]} | R${linha["cnpj"]} | Qtd: {linha["Telefone"]} 
                  | Cate: {linha["Email"]} | Fabri: {linha["endereco"]}""")
    elif funcao == "Remover":
        #Verifica se o nome_empresa está em alguma linha
        if nome_empresa in df["Nome_Empresa"].values:
            #Retorna a linha e o caminho
            return path
    #Salva o arquivo para não perder as modificações
    df.to_json(path, orient="records", indent=4)