from Fornecedores.FornecedorNovo import Provider
from Fornecedores.FornecedorLista import DataProvider
def Fornecedores():
    nome_empresa = input("Qual o nome da empresa do fornecedor? ")
    #Verifica o CNPJ
    cnpj = input("Qual o CNPJ da empresa? ")
    email = input("Qual o email? ")
    telefone = input("Qual o telefone? ")
    endereco = input("Qual o endereço? ")
    #Cria um objeto com as espeficicações do fornecedor
    NovoFornecedor = Provider(nome=nome_empresa,cnpj=cnpj,email=email,telefone=telefone,endereco=endereco)
    DataProvider("Cadastro",NovoFornecedor.nome,NovoFornecedor.cnpj,
                 NovoFornecedor.email,NovoFornecedor.telefone,
                 NovoFornecedor.endereco)