from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from app.schemas import UnidadeConsumidora, UnidadeConsumidoraOpcional, UnidadeConsumidoraReposta
from sqlalchemy.orm.session import Session
from app.database import get_db
from app import models

router = APIRouter()

@router.get("/", response_model=List[UnidadeConsumidoraReposta])
def get(db: Session = Depends(get_db)):
    return [unidade.__dict__ for unidade in db.query(models.UnidadeConsumidora).all()]

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=UnidadeConsumidoraReposta)
def get_id(id:int, db: Session = Depends(get_db)):
    unidade = db.query(models.UnidadeConsumidora).filter(models.UnidadeConsumidora.id == id).first()
    if not unidade:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unidade Consumidora não encontrado")
    return unidade.__dict__

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UnidadeConsumidoraReposta)
def post(unidade: UnidadeConsumidora, db: Session = Depends(get_db)):
    db_item = models.UnidadeConsumidora(**unidade.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item.__dict__

@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=UnidadeConsumidoraReposta)
def put(id:int, unidade:UnidadeConsumidora, db: Session = Depends(get_db)):
    unidade_db = db.query(models.UnidadeConsumidora).filter(models.UnidadeConsumidora.id == id)
    if not unidade_db.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unidade Consumidora não encontrado")
    unidade_db.update(unidade.__dict__)
    db.commit()
    return unidade_db.first().__dict__

@router.patch("/{id}", status_code=status.HTTP_200_OK, response_model=UnidadeConsumidoraReposta)
def patch(id:int, unidade:UnidadeConsumidoraOpcional, db: Session = Depends(get_db)):
    unidade_db = db.query(models.UnidadeConsumidora).filter(models.UnidadeConsumidora.id == id)
    if not unidade_db.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unidade Consumidora não encontrado")
    usuario_dict = {}
    for key in unidade.__dict__.keys():
        if unidade.__dict__.get(key) or isinstance(unidade.__dict__.get(key), int):
            usuario_dict[key] = unidade.__dict__.get(key)
    unidade_db.update(usuario_dict)
    db.commit()
    return unidade_db.first().__dict__

@router.delete("/{id}", status_code=status.HTTP_200_OK, response_model=UnidadeConsumidoraReposta)
def delete(id:int, db: Session = Depends(get_db)):
    unidade_db = db.query(models.UnidadeConsumidora).filter(models.UnidadeConsumidora.id == id)
    if not unidade_db.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unidade Consumidora não encontrado")
    usuario_dict = unidade_db.first().__dict__
    unidade_db.delete()
    db.commit()
    return usuario_dict
