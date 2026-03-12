class Provider:
    #Cria um objeto novo com essas especificações
    def __init__(self,nome_empresa,cnpj,telefone,email,endereco):
        self.nome_empresa = nome_empresa
        self.cnpj = cnpj
        self.telefone = telefone
        self.email = email
        self.endereco = endereco