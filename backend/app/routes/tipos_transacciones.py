from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.tipos_transacciones import TipoTransaccion
from app.schemas.tipos_transacciones import (
    TipoTransaccionCreate, TipoTransaccionOut
)

router = APIRouter()

@router.get("/tipos-transacciones", response_model=list[TipoTransaccionOut])
def listar_tipos_transacciones(db: Session = Depends(get_db)):
    return db.query(TipoTransaccion).all()

@router.get("/tipos-transacciones/{id}", response_model=TipoTransaccionOut)
def obtener_tipo_transaccion(id: int, db: Session = Depends(get_db)):
    tipo = db.query(TipoTransaccion).filter(TipoTransaccion.id == id).first()
    if not tipo:
        raise HTTPException(status_code=404, detail="Tipo de transacción no encontrado")
    return tipo

@router.post("/tipos-transacciones", response_model=TipoTransaccionOut)
def crear_tipo_transaccion(data: TipoTransaccionCreate, db: Session = Depends(get_db)):
    nuevo = TipoTransaccion(**data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.put("/tipos-transacciones/{id}", response_model=TipoTransaccionOut)
def actualizar_tipo_transaccion(id: int, data: TipoTransaccionCreate, db: Session = Depends(get_db)):
    tipo = db.query(TipoTransaccion).filter(TipoTransaccion.id == id).first()
    if not tipo:
        raise HTTPException(status_code=404, detail="Tipo de transacción no encontrado")
    tipo.nombre = data.nombre
    db.commit()
    return tipo

@router.delete("/tipos-transacciones/{id}")
def eliminar_tipo_transaccion(id: int, db: Session = Depends(get_db)):
    tipo = db.query(TipoTransaccion).filter(TipoTransaccion.id == id).first()
    if not tipo:
        raise HTTPException(status_code=404, detail="Tipo de transacción no encontrado")
    db.delete(tipo)
    db.commit()
    return {"ok": True}
