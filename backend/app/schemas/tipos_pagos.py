from pydantic import BaseModel

class TipoPagoBase(BaseModel):
    nombre: str

class TipoPagoCreate(TipoPagoBase):
    pass

class TipoPagoOut(TipoPagoBase):
    id: int

    class Config:
        orm_mode = True
