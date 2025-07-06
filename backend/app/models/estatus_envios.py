from sqlalchemy import Column, Integer, String
from app.database import Base

class EstatusEnvio(Base):
    __tablename__ = "estatus_envios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), nullable=False)
