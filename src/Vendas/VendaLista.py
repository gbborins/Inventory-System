#Fornecedores listados
import pandas as pd
from pathlib import Path
def DataSale(funcao,cliente_id = None,nome = None, Cpf = None,
                email = None, telefone = None, endereco = None):
    path = Path(input("Digite o nome do arquivo JSON: "))
    json_file = Path(__file__).parent / path
    #verifica se o caminho já existe
    if not Path.exists(json_file):
        #Se não existir cria um novo
        df = pd.DataFrame(columns=[
        "Cliente_ID",
        "Nome",
        "CPF",
        "Email",
        "Telefone",
        "Endereco"
        ])
    elif Path(json_file).stat().st_size > 0:
        #Lê um arquivo json
        df = pd.read_json(json_file)
        if df.empty:
            df = pd.DataFrame(columns=[
            "Cliente_ID",
            "Nome",
            "CPF",
            "Email",
            "Telefone",
            "Endereco"
        ])
    if funcao == "Cadastro": 
        #Escreve no arquivo json
        if cliente_id not in df["Cliente_ID"].values:
            #Adiciona uma nova linha com os valores
            df.loc[len(df)] = [cliente_id,nome,Cpf,email,telefone,endereco]
            print(f"\nCliente {cliente_id} cadastrado com sucesso")
        else:
            linha = df[df["Cliente_ID"] == cliente_id].index[0]
            #Substitui o novo nome
            if df.loc[linha,"Nome"] != nome:
                df.loc[linha,"Nome"] = nome
                print("\nO nome mudou")
            if df.loc[linha,"CPF"] != Cpf:
                df.loc[linha,"CPF"] = Cpf
                print("\nO Cpf mudou")
            if df.loc[linha,"Email"] != email:
                df.loc[linha,"Email"] = email
                print("\nO email mudou")
            if df.loc[linha,"Telefone"] != telefone:
                df.loc[linha,"Telefone"] = telefone
                print("\nO telefone mudou")
            if df.loc[linha,"Endereco"] != endereco:
                df.loc[linha,"Endereco"] = endereco
                print("\nO endereco mudou")
    elif funcao == "Buscar":
        #Verifica se o cliente_id está em alguma linha
        if cliente_id in df["Cliente_ID"].values:
            #Obtém a linha em que o cliente_id é encontrado
            linha = df[df["Cliente_ID"] == cliente_id].index[0]
            return [df.loc[linha,"Nome"],df.loc[linha,"CPF"],
                    df.loc[linha,"Email"],df.loc[linha,"Telefone"],
                    df.loc[linha,"endereco"]]
        else:
            return False
    elif funcao == "Lista":
        for _,linha in df.iterrows():
            print(f"""\nID: {linha["Cliente_ID"]} | Nome: {linha["Nome"]} | CPF: {linha["CPF"]} 
                  | Email: {linha["Email"]} | Telefone: {linha["Telefone"]} | Endereco {linha["Endereco"]}""")
    elif funcao == "Remover":
        #Verifica se o cliente_id está em alguma linha
        if cliente_id in df["Cliente_ID"].values:
            #Retorna a linha e o caminho
            return json_file
    #Salva o arquivo para não perder as modificações
    df.to_json(json_file, orient="records", indent=4)