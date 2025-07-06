from sqlalchemy import Column, Integer, String
from app.database import Base

class Estatus(Base):
    __tablename__ = "estatus"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), nullable=False)
