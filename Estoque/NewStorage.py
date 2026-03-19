class Storage:
    #Cria um objeto novo com essas especificações
    def __init__(self,produto_id,quantidade,origem,motivo):
        self.produto_id = produto_id
        self.quantidade = quantidade
        self.origem = origem
        self.motivo = motivo