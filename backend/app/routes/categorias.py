from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.categorias import Categoria
from app.schemas.categorias import CategoriaCreate, CategoriaOut

router = APIRouter()

@router.get("/categorias", response_model=list[CategoriaOut])
def listar_categorias(db: Session = Depends(get_db)):
    return db.query(Categoria).all()

@router.get("/categoria", response_model=CategoriaOut)
def obtener_categoria(id: int = Query(...), db: Session = Depends(get_db)):
    categoria = db.query(Categoria).filter(Categoria.id == id).first()
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return categoria

@router.post("/categoria", response_model=CategoriaOut)
def crear_categoria(data: CategoriaCreate, db: Session = Depends(get_db)):
    nueva = Categoria(**data.dict())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

@router.put("/categoria", response_model=CategoriaOut)
def actualizar_categoria(id: int = Query(...), data: CategoriaCreate = None, db: Session = Depends(get_db)):
    categoria = db.query(Categoria).filter(Categoria.id == id).first()
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    categoria.nombre = data.nombre
    db.commit()
    return categoria

@router.delete("/categoria")
def eliminar_categoria(id: int = Query(...), db: Session = Depends(get_db)):
    categoria = db.query(Categoria).filter(Categoria.id == id).first()
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    db.delete(categoria)
    db.commit()
    return {"ok": True}
