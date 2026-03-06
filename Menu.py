from Produtos import CadastroProduto
from Estoque import CadastroEstoque
from Verify import verification
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
            CadastroProduto.Produto()
        elif escolha == 2:
            break
        elif escolha == 3:
            CadastroEstoque.Estoque()
if __name__ == "__main__":
    main()