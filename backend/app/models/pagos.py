from sqlalchemy import Column, Integer, Date, ForeignKey
from app.database import Base

class Pago(Base):
    __tablename__ = "pagos"

    id = Column(Integer, primary_key=True, index=True)
    pago_fijo_id = Column(Integer, ForeignKey("pagos_fijos.id"))
    fecha_programada = Column(Date, nullable=True)
    fecha_realizada = Column(Date, nullable=True)
    estatus_id = Column(Integer, ForeignKey("estatus.id"))
