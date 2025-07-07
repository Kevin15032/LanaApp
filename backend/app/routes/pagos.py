from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.pagos import Pago
from app.schemas.pagos import PagoCreate, PagoOut

router = APIRouter()

@router.get("/pagos", response_model=List[PagoOut])
def listar_pagos(db: Session = Depends(get_db)):
    return db.query(Pago).all()

@router.get("/pago", response_model=PagoOut)
def obtener_pago(id: int = Query(...), db: Session = Depends(get_db)):
    pago = db.query(Pago).filter(Pago.id == id).first()
    if not pago:
        raise HTTPException(status_code=404, detail="Pago no encontrado")
    return pago

@router.post("/pago", response_model=PagoOut)
def crear_pago(data: PagoCreate, db: Session = Depends(get_db)):
    nuevo = Pago(**data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.put("/pago", response_model=PagoOut)
def actualizar_pago(id: int = Query(...), data: PagoCreate = None, db: Session = Depends(get_db)):
    pago = db.query(Pago).filter(Pago.id == id).first()
    if not pago:
        raise HTTPException(status_code=404, detail="Pago no encontrado")
    pago.pago_fijo_id = data.pago_fijo_id
    pago.fecha_programada = data.fecha_programada
    pago.fecha_realizada = data.fecha_realizada
    pago.estatus_id = data.estatus_id
    db.commit()
    db.refresh(pago)
    return pago

@router.delete("/pago")
def eliminar_pago(id: int = Query(...), db: Session = Depends(get_db)):
    pago = db.query(Pago).filter(Pago.id == id).first()
    if not pago:
        raise HTTPException(status_code=404, detail="Pago no encontrado")
    db.delete(pago)
    db.commit()
    return {"ok": True}
