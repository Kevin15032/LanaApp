from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.estatus import Estatus
from app.schemas.estatus import EstatusCreate, EstatusOut

router = APIRouter()

@router.get("/estatus", response_model=list[EstatusOut])
def listar_estatus(db: Session = Depends(get_db)):
    return db.query(Estatus).all()

@router.get("/estatus/{id}", response_model=EstatusOut)
def obtener_estatus(id: int, db: Session = Depends(get_db)):
    estatus = db.query(Estatus).filter(Estatus.id == id).first()
    if not estatus:
        raise HTTPException(status_code=404, detail="Estatus no encontrado")
    return estatus

@router.post("/estatus", response_model=EstatusOut)
def crear_estatus(data: EstatusCreate, db: Session = Depends(get_db)):
    nuevo = Estatus(**data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.put("/estatus/{id}", response_model=EstatusOut)
def actualizar_estatus(id: int, data: EstatusCreate, db: Session = Depends(get_db)):
    estatus = db.query(Estatus).filter(Estatus.id == id).first()
    if not estatus:
        raise HTTPException(status_code=404, detail="Estatus no encontrado")
    estatus.nombre = data.nombre
    db.commit()
    return estatus

@router.delete("/estatus/{id}")
def eliminar_estatus(id: int, db: Session = Depends(get_db)):
    estatus = db.query(Estatus).filter(Estatus.id == id).first()
    if not estatus:
        raise HTTPException(status_code=404, detail="Estatus no encontrado")
    db.delete(estatus)
    db.commit()
    return {"ok": True}
