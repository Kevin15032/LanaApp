from sqlalchemy import Column, Integer, String
from app.database import Base

class TipoPago(Base):
    __tablename__ = "tipos_pagos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), nullable=False)
