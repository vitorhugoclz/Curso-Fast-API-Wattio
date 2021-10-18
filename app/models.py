from sqlalchemy import Column, Integer, String
from .database import Base

class Usuario(Base):
    __tablename__ = "usuario"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    password = Column(String)

class UnidadeConsumidora(Base):
    __tablename__ = "unidade_consumidora"

    id = Column(Integer, primary_key=True, index=True)
    numero_identificacao = Column(String)
    
    estado = Column(String)
    cidade = Column(String)
    bairro = Column(String)
    rua = Column(String)
    numero = Column(Integer)