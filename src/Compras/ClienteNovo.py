from pydantic import BaseModel, EmailStr
from typing import Optional
class Client(BaseModel):
    nome: Optional[str] = None
    Cpf: Optional[str] = None
    email: Optional[EmailStr] = None
    telefone: Optional[str] = None
    endereco: Optional[str] = None