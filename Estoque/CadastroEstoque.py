from Estoque.NewStorage import Storage
from Estoque.ListaStorage import DataStorage
def Estoques():
    produto_id = input("Qual o ID do produto? ")
    #Verifica o CNPJ
    quantidade = input("Qual a quantidade do produto? ")
    origem = input("Qual a origem do produto? ")
    motivo = input("Qual o motivo do produto? ")
    #Cria um objeto com as espeficicações do fornecedor
    NovoEstoque = Storage(produto_id,quantidade,origem,motivo)
    DataStorage("Cadastro",NovoEstoque.produto_id,NovoEstoque.quantidade,
                 NovoEstoque.origem,NovoEstoque.motivo)