from fastapi import FastAPI
from app.database import engine
from app import models
from app.routers import usuario, unidade_consumidora, fatura_cliente


app = FastAPI()

base_dados = {1: {"id": 1, "username": "Vitor", "idade": 10},
              2: {"id": 2, "username": "Teste Teste", "idade": 45}}

models.Base.metadata.create_all(bind=engine)

app.include_router(usuario.router,prefix="/usuario", tags=["Usuario"])
app.include_router(unidade_consumidora.router,prefix="/unidade_consumidora", tags=["Unidade Consumidora"])
app.include_router(fatura_cliente.router, prefix="/fatura_cliente", tags=["Fatura Cliente"])