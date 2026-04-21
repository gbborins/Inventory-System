from pydantic import BaseModel, EmailStr
from typing import Optional
class Provider(BaseModel):
    #Cria um objeto novo com essas especificações
    nome: Optional[str] = None
    cnpj: Optional[str] = None
    email: Optional[EmailStr] = None
    telefone: Optional[str] = None
    endereco: Optional[str] = None
    fornecedor_id: Optional[int] = None
    produto_id: Optional[int] = None
    quant: Optional[int] = None
    preco: Optional[float] = None
    data_compra: Optional[str] = None