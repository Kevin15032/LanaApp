from pydantic import BaseModel

class TipoTransaccionBase(BaseModel):
    nombre: str

class TipoTransaccionCreate(TipoTransaccionBase):
    pass

class TipoTransaccionOut(TipoTransaccionBase):
    id: int

    class Config:
        orm_mode = True
