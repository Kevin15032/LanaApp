from pydantic import BaseModel

class PresupuestoBase(BaseModel):
    usuario_id: int
    categoria_id: int
    monto: float
    periodo: str

class PresupuestoCreate(PresupuestoBase):
    pass

class PresupuestoOut(PresupuestoBase):
    id: int

    class Config:
        orm_mode = True
