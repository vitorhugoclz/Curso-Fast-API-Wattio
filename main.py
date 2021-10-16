from fastapi import FastAPI, status
from typing import List, Optional
from pydantic import BaseModel

app = FastAPI()


base_dados = {1: {"username": "Vitor", "idade": 10},
              2: {"username": "Teste Teste", "idade": 45}}

@app.get("/")
async def root():
    return base_dados

@app.get("/{id}")
def get_id(id:int):
    return base_dados.get(id)

@app.post("/")
def post(username:str, idade:int):
    ultimo_id = list(base_dados.keys())[-1]
    id = ultimo_id + 1
    base_dados[id] = {"username": username, "idade": idade}
    return base_dados[id]

@app.put("/{id}")
def put(id:int, username:str, idade:int):
    informacao_usuario = base_dados.get(id)
    if informacao_usuario:
        informacao_usuario["username"] = username
        informacao_usuario["idade"] = idade
    return informacao_usuario

@app.patch("/{id}")
def patch(id:int, username:Optional[str], idade:Optional[int]):
    informacao_usuario = base_dados.get(id)
    if username:
        informacao_usuario["username"] = username
    if idade:
        informacao_usuario["idade"] = idade
    return informacao_usuario

@app.delete("/{id}")
def delete(id:int):
    base_dados.pop(id)