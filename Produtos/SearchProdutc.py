from Produtos.ListProduct import DataProduct
def buscar_produto():
    nome = input("Qual o nome do produto? ")
    produto = DataProduct("Buscar",nome)
    if produto:
        print(f"\nO produto {nome} tem os seguintes dado: ")
        print(f"""R${produto[0]} | Qtd: {produto[1]} | Cate: {produto[2]} | Fabri: {produto[3]} | Espe: {produto[4]}""")
    else:
        print(f"Não foi possível achar o produto com nome {nome}")