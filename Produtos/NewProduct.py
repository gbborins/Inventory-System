class Product:
    #Cria um objeto novo com essas especificações
    def __init__(self,nome,valor,quantidade,categoria,fabricante,especificacao,fornecedor_id):
        self.nome = nome
        self.valor = valor
        self.quantidade = quantidade
        self.categoria = categoria
        self.fabricante = fabricante
        self.especificacao = especificacao
        self.fornecedor_id = fornecedor_id