from pydantic import BaseModel
from typing import Optional

class UsuariosHasPostsCreate(BaseModel):
    usuarios_id: int
    posts_id_post: int

class UsuariosHasPostsUpdate(BaseModel):
    usuarios_id: Optional[int] = None
    posts_id_post: Optional[int] = None

class UsuariosHasPostsOut(UsuariosHasPostsCreate):
    id_usuarios_has_postscol: int
