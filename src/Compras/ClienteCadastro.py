from Clientes.ClienteNovo import Client
from Clientes.ClienteLista import DataClient
def Clientes():
    nome = input("Qual o nome do cliente? ")
    Cpf = input("Qual o CPF do cliente? ")
    email = input("Qual o email do cliente? ")
    telefone = input("Qual o telefone do cliente? ")
    endereco = input("Qual o endereco do cliente? ")

    NovoCliente = Client(nome=nome,Cpf=Cpf,email=email,telefone=telefone,endereco=endereco)
    DataClient("Cadastro",NovoCliente.nome,
                 NovoCliente.Cpf,NovoCliente.email, NovoCliente.telefone,
                 NovoCliente.endereco)