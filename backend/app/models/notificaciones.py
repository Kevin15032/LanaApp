from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.database import Base

class Notificacion(Base):
    __tablename__ = "notificaciones"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    tipo_notificacion_id = Column(Integer, ForeignKey("tipos_notificaciones.id"), nullable=False)
    mensaje = Column(String(150), nullable=True)
    fecha_creacion = Column(DateTime, server_default=func.now())
    pago_id = Column(Integer, ForeignKey("pagos.id"), nullable=True)
    presupuesto_id = Column(Integer, ForeignKey("presupuestos.id"), nullable=True)
