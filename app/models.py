from sqlalchemy import Column, Integer, String
from .database import Base

class Usuario(Base):
    __tablename__ = "usuario"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    password = Column(String)