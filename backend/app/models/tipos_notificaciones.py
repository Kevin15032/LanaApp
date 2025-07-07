from sqlalchemy import Column, Integer, String
from app.database import Base

class TipoNotificacion(Base):
    __tablename__ = "tipos_notificaciones"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), nullable=False)
