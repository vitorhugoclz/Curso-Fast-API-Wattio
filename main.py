from fastapi import FastAPI, status
from typing import List
from schemas import Usuario, UsuarioResposta, UsarioOpcional
app = FastAPI()

base_dados = {1: {"id": 1, "username": "Vitor", "idade": 10},
              2: {"id": 2, "username": "Teste Teste", "idade": 45}}

@app.get("/", response_model=List[UsuarioResposta])
def root():
    return list(base_dados.values())

@app.get("/{id}", status_code=status.HTTP_200_OK, response_model=UsuarioResposta)
def get_id(id:int):
    return base_dados.get(id)

@app.post("/", status_code=status.HTTP_201_CREATED, response_model=UsuarioResposta)
def post(usuario: Usuario):
    ultimo_id = list(base_dados.keys())[-1]
    id = ultimo_id + 1
    base_dados[id] = {"id": id, "username": usuario.username, "idade": usuario.idade}
    return base_dados[id]

@app.put("/{id}", status_code=status.HTTP_200_OK, response_model=UsuarioResposta)
def put(id:int, usuario:Usuario):
    informacao_usuario = base_dados.get(id)
    if informacao_usuario:
        informacao_usuario["username"] = usuario.username
        informacao_usuario["idade"] = usuario.idade
    return informacao_usuario

@app.patch("/{id}", status_code=status.HTTP_200_OK, response_model=UsuarioResposta)
def patch(id:int, usuario:UsarioOpcional):
    informacao_usuario = base_dados.get(id)
    if usuario.username:
        informacao_usuario["username"] = usuario.username
    if usuario.idade != None:
        informacao_usuario["idade"] = usuario.idade
    return informacao_usuario

@app.delete("/{id}", status_code=status.HTTP_200_OK, response_model=UsuarioResposta)
def delete(id:int):
    informacao_usuario = base_dados.pop(id)
    return informacao_usuario