from Fornecedores.ListaFornecedores import DataProvider
def buscar_fornecedor():
    nome_empresa = input("Qual o nome da empresa? ")
    #Envia o nome da empresa para a lista
    produto = DataProvider("Buscar",nome_empresa)
    #Se a empresa existir mostra os dados
    if produto:
        print(f"\nA empresa {nome_empresa} tem os seguintes dado: ")
        print(f"""CNPJ: {produto[0]} | Telefone: {produto[1]} | Email: {produto[2]} 
              | Endereco: {produto[3]}""")
    else:
        print(f"Não foi possível achar a empresa com nome {nome_empresa}")