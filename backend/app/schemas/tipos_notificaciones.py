from pydantic import BaseModel

class TipoNotificacionBase(BaseModel):
    nombre: str

class TipoNotificacionCreate(TipoNotificacionBase):
    pass

class TipoNotificacionOut(TipoNotificacionBase):
    id: int

    class Config:
        from_attributes = True
