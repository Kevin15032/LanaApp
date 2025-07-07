from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.tipos_notificaciones import TipoNotificacion
from app.schemas.tipos_notificaciones import TipoNotificacionCreate, TipoNotificacionOut

router = APIRouter()

@router.get("/tiposNotificaciones", response_model=List[TipoNotificacionOut])
def listar_tipos_notificaciones(db: Session = Depends(get_db)):
    return db.query(TipoNotificacion).all()

@router.get("/tipoNotificacion", response_model=TipoNotificacionOut)
def obtener_tipo_notificacion(id: int = Query(...), db: Session = Depends(get_db)):
    tipo = db.query(TipoNotificacion).filter(TipoNotificacion.id == id).first()
    if not tipo:
        raise HTTPException(status_code=404, detail="Tipo de notificación no encontrado")
    return tipo

@router.post("/tipoNotificacion", response_model=TipoNotificacionOut)
def crear_tipo_notificacion(data: TipoNotificacionCreate, db: Session = Depends(get_db)):
    nuevo = TipoNotificacion(**data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.put("/tipoNotificacion", response_model=TipoNotificacionOut)
def actualizar_tipo_notificacion(id: int = Query(...), data: TipoNotificacionCreate = None, db: Session = Depends(get_db)):
    tipo = db.query(TipoNotificacion).filter(TipoNotificacion.id == id).first()
    if not tipo:
        raise HTTPException(status_code=404, detail="Tipo de notificación no encontrado")
    tipo.nombre = data.nombre
    db.commit()
    db.refresh(tipo)
    return tipo

@router.delete("/tipoNotificacion")
def eliminar_tipo_notificacion(id: int = Query(...), db: Session = Depends(get_db)):
    tipo = db.query(TipoNotificacion).filter(TipoNotificacion.id == id).first()
    if not tipo:
        raise HTTPException(status_code=404, detail="Tipo de notificación no encontrado")
    db.delete(tipo)
    db.commit()
    return {"ok": True}
