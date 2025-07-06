from pydantic import BaseModel
from datetime import date

class TransaccionBase(BaseModel):
    usuario_id: int
    monto: float
    categoria_id: int
    fecha: date
    concepto: str | None = None
    estatus_id: int
    tipo_transaccion_id: int

class TransaccionCreate(TransaccionBase):
    pass

class TransaccionOut(TransaccionBase):
    id: int

    class Config:
        orm_mode = True
