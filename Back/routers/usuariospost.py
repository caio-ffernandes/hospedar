from fastapi import APIRouter, HTTPException
from schemas.usuariospost import UsuariosHasPostsCreate, UsuariosHasPostsUpdate, UsuariosHasPostsOut
from crud.usuariospost import (create_usuarios_has_posts, get_all_usuarios_has_posts,
                       get_usuarios_has_posts_by_id, update_usuarios_has_posts, delete_usuarios_has_posts)

router = APIRouter(prefix='/usuarios', tags=['USUARIOS-POSTS'])

# Criar um novo relacionamento
@router.post("/usuarios_has_posts/", response_model=UsuariosHasPostsOut)
def create_usuarios_post(data: UsuariosHasPostsCreate):
    new_record = create_usuarios_has_posts(data)
    return new_record.to_dict()

# Listar todos os relacionamentos
@router.get("/usuarios_has_posts/")
def list_usuarios_posts():
    return get_all_usuarios_has_posts()

# Obter um relacionamento por ID
@router.get("/usuarios_has_posts/{record_id}", response_model=UsuariosHasPostsOut)
def get_usuarios_post(record_id: int):
    record = get_usuarios_has_posts_by_id(record_id)
    if record is None:
        raise HTTPException(status_code=404, detail="Record not found")
    return record

# Atualizar um relacionamento
@router.put("/usuarios_has_posts/{record_id}", response_model=UsuariosHasPostsOut)
def update_usuarios_post(record_id: int, data: UsuariosHasPostsUpdate):
    record = get_usuarios_has_posts_by_id(record_id)
    if record is None:
        raise HTTPException(status_code=404, detail="Record not found")
    updated_record = update_usuarios_has_posts(record_id, data)
    return updated_record

# Deletar um relacionamento
@router.delete("/usuarios_has_posts/{record_id}")
def delete_usuarios_post(record_id: int):
    record = get_usuarios_has_posts_by_id(record_id)
    if record is None:
        raise HTTPException(status_code=404, detail="Record not found")
    delete_usuarios_has_posts(record_id)
    return {"detail": "Record deleted"}
