from sqlalchemy import Column, Integer, String
from app.database import Base

class TipoTransaccion(Base):
    __tablename__ = "tipos_transacciones"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), nullable=False)
