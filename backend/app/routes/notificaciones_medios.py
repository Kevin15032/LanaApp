from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.notificaciones_medios import NotificacionMedio
from app.schemas.notificaciones_medios import NotificacionMedioCreate, NotificacionMedioOut

router = APIRouter()

@router.get("/notificacionesMedios", response_model=List[NotificacionMedioOut])
def listar_medios(notificacion: int = Query(...), db: Session = Depends(get_db)):
    return db.query(NotificacionMedio).filter(NotificacionMedio.notificacion_id == notificacion).all()

@router.post("/notificacionesMedios", response_model=NotificacionMedioOut)
def crear_medio(data: NotificacionMedioCreate, db: Session = Depends(get_db)):
    nuevo = NotificacionMedio(**data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.put("/notificacionesMedios", response_model=NotificacionMedioOut)
def actualizar_medio(id: int = Query(...), data: NotificacionMedioCreate = None, db: Session = Depends(get_db)):
    medio = db.query(NotificacionMedio).filter(NotificacionMedio.id == id).first()
    if not medio:
        raise HTTPException(status_code=404, detail="Medio de notificación no encontrado")
    medio.notificacion_id = data.notificacion_id
    medio.medio = data.medio
    medio.estado_envio = data.estado_envio
    db.commit()
    db.refresh(medio)
    return medio
