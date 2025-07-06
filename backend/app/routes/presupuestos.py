from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.presupuestos import Presupuesto
from app.schemas.presupuestos import PresupuestoCreate, PresupuestoOut

router = APIRouter()

@router.get("/presupuestos", response_model=list[PresupuestoOut])
def listar_presupuestos(db: Session = Depends(get_db)):
    return db.query(Presupuesto).all()

@router.get("/presupuestos/{id}", response_model=PresupuestoOut)
def obtener_presupuesto(id: int, db: Session = Depends(get_db)):
    presupuesto = db.query(Presupuesto).filter(Presupuesto.id == id).first()
    if not presupuesto:
        raise HTTPException(status_code=404, detail="Presupuesto no encontrado")
    return presupuesto

@router.post("/presupuestos", response_model=PresupuestoOut)
def crear_presupuesto(data: PresupuestoCreate, db: Session = Depends(get_db)):
    nuevo = Presupuesto(**data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.put("/presupuestos/{id}", response_model=PresupuestoOut)
def actualizar_presupuesto(id: int, data: PresupuestoCreate, db: Session = Depends(get_db)):
    presupuesto = db.query(Presupuesto).filter(Presupuesto.id == id).first()
    if not presupuesto:
        raise HTTPException(status_code=404, detail="Presupuesto no encontrado")
    for key, value in data.dict().items():
        setattr(presupuesto, key, value)
    db.commit()
    return presupuesto

@router.delete("/presupuestos/{id}")
def eliminar_presupuesto(id: int, db: Session = Depends(get_db)):
    presupuesto = db.query(Presupuesto).filter(Presupuesto.id == id).first()
    if not presupuesto:
        raise HTTPException(status_code=404, detail="Presupuesto no encontrado")
    db.delete(presupuesto)
    db.commit()
    return {"ok": True}
