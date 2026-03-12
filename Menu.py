from Produtos import CadastroProduto, SearchProdutc, ListProduct, RemoveProduct
from Estoque import CadastroEstoque
from Verify import verification
from Fornecedores import CadastroFornecedores, SearchFornecedor, ListaFornecedores, RemoveProvider
def main():
    print("""
    1: Produtos
    2: Fornecedors
    3: Estoque
    4: Clientes
    5: Compras
    6: Vendas
    7: Pedidos
    8: Logística e Entrega
    9: Financeiro
    """)
    #Repetição das escolhas
    while True:
        #Chama e verifica se é int
        escolha = verification.validation(int,"Escolha uma opção: ",True)
        if escolha == 0:
            break
        if escolha == 1:
            print("""
            1 - Novo Produto
            2 - Procurar Produto
            3 - Lista dos Produtos
            4 - Remover Produto""")
            opcao = verification.validation(int,"Escolha uma opção: ",False)
            if opcao == 1:
                CadastroProduto.Produto()
            elif opcao == 2:
                SearchProdutc.buscar_produto()
            elif opcao == 3:
                ListProduct.DataProduct("Lista")
            elif opcao == 4:
                RemoveProduct.remove_produto()
        elif escolha == 2:
            print("""
            1 - Novo Fornecedor
            2 - Procurar Fornecedor
            3 - Lista dos Fornecedores
            4 - Remover Produto""")
            opcao = verification.validation(int,"Escolha uma opção: ",False)
            if opcao == 1:
                CadastroFornecedores.Fornecedores()
            elif opcao == 2:
                SearchFornecedor.buscar_fornecedor()
            elif opcao == 3:
                ListaFornecedores.DataProvider("Lista")
            elif opcao == 4:
                RemoveProvider.remove_provider()
        elif escolha == 3:
            CadastroEstoque.Estoque()
if __name__ == "__main__":
    main()