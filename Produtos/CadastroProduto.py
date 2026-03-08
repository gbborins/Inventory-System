from Produtos.NewProduct import Product
from Produtos.ListProduct import DataProduct
from Verify import verification
def Produto():
    nome = input("Qual o nome do produto? ")
    #Verifica o valor e quantidade
    valor = verification.validation(float,"Qual o valor do produto? ")
    quantidade = verification.validation(int,"Qual a quantidade do produto? ")
    #A categoria do produto, seu fabricante e especificações técnicas
    categoria = input("Qual a categoria do produto? ")
    fabricante = input("Qual o fabricante do produto? ")
    especificacao = input("Quais as especificações técnicas? ")
    #Cria um objeto com as espeficicações do produto
    NovoProduto = Product(nome,valor,quantidade,categoria,fabricante,especificacao)
    #Envia para o leitor de JSON para guardar os dados
    DataProduct("Cadastro",NovoProduto.nome,NovoProduto.valor,
                NovoProduto.quantidade,NovoProduto.categoria,
                NovoProduto.fabricante,NovoProduto.especificacao)