from Fornecedores.FornecedorNovo import Provider
from Fornecedores.FornecedorLista import DataProvider
def Fornecedores():
    nome_empresa = input("Qual o nome da empresa do fornecedor? ")
    #Verifica o CNPJ
    cnpj = input("Qual o CNPJ da empresa? ")
    telefone = input("Qual o telefone? ")
    email = input("Qual o email? ")
    endereco = input("Qual o endereço? ")
    #Cria um objeto com as espeficicações do fornecedor
    NovoFornecedor = Provider(nome_empresa,cnpj,telefone,email,endereco)
    DataProvider("Cadastro",NovoFornecedor.nome_empresa,NovoFornecedor.cnpj,
                 NovoFornecedor.telefone,NovoFornecedor.email,
                 NovoFornecedor.endereco)