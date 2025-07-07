from pydantic import BaseModel
from datetime import date

class PagoBase(BaseModel):
    pago_fijo_id: int | None = None
    fecha_programada: date | None = None
    fecha_realizada: date | None = None
    estatus_id: int | None = None

class PagoCreate(PagoBase):
    pass

class PagoOut(PagoBase):
    id: int

    class Config:
        from_attributes = True
