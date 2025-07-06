from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.tipos_usuarios import TipoUsuario
from app.schemas.tipos_usuarios import TipoUsuarioCreate, TipoUsuarioOut

router = APIRouter()

@router.get("/tiposUsuarios", response_model=list[TipoUsuarioOut])
def listar_tipos_usuarios(db: Session = Depends(get_db)):
    return db.query(TipoUsuario).all()

@router.get("/tipoUsuario", response_model=TipoUsuarioOut)
def obtener_tipo_usuario(id: int = Query(...), db: Session = Depends(get_db)):
    tipo = db.query(TipoUsuario).filter(TipoUsuario.id == id).first()
    if not tipo:
        raise HTTPException(status_code=404, detail="Tipo de usuario no encontrado")
    return tipo

@router.post("/tipoUsuario", response_model=TipoUsuarioOut)
def crear_tipo_usuario(data: TipoUsuarioCreate, db: Session = Depends(get_db)):
    nuevo = TipoUsuario(**data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.put("/tipoUsuario", response_model=TipoUsuarioOut)
def actualizar_tipo_usuario(id: int = Query(...), data: TipoUsuarioCreate = None, db: Session = Depends(get_db)):
    tipo = db.query(TipoUsuario).filter(TipoUsuario.id == id).first()
    if not tipo:
        raise HTTPException(status_code=404, detail="Tipo de usuario no encontrado")
    tipo.nombre = data.nombre
    db.commit()
    return tipo

@router.delete("/tipoUsuario")
def eliminar_tipo_usuario(id: int = Query(...), db: Session = Depends(get_db)):
    tipo = db.query(TipoUsuario).filter(TipoUsuario.id == id).first()
    if not tipo:
        raise HTTPException(status_code=404, detail="Tipo de usuario no encontrado")
    db.delete(tipo)
    db.commit()
    return {"ok": True}
