from pydantic import BaseModel

class EstatusEnvioBase(BaseModel):
    nombre: str

class EstatusEnvioCreate(EstatusEnvioBase):
    pass

class EstatusEnvioOut(EstatusEnvioBase):
    id: int

    class Config:
        from_attributes = True

