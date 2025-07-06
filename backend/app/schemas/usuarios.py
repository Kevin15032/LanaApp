from pydantic import BaseModel

class UsuarioBase(BaseModel):
    persona_id: int | None = None
    correo: str
    tipo_usuario_id: int | None = None

class UsuarioCreate(UsuarioBase):
    contrasena: str

class UsuarioOut(UsuarioBase):
    id: int

    class Config:
        orm_mode = True

class LoginRequest(BaseModel):
    correo: str
    contrasena: str

class LoginResponse(BaseModel):
    id: int
    correo: str
    mensaje: str
