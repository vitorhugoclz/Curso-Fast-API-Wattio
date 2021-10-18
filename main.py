from fastapi import FastAPI, status, Depends, HTTPException
from typing import List
from app.schemas import Usuario, UsuarioResposta, UsarioOpcional
from app.database import engine, get_db
from app import models
from app.routers import usuario, unidade_consumidora

from sqlalchemy.orm import Session


app = FastAPI()

base_dados = {1: {"id": 1, "username": "Vitor", "idade": 10},
              2: {"id": 2, "username": "Teste Teste", "idade": 45}}

models.Base.metadata.create_all(bind=engine)

app.include_router(usuario.router,prefix="/usuario", tags=["Usuario"])
app.include_router(unidade_consumidora.router,prefix="/unidade_consumidora", tags=["Unidade Consumidora"])