
from typing import Optional
from pydantic import BaseModel

class Usuario(BaseModel):
    email: str
    password: str

class UsuarioResposta(Usuario):
    id:int

class UsarioOpcional(BaseModel):
    email: Optional[str] = None
    password: Optional[str] = None

class UnidadeConsumidora(BaseModel):
    numero_identificacao: str
    estado: str
    cidade: str
    bairro: str
    rua: str
    numero: int

class UnidadeConsumidoraReposta(UnidadeConsumidora):
    id: int

class UnidadeConsumidoraOpcional(BaseModel):
    numero_identificacao: Optional[str]
    estado: Optional[str]
    cidade: Optional[str]
    bairro: Optional[str]
    rua: Optional[str]
    numero: Optional[int]
