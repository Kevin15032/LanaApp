from sqlalchemy import Column, Integer, Boolean, ForeignKey
from app.database import Base

class PreferenciaNotificacion(Base):
    __tablename__ = "preferencias_notificaciones"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    via_sms = Column(Boolean, default=False)
    via_email = Column(Boolean, default=False)
