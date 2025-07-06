from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.tipos_pagos import TipoPago
from app.schemas.tipos_pagos import TipoPagoCreate, TipoPagoOut

router = APIRouter()

@router.get("/tipos-pagos", response_model=list[TipoPagoOut])
def listar_tipos_pagos(db: Session = Depends(get_db)):
    return db.query(TipoPago).all()

@router.get("/tipos-pagos/{id}", response_model=TipoPagoOut)
def obtener_tipo_pago(id: int, db: Session = Depends(get_db)):
    tipo = db.query(TipoPago).filter(TipoPago.id == id).first()
    if not tipo:
        raise HTTPException(status_code=404, detail="Tipo de pago no encontrado")
    return tipo

@router.post("/tipos-pagos", response_model=TipoPagoOut)
def crear_tipo_pago(data: TipoPagoCreate, db: Session = Depends(get_db)):
    nuevo = TipoPago(**data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.put("/tipos-pagos/{id}", response_model=TipoPagoOut)
def actualizar_tipo_pago(id: int, data: TipoPagoCreate, db: Session = Depends(get_db)):
    tipo = db.query(TipoPago).filter(TipoPago.id == id).first()
    if not tipo:
        raise HTTPException(status_code=404, detail="Tipo de pago no encontrado")
    tipo.nombre = data.nombre
    db.commit()
    return tipo

@router.delete("/tipos-pagos/{id}")
def eliminar_tipo_pago(id: int, db: Session = Depends(get_db)):
    tipo = db.query(TipoPago).filter(TipoPago.id == id).first()
    if not tipo:
        raise HTTPException(status_code=404, detail="Tipo de pago no encontrado")
    db.delete(tipo)
    db.commit()
    return {"ok": True}
