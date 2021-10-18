from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm.session import Session
from app import models
from app.database import get_db

from app.schemas import UsarioOpcional, Usuario, UsuarioResposta

router = APIRouter()

@router.get("/", response_model=List[UsuarioResposta])
def get(db: Session = Depends(get_db)):
    return [usuario.__dict__ for usuario in db.query(models.Usuario).all()]

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=UsuarioResposta)
def get_id(id:int, db: Session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter(models.Usuario.id == id).first()
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario não encontrado")
    return usuario.__dict__

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UsuarioResposta)
def post(usuario: Usuario, db: Session = Depends(get_db)):
    db_item = models.Usuario(**usuario.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item.__dict__

@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=UsuarioResposta)
def put(id:int, usuario:Usuario, db: Session = Depends(get_db)):
    usuario_db = db.query(models.Usuario).filter(models.Usuario.id == id)
    if not usuario_db.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario não encontrado")
    usuario_db.update(usuario.__dict__)
    db.commit()
    return usuario_db.first().__dict__

@router.patch("/{id}", status_code=status.HTTP_200_OK, response_model=UsuarioResposta)
def patch(id:int, usuario:UsarioOpcional, db: Session = Depends(get_db)):
    usuario_db = db.query(models.Usuario).filter(models.Usuario.id == id)
    if not usuario_db.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario não encontrado")
    usuario_dict = {}
    for key in usuario.__dict__.keys():
        if usuario.__dict__.get(key) or isinstance(usuario.__dict__.get(key), int):
            usuario_dict[key] = usuario.__dict__.get(key)
    usuario_db.update(usuario_dict)
    db.commit()
    return usuario_db.first().__dict__

@router.delete("/{id}", status_code=status.HTTP_200_OK, response_model=UsuarioResposta)
def delete(id:int, db: Session = Depends(get_db)):
    usuario_db = db.query(models.Usuario).filter(models.Usuario.id == id)
    if not usuario_db.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario não encontrado")
    usuario_dict = usuario_db.first().__dict__
    usuario_db.delete()
    db.commit()
    return usuario_dict