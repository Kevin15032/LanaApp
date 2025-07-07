from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class NotificacionMedio(Base):
    __tablename__ = "notificaciones_medios"

    id = Column(Integer, primary_key=True, index=True)
    notificacion_id = Column(Integer, ForeignKey("notificaciones.id"), nullable=False)
    medio = Column(String(50), nullable=False)
    estado_envio = Column(String(50), nullable=True)
