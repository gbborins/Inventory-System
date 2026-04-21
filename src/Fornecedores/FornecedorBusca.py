from Fornecedores.FornecedorLista import DataProvider
def BuscarFornecedor():
    fornecedor_id = input("Qual o ID do fornecedor? ")
    #Envia o ID do fornecedor para a lista
    fornecedor = DataProvider("Buscar",fornecedor_id = fornecedor_id)
    #Se o fornecedor existir mostra os dados
    if fornecedor:
        print(f"\nA empresa {fornecedor_id} tem os seguintes dado: ")
        print(f"""\nNomeEmpresa: {fornecedor[0]} CNPJ: {fornecedor[1]} | Email: {fornecedor[2]} 
              | Telefone: {fornecedor[3]} | Endereco: {fornecedor[4]}""")
    else:
        print(f"\nNão foi possível achar o fornecedor com ID {fornecedor_id}")