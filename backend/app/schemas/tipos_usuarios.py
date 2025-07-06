from pydantic import BaseModel

class TipoUsuarioBase(BaseModel):
    nombre: str

class TipoUsuarioCreate(TipoUsuarioBase):
    pass

class TipoUsuarioOut(TipoUsuarioBase):
    id: int

    class Config:
        orm_mode = True
