from pydantic import BaseModel

class PagoFijoBase(BaseModel):
    usuario_id: int
    tipo_pago_id: int
    monto: float
    descripcion: str | None = None

class PagoFijoCreate(PagoFijoBase):
    pass

class PagoFijoOut(PagoFijoBase):
    id: int

    class Config:
        orm_mode = True
