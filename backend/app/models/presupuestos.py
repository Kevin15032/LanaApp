from sqlalchemy import Column, Integer, Float, ForeignKey, String
from app.database import Base

class Presupuesto(Base):
    __tablename__ = "presupuestos"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=False)
    monto = Column(Float, nullable=False)
    periodo = Column(String(50), nullable=False)
