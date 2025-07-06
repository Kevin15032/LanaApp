from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.estatus_envios import EstatusEnvio
from app.schemas.estatus_envios import EstatusEnvioCreate, EstatusEnvioOut

router = APIRouter()

@router.get("/estatusEnvios", response_model=list[EstatusEnvioOut])
def listar_estatus_envios(db: Session = Depends(get_db)):
    return db.query(EstatusEnvio).all()

@router.get("/estatusEnvio", response_model=EstatusEnvioOut)
def obtener_estatus_envio(id: int = Query(...), db: Session = Depends(get_db)):
    estatus = db.query(EstatusEnvio).filter(EstatusEnvio.id == id).first()
    if not estatus:
        raise HTTPException(status_code=404, detail="Estatus de envío no encontrado")
    return estatus

@router.post("/estatusEnvio", response_model=EstatusEnvioOut)
def crear_estatus_envio(data: EstatusEnvioCreate, db: Session = Depends(get_db)):
    nuevo = EstatusEnvio(**data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.put("/estatusEnvio", response_model=EstatusEnvioOut)
def actualizar_estatus_envio(id: int = Query(...), data: EstatusEnvioCreate = None, db: Session = Depends(get_db)):
    estatus = db.query(EstatusEnvio).filter(EstatusEnvio.id == id).first()
    if not estatus:
        raise HTTPException(status_code=404, detail="Estatus de envío no encontrado")
    estatus.nombre = data.nombre
    db.commit()
    return estatus

@router.delete("/estatusEnvio")
def eliminar_estatus_envio(id: int = Query(...), db: Session = Depends(get_db)):
    estatus = db.query(EstatusEnvio).filter(EstatusEnvio.id == id).first()
    if not estatus:
        raise HTTPException(status_code=404, detail="Estatus de envío no encontrado")
    db.delete(estatus)
    db.commit()
    return {"ok": True}
