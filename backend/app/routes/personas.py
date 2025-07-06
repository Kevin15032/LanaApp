from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.personas import Persona
from app.schemas.personas import PersonaCreate, PersonaOut

router = APIRouter()

@router.get("/personas", response_model=list[PersonaOut])
def listar_personas(db: Session = Depends(get_db)):
    return db.query(Persona).all()

@router.get("/persona", response_model=PersonaOut)
def obtener_persona(id: int = Query(...), db: Session = Depends(get_db)):
    persona = db.query(Persona).filter(Persona.id == id).first()
    if not persona:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    return persona

@router.post("/persona", response_model=PersonaOut)
def crear_persona(data: PersonaCreate, db: Session = Depends(get_db)):
    nueva = Persona(**data.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

@router.put("/persona", response_model=PersonaOut)
def actualizar_persona(id: int = Query(...), data: PersonaCreate = None, db: Session = Depends(get_db)):
    persona = db.query(Persona).filter(Persona.id == id).first()
    if not persona:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    persona.nombre = data.nombre
    persona.ap_paterno = data.ap_paterno
    persona.ap_materno = data.ap_materno
    persona.telefono = data.telefono
    db.commit()
    return persona

@router.delete("/persona")
def eliminar_persona(id: int = Query(...), db: Session = Depends(get_db)):
    persona = db.query(Persona).filter(Persona.id == id).first()
    if not persona:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    db.delete(persona)
    db.commit()
    return {"ok": True}
