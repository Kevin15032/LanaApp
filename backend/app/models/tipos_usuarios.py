from sqlalchemy import Column, Integer, String
from app.database import Base

class TipoUsuario(Base):
    __tablename__ = "tipos_usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), nullable=False)
