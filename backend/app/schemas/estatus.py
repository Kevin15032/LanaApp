from pydantic import BaseModel

class EstatusBase(BaseModel):
    nombre: str

class EstatusCreate(EstatusBase):
    pass

class EstatusOut(EstatusBase):
    id: int

    class Config:
        orm_mode = True
