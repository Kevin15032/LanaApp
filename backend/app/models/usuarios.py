from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    persona_id = Column(Integer, ForeignKey("personas.id"))
    correo = Column(String(150), nullable=False)
    contrasena = Column(String(150), nullable=False)
    tipo_usuario_id = Column(Integer, ForeignKey("tipos_usuarios.id"))
