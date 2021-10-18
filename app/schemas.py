
from datetime import date
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
    usuario_id: int


class UnidadeConsumidoraReposta(UnidadeConsumidora):
    id: int


class UnidadeConsumidoraOpcional(BaseModel):
    numero_identificacao: Optional[str]
    estado: Optional[str]
    cidade: Optional[str]
    bairro: Optional[str]
    rua: Optional[str]
    numero: Optional[int]
    usuario_id: int

class FaturaCliente(BaseModel):
    valor_consumo: float
    nome_titular: str
    data_emissao: date
    data_leitura: date
    data_vencimento: date
    energia_consumida: int
    unidade_consumidora_id: int
class FaturaClienteResposta(FaturaCliente):
    id: int

class FaturaClienteOpcional(BaseModel):
    valor_consumo: Optional[float]
    nome_titular: Optional[str]
    data_emissao: Optional[date]
    data_leitura: Optional[date]
    data_vencimento: Optional[date]
    energia_consumida: Optional[int] 
    unidade_consumidora_id: Optional[int] 