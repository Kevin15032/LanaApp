from pydantic import BaseModel

class PreferenciaNotificacionBase(BaseModel):
    usuario_id: int
    via_sms: bool = False
    via_email: bool = False

class PreferenciaNotificacionCreate(PreferenciaNotificacionBase):
    pass

class PreferenciaNotificacionOut(PreferenciaNotificacionBase):
    id: int

    class Config:
        from_attributes = True
