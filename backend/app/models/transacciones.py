from sqlalchemy import Column, Integer, String, DECIMAL, Date, ForeignKey
from app.database import Base

class Transaccion(Base):
    __tablename__ = "transacciones"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    monto = Column(DECIMAL(10, 2), nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=False)
    fecha = Column(Date, nullable=False)
    concepto = Column(String(150), nullable=True)
    estatus_id = Column(Integer, ForeignKey("estatus.id"), nullable=False)
    tipo_transaccion_id = Column(Integer, ForeignKey("tipos_transacciones.id"), nullable=False)
