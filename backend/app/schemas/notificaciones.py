from pydantic import BaseModel
from datetime import datetime

class NotificacionBase(BaseModel):
    usuario_id: int
    tipo_notificacion_id: int
    mensaje: str | None = None
    pago_id: int | None = None
    presupuesto_id: int | None = None

class NotificacionCreate(NotificacionBase):
    pass

class NotificacionOut(NotificacionBase):
    id: int
    fecha_creacion: datetime

    class Config:
        from_attributes = True
