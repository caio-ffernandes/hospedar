from pydantic import BaseModel
from typing import Optional

class SubcategoriasRead(BaseModel):
    id_subcategoria: int
    nome_subcategoria: str
    culturas_id_cultura: Optional[int]  # Ajuste conforme seu modelo

    class Config:
        orm_mode = True  # Habilita a compatibilidade com ORM

class SubcategoriasReadMany(BaseModel):
    subcategorias: list[SubcategoriasRead]

class SubcategoriasCreate(BaseModel):
    nome_subcategoria: str
    culturas_id_cultura: Optional[int]

class SubcategoriasUpdate(BaseModel):
    nome_subcategoria: Optional[str]
    culturas_id_cultura: Optional[int]
