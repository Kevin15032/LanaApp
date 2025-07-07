from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.notificaciones import Notificacion
from app.schemas.notificaciones import NotificacionCreate, NotificacionOut

router = APIRouter()

@router.get("/notificaciones", response_model=List[NotificacionOut])
def listar_notificaciones(usuario: int = Query(...), db: Session = Depends(get_db)):
    return db.query(Notificacion).filter(Notificacion.usuario_id == usuario).all()

@router.get("/notificacion", response_model=NotificacionOut)
def obtener_notificacion(id: int = Query(...), db: Session = Depends(get_db)):
    noti = db.query(Notificacion).filter(Notificacion.id == id).first()
    if not noti:
        raise HTTPException(status_code=404, detail="Notificación no encontrada")
    return noti

@router.post("/notificacion", response_model=NotificacionOut)
def crear_notificacion(data: NotificacionCreate, db: Session = Depends(get_db)):
    nueva = Notificacion(**data.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

@router.put("/notificacion", response_model=NotificacionOut)
def actualizar_notificacion(id: int = Query(...), data: NotificacionCreate = None, db: Session = Depends(get_db)):
    noti = db.query(Notificacion).filter(Notificacion.id == id).first()
    if not noti:
        raise HTTPException(status_code=404, detail="Notificación no encontrada")
    noti.usuario_id = data.usuario_id
    noti.tipo_notificacion_id = data.tipo_notificacion_id
    noti.mensaje = data.mensaje
    noti.pago_id = data.pago_id
    noti.presupuesto_id = data.presupuesto_id
    db.commit()
    db.refresh(noti)
    return noti

@router.delete("/notificacion")
def eliminar_notificacion(id: int = Query(...), db: Session = Depends(get_db)):
    noti = db.query(Notificacion).filter(Notificacion.id == id).first()
    if not noti:
        raise HTTPException(status_code=404, detail="Notificación no encontrada")
    db.delete(noti)
    db.commit()
    return {"ok": True}
