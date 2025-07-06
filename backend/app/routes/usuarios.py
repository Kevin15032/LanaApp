from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.usuarios import Usuario
from app.schemas.usuarios import UsuarioCreate, UsuarioOut, LoginRequest, LoginResponse

router = APIRouter()

@router.get("/usuarios", response_model=list[UsuarioOut])
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(Usuario).all()

@router.get("/usuario", response_model=UsuarioOut)
def obtener_usuario(id: int = Query(...), db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.post("/usuario", response_model=UsuarioOut)
def registrar_usuario(data: UsuarioCreate, db: Session = Depends(get_db)):
    nuevo = Usuario(**data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.put("/usuario", response_model=UsuarioOut)
def actualizar_usuario(id: int = Query(...), data: UsuarioCreate = None, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    usuario.persona_id = data.persona_id
    usuario.correo = data.correo
    usuario.contrasena = data.contrasena
    usuario.tipo_usuario_id = data.tipo_usuario_id
    db.commit()
    return usuario

@router.delete("/usuario")
def eliminar_usuario(id: int = Query(...), db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db.delete(usuario)
    db.commit()
    return {"ok": True}

@router.post("/login", response_model=LoginResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(
        Usuario.correo == data.correo,
        Usuario.contrasena == data.contrasena
    ).first()
    if not usuario:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    return LoginResponse(
        id=usuario.id,
        correo=usuario.correo,
        mensaje="Inicio de sesión exitoso"
    )
