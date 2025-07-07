from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.preferencias_notificaciones import PreferenciaNotificacion
from app.schemas.preferencias_notificaciones import (
    PreferenciaNotificacionCreate,
    PreferenciaNotificacionOut,
)

router = APIRouter()

@router.get("/preferenciasNotificaciones", response_model=PreferenciaNotificacionOut)
def obtener_preferencias(usuario: int = Query(...), db: Session = Depends(get_db)):
    pref = db.query(PreferenciaNotificacion).filter(
        PreferenciaNotificacion.usuario_id == usuario
    ).first()
    if not pref:
        raise HTTPException(status_code=404, detail="Preferencias no encontradas")
    return pref

@router.post("/preferenciasNotificaciones", response_model=PreferenciaNotificacionOut)
def crear_o_actualizar_preferencias(data: PreferenciaNotificacionCreate, db: Session = Depends(get_db)):
    pref = db.query(PreferenciaNotificacion).filter(
        PreferenciaNotificacion.usuario_id == data.usuario_id
    ).first()
    if pref:
        # Si existe, actualiza
        pref.via_sms = data.via_sms
        pref.via_email = data.via_email
        db.commit()
        db.refresh(pref)
        return pref
    else:
        # Si no existe, crea
        nueva = PreferenciaNotificacion(**data.dict())
        db.add(nueva)
        db.commit()
        db.refresh(nueva)
        return nueva

@router.put("/preferenciasNotificaciones", response_model=PreferenciaNotificacionOut)
def actualizar_preferencias(id: int = Query(...), data: PreferenciaNotificacionCreate = None, db: Session = Depends(get_db)):
    pref = db.query(PreferenciaNotificacion).filter(PreferenciaNotificacion.id == id).first()
    if not pref:
        raise HTTPException(status_code=404, detail="Preferencias no encontradas")
    pref.usuario_id = data.usuario_id
    pref.via_sms = data.via_sms
    pref.via_email = data.via_email
    db.commit()
    db.refresh(pref)
    return pref
