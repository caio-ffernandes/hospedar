from pydantic import BaseModel

class CulturaCreate(BaseModel):
    nome_cultura: str

class CulturaRead(BaseModel):
    id_cultura: int
    nome_cultura: str

class CulturaUpdate(BaseModel):
    nome_cultura: str

class CulturaReadMany(BaseModel):
    culturas: list[CulturaRead]
