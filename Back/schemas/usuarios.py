from pydantic import BaseModel, EmailStr
from typing import Optional

class UsuariosCreate(BaseModel):
    nome: str
    email: EmailStr
    senha: str
    telefone: Optional[str] = None
    tipo: Optional[str] = 'comum'  # Novo campo com valor padrão

class UsuariosRead(BaseModel):
    id: int
    nome: str
    email: EmailStr
    senha: str
    telefone: Optional[str] = None
    tipo: str  # Novo campo

    class Config:
        from_attributes = True  # Atualizado para a nova configuração

class UsuariosUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[EmailStr] = None
    senha: Optional[str] = None
    telefone: Optional[str] = None
    tipo: Optional[str] = None  # Novo campo

class UsuariosReadMany(BaseModel):
    usuarios: list[UsuariosRead]
