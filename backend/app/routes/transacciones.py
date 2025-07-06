from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import date
from app.database import get_db
from app.models.transacciones import Transaccion
from app.schemas.transacciones import TransaccionCreate, TransaccionOut

router = APIRouter()

@router.get("/transacciones", response_model=List[TransaccionOut])
def listar_transacciones(
    usuario_id: Optional[int] = None,
    categoria_id: Optional[int] = None,
    fecha_inicio: Optional[date] = None,
    fecha_fin: Optional[date] = None,
    db: Session = Depends(get_db)
):
    query = db.query(Transaccion)
    if usuario_id is not None:
        query = query.filter(Transaccion.usuario_id == usuario_id)
    if categoria_id is not None:
        query = query.filter(Transaccion.categoria_id == categoria_id)
    if fecha_inicio is not None:
        query = query.filter(Transaccion.fecha >= fecha_inicio)
    if fecha_fin is not None:
        query = query.filter(Transaccion.fecha <= fecha_fin)
    return query.all()

@router.get("/transaccion", response_model=TransaccionOut)
def obtener_transaccion(id: int = Query(...), db: Session = Depends(get_db)):
    transaccion = db.query(Transaccion).filter(Transaccion.id == id).first()
    if not transaccion:
        raise HTTPException(status_code=404, detail="Transacción no encontrada")
    return transaccion

@router.post("/transaccion", response_model=TransaccionOut)
def crear_transaccion(data: TransaccionCreate, db: Session = Depends(get_db)):
    nueva = Transaccion(**data.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

@router.put("/transaccion", response_model=TransaccionOut)
def actualizar_transaccion(id: int = Query(...), data: TransaccionCreate = None, db: Session = Depends(get_db)):
    transaccion = db.query(Transaccion).filter(Transaccion.id == id).first()
    if not transaccion:
        raise HTTPException(status_code=404, detail="Transacción no encontrada")
    transaccion.usuario_id = data.usuario_id
    transaccion.monto = data.monto
    transaccion.categoria_id = data.categoria_id
    transaccion.fecha = data.fecha
    transaccion.concepto = data.concepto
    transaccion.estatus_id = data.estatus_id
    transaccion.tipo_transaccion_id = data.tipo_transaccion_id
    db.commit()
    return transaccion

@router.delete("/transaccion")
def eliminar_transaccion(id: int = Query(...), db: Session = Depends(get_db)):
    transaccion = db.query(Transaccion).filter(Transaccion.id == id).first()
    if not transaccion:
        raise HTTPException(status_code=404, detail="Transacción no encontrada")
    db.delete(transaccion)
    db.commit()
    return {"ok": True}
