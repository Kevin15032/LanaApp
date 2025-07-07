from pydantic import BaseModel

class NotificacionMedioBase(BaseModel):
    notificacion_id: int
    medio: str
    estado_envio: str | None = None

class NotificacionMedioCreate(NotificacionMedioBase):
    pass

class NotificacionMedioOut(NotificacionMedioBase):
    id: int

    class Config:
        from_attributes = True
