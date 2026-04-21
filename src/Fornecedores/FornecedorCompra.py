from Verify.verification import validation
from Fornecedores.FornecedorNovo import Provider
from Fornecedores.FornecedorLista import DataProvider
def PurchaseProvider():
    fornecedor_id = validation(int,"Qual o ID da empresa do fornecedor? ",False)
    produto_id = validation(int,"Qual o ID do produto comprado? ",False)
    quant = validation(int,"Qual a quantidade do produto? ",False)
    preco_unitario_compra = validation(float,"Qual o preco do produto? ",False)
    data_compra = input("Qual a data da compra? ")
    #Cria um objeto com as espeficicações do fornecedor
    NovoFornecedor = Provider(fornecedor_id=fornecedor_id,
                              produto_id=produto_id,quant=quant,
                              preco=preco_unitario_compra,data_compra=data_compra )
    DataProvider("Compra",fornecedor_id = NovoFornecedor.fornecedor_id, 
                 produto_id = NovoFornecedor.produto_id,
                 quant = NovoFornecedor.quant,preco = NovoFornecedor.preco,
                 data_compra = NovoFornecedor.data_compra)