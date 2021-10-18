from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from app.schemas import FaturaCliente, FaturaClienteOpcional, FaturaClienteResposta
from sqlalchemy.orm.session import Session
from app.database import get_db
from app import models

router = APIRouter()

@router.get("/", response_model=List[FaturaClienteResposta])
def get(db: Session = Depends(get_db)):
    return [unidade.__dict__ for unidade in db.query(models.FaturaCliente).all()]

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=FaturaClienteResposta)
def get_id(id:int, db: Session = Depends(get_db)):
    fatura = db.query(models.FaturaCliente).filter(models.FaturaCliente.id == id).first()
    if not fatura:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Fatura Cliente não encontrada")
    return fatura.__dict__

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=FaturaClienteResposta)
def post(fatura: FaturaCliente, db: Session = Depends(get_db)):
    db_item = models.FaturaCliente(**fatura.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item.__dict__

@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=FaturaClienteResposta)
def put(id:int, fatura:FaturaCliente, db: Session = Depends(get_db)):
    fatura_db = db.query(models.FaturaCliente).filter(models.FaturaCliente.id == id)
    if not fatura_db.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Fatura Cliente não encontrada")
    fatura_db.update(fatura.__dict__)
    db.commit()
    return fatura_db.first().__dict__

@router.patch("/{id}", status_code=status.HTTP_200_OK, response_model=FaturaClienteResposta)
def patch(id:int, fatura:FaturaClienteOpcional, db: Session = Depends(get_db)):
    fatura_db = db.query(models.FaturaCliente).filter(models.FaturaCliente.id == id)
    if not fatura_db.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Fatura Cliente não encontrada")
    usuario_dict = {}
    for key in fatura.__dict__.keys():
        if fatura.__dict__.get(key):
            usuario_dict[key] = fatura.__dict__.get(key)
    fatura_db.update(usuario_dict)
    db.commit()
    return fatura_db.first().__dict__

@router.delete("/{id}", status_code=status.HTTP_200_OK, response_model=FaturaClienteResposta)
def delete(id:int, db: Session = Depends(get_db)):
    fatura_db = db.query(models.FaturaCliente).filter(models.FaturaCliente.id == id)
    if not fatura_db.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unidade Consumidora não encontrada")
    fatura_dict = fatura_db.first().__dict__
    fatura_db.delete()
    db.commit()
    return fatura_dict

