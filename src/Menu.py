from Clientes import ClienteBusca, ClienteCadastro, ClienteLista, ClienteRemove, ClienteExportar_csv
from Estoque import EstoqueBusca, EstoqueCadastro, EstoqueLista, EstoqueRemove
from Fornecedores import FornecedorBusca, FornecedorCadastro, FornecedorLista, FornecedorRemove
from Produtos import ProdutoBusca, ProdutoCadastro, ProdutoLista, ProdutoRemove
from Verify.verification import validation
def main():
    print("""
    1: Produtos
    2: Fornecedores
    3: Estoque
    4: Clientes
    5: Compras
    6: Vendas
    7: Pedidos
    8: Logística e Entrega
    9: Financeiro
    10: Relatório
    0: Sair
    """)
    #Repetição das escolhas
    while True:
        #Chama e verifica se é int
        escolha = validation(int,"Escolha uma opção: ",True)
        if escolha == 0:
            break
        if escolha == 1:
            print("""
            1 - Novo Produto
            2 - Procurar Produto
            3 - Lista dos Produtos
            4 - Remover Produto""")
            opcao = validation(int,"Escolha uma opção: ",False)
            if opcao == 1:
                ProdutoCadastro.Produto()
            elif opcao == 2:
                ProdutoBusca.buscar_produto()
            elif opcao == 3:
                ProdutoLista.DataProduct("Lista")
            elif opcao == 4:
                ProdutoRemove.remove_produto()
        elif escolha == 2:
            print("""
            1 - Novo Fornecedor
            2 - Procurar Fornecedor
            3 - Lista dos Fornecedores
            4 - Remover Produto""")
            opcao = validation(int,"Escolha uma opção: ",False)
            if opcao == 1:
                FornecedorCadastro.Fornecedores()
            elif opcao == 2:
                FornecedorBusca.BuscarFornecedor()
            elif opcao == 3:
                FornecedorLista.DataProvider("Lista")
            elif opcao == 4:
                FornecedorRemove.RemoveProvider()
        elif escolha == 3:
            print("""
            1 - Novo Estoque
            2 - Procurar Estoque
            3 - Lista do Estoque
            4 - Remover Estoque""")
            opcao = validation(int,"Escolha uma opção: ",False)
            if opcao == 1:
                EstoqueCadastro.Estoque()
            elif opcao == 2:
                EstoqueBusca.BuscarEstoque()
            elif opcao == 3:
                EstoqueLista.DataStorage("Lista")
            elif opcao == 4:
                EstoqueRemove.RemoveStorage()
        elif escolha == 4:
            print("""
            1 - Novo Cliente
            2 - Procurar Cliente
            3 - Lista de clientes
            4 - Remover Cliente
            5 - Criar Relatório Cliente""")
            opcao = validation(int,"Escolha uma opção: ",False)
            if opcao == 1:
                ClienteCadastro.Clientes()
            elif opcao == 2:
                ClienteBusca.BuscarCliente()
            elif opcao == 3:
                ClienteLista.DataClient("Lista")
            elif opcao == 4:
                ClienteRemove.RemoveClient()
            elif opcao == 5:
                ClienteExportar_csv.Exportar_Cliente()
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
    10: Relatório
    0: Sair
    """)
if __name__ == "__main__":
    main()