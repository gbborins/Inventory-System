from Vendas.VendaNovo import Sale
from Vendas.VendaLista import DataSale
def Vendas():
    cliente_id = input("Qual o ID do cliente? ")
    nome = input("Qual o nome do cliente? ")
    Cpf = input("Qual o CPF do cliente? ")
    email = input("Qual o email do cliente? ")
    telefone = input("Qual o telefone do cliente? ")
    endereco = input("Qual o endereco do cliente? ")

    NovoCliente = Sale(cliente_id,nome,Cpf,email,telefone,endereco)
    DataSale("Cadastro",NovoCliente.cliente_id,NovoCliente.nome,
                 NovoCliente.Cpf,NovoCliente.email, NovoCliente.telefone,
                 NovoCliente.endereco)