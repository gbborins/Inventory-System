from Estoque.EstoqueNovo import Storage
from Estoque.EstoqueLista import DataStorage
def Estoque():
    produto_id = input("Qual o ID do produto? ")
    #Verifica o CNPJ
    quantidade = input("Qual a quantidade do produto? ")
    origem = input("Qual a origem do produto? ")
    motivo = input("Qual o motivo do produto? ")
    #Cria um objeto com as espeficicações do fornecedor
    NovoEstoque = Storage(produto_id,quantidade,origem,motivo)
    DataStorage("Cadastro",NovoEstoque.produto_id,NovoEstoque.quantidade,
                 NovoEstoque.origem,NovoEstoque.motivo)