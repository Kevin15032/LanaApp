from fastapi import FastAPI
from app.database import Base, engine
from app.routes import (
    usuarios, personas, categorias, transacciones,
    presupuestos, tipos_transacciones, estatus,
    tipos_pagos, pagos_fijos, tipos_usuarios,
    estatus_envios, pagos, preferencias_notificaciones,
    notificaciones, notificaciones_medios,
    tipos_notificaciones
)

app = FastAPI()

# Crear tablas automáticamente (solo al inicio)
Base.metadata.create_all(bind=engine)

# Incluir routers
# Rutas implementadas (6-10)
app.include_router(tipos_transacciones.router, prefix="/tipos-transacciones")
app.include_router(estatus.router, prefix="/estatus")
app.include_router(presupuestos.router, prefix="/presupuestos")
app.include_router(tipos_pagos.router, prefix="/tipos-pagos")
app.include_router(pagos_fijos.router, prefix="/pagos-fijos")

# Rutas implementadas (1-5)
app.include_router(usuarios.router, prefix="/usuarios")
app.include_router(personas.router, prefix="/personas")
app.include_router(categorias.router, prefix="/categorias")
app.include_router(transacciones.router, prefix="/transacciones")
app.include_router(tipos_usuarios.router, prefix="/tipos_usuarios")
app.include_router(estatus_envios.router, prefix="/estatus_envios")

# Rutas implementadas (11 - 15)
app.include_router(pagos.router, prefix="/pagos")
app.include_router(preferencias_notificaciones.router, prefix="/preferencias_notificaciones")
app.include_router(notificaciones.router, prefix="/notificaciones")
app.include_router(notificaciones_medios.router, prefix="/notificaciones_medios")
app.include_router(tipos_notificaciones.router, prefix="/tipos_notificaciones")




@app.get("/")
def root():
    return {"mensaje": "Lana App API funcionando"}
