from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.pagos_fijos import PagoFijo
from app.schemas.pagos_fijos import PagoFijoCreate, PagoFijoOut

router = APIRouter()

@router.get("/pagos-fijos", response_model=list[PagoFijoOut])
def listar_pagos_fijos(db: Session = Depends(get_db)):
    return db.query(PagoFijo).all()

@router.get("/pagos-fijos/{id}", response_model=PagoFijoOut)
def obtener_pago_fijo(id: int, db: Session = Depends(get_db)):
    pago = db.query(PagoFijo).filter(PagoFijo.id == id).first()
    if not pago:
        raise HTTPException(status_code=404, detail="Pago fijo no encontrado")
    return pago

@router.post("/pagos-fijos", response_model=PagoFijoOut)
def crear_pago_fijo(data: PagoFijoCreate, db: Session = Depends(get_db)):
    nuevo = PagoFijo(**data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.put("/pagos-fijos/{id}", response_model=PagoFijoOut)
def actualizar_pago_fijo(id: int, data: PagoFijoCreate, db: Session = Depends(get_db)):
    pago = db.query(PagoFijo).filter(PagoFijo.id == id).first()
    if not pago:
        raise HTTPException(status_code=404, detail="Pago fijo no encontrado")
    for key, value in data.dict().items():
        setattr(pago, key, value)
    db.commit()
    return pago

@router.delete("/pagos-fijos/{id}")
def eliminar_pago_fijo(id: int, db: Session = Depends(get_db)):
    pago = db.query(PagoFijo).filter(PagoFijo.id == id).first()
    if not pago:
        raise HTTPException(status_code=404, detail="Pago fijo no encontrado")
    db.delete(pago)
    db.commit()
    return {"ok": True}
