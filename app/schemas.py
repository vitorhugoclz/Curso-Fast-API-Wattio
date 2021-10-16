
from typing import Optional
from pydantic import BaseModel

class Usuario(BaseModel):
    username: str
    idade: int

class UsuarioResposta(Usuario):
    id:int

class UsarioOpcional(BaseModel):
    username: Optional[str] = None
    idade: Optional[int] = None
