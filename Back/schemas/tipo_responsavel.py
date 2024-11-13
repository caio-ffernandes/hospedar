from pydantic import BaseModel

class ResponsavelCreate(BaseModel):
    nome: str

class ResponsavelRead(BaseModel):
    id_tipos_resps: int
    nome: str

class ResponsavelUpdate(BaseModel):
    nome_resp: str

class ResponsavelReadMany(BaseModel):
    responsaveis: list[ResponsavelRead]
