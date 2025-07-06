from sqlalchemy import Column, Integer, String
from app.database import Base

class Persona(Base):
    __tablename__ = "personas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), nullable=False)
    ap_paterno = Column(String(150), nullable=True)
    ap_materno = Column(String(150), nullable=True)
    telefono = Column(String(10), nullable=True)
