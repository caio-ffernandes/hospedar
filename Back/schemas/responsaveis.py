from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class ResponsaveisCreate(BaseModel):
    nome: Optional[str]
    data_in: Optional[date]
    data_out: Optional[datetime]
    biografia: Optional[str]
    foto: Optional[str]  # Caminho para a foto
    tipos_resps_id_tipos_resps: int
    posts_id_post: int

class ResponsaveisRead(BaseModel):
    id_resposaveis: int
    nome: Optional[str]
    data_in: Optional[date]
    data_out: Optional[datetime]
    biografia: Optional[str]
    foto: Optional[str]  # Caminho para a foto
    tipos_resps_id_tipos_resps: int
    posts_id_post: int

    class Config:
        orm_mode = True

class ResponsaveisUpdate(BaseModel):
    nome: Optional[str]
    data_in: Optional[date]
    data_out: Optional[datetime]
    biografia: Optional[str]
    foto: Optional[str]  # Caminho para a foto
    tipos_resps_id_tipos_resps: Optional[int]
    posts_id_post: Optional[int]

class ResponsaveisReadMany(BaseModel):
    responsaveis: list[ResponsaveisRead]
