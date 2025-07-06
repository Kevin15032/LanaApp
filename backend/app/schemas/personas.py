from pydantic import BaseModel

class PersonaBase(BaseModel):
    nombre: str
    ap_paterno: str | None = None
    ap_materno: str | None = None
    telefono: str | None = None

class PersonaCreate(PersonaBase):
    pass

class PersonaOut(PersonaBase):
    id: int

    class Config:
        orm_mode = True
