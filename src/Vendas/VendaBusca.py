from Vendas.VendaLista import DataSale
def BuscarVenda():
    cliente_id = input("Qual o ID do produto? ")
    #Envia o ID do produto para a lista
    cliente = DataSale("Buscar",cliente_id)
    #Se o produto_id existir mostra os dados
    if cliente:
        print(f"\nO cliente {cliente_id} tem os seguintes dado: ")
        print(f"\nNome: {cliente[0]} | Cpf: {cliente[1]} | Email: {cliente[2]} | Tel: {cliente[3]} | Ende: {cliente[4]}")
    else:
        print(f"\nNão foi possível achar o cliente com ID {cliente_id}")