from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship

class Usuario(Base):
    __tablename__ = "usuario"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    password = Column(String)

    unidades_consumidoras = relationship("UnidadeConsumidora", back_populates="usuario")


class UnidadeConsumidora(Base):
    __tablename__ = "unidade_consumidora"

    id = Column(Integer, primary_key=True, index=True)
    numero_identificacao = Column(String)
    
    estado = Column(String)
    cidade = Column(String)
    bairro = Column(String)
    rua = Column(String)
    numero = Column(Integer)

    usuario_id = Column(Integer, ForeignKey("usuario.id"))
    usuario = relationship("Usuario", back_populates="unidades_consumidoras")
    faturas_clientes = relationship("FaturaCliente", back_populates="unidade_consumidora")

class FaturaCliente(Base):
    __tablename__ = "fatura_cliente"

    id = Column(Integer, primary_key=True, index=True)
    valor_consumo = Column(Float)
    nome_titular = Column(String)
    data_emissao = Column(Date)
    data_leitura = Column(Date)
    data_vencimento = Column(Date)
    energia_consumida = Column(Integer)

    unidade_consumidora_id = Column(Integer, ForeignKey("unidade_consumidora.id"))
    unidade_consumidora = relationship("UnidadeConsumidora", back_populates="faturas_clientes")