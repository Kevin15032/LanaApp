from sqlalchemy import Column, Integer, Float, ForeignKey, String
from app.database import Base

class PagoFijo(Base):
    __tablename__ = "pagos_fijos"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    tipo_pago_id = Column(Integer, ForeignKey("tipos_pagos.id"), nullable=False)
    monto = Column(Float, nullable=False)
    descripcion = Column(String(150))
