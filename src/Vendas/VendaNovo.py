class Sale:
    #Cria um objeto novo com essas especificações
    def __init__(self,venda_id,cliente_id,data_venda,valor_total, status_pagamento):
        self.venda_id = venda_id
        self.cliente_id = cliente_id
        self.data_venda = data_venda
        self.valor_total = valor_total
        self.status_pagamento = status_pagamento