from Produtos.ProdutoLista import DataProduct
def buscar_produto():
    nome = input("Qual o nome do produto? ")
    #Envia o nome do produto para a lista
    produto = DataProduct("Buscar",nome)
    #Se o produto existir mostra os dados
    if produto:
        print(f"\nO produto {nome} tem os seguintes dado: ")
        print(f"""\nR${produto[0]} | Qtd: {produto[1]} | Cate: {produto[2]} 
              | Fabri: {produto[3]} | Espe: {produto[4]} | Forn_id {produto[5]}""")
    else:
        print(f"\nNão foi possível achar o produto com nome {nome}")