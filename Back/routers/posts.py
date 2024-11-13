from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from models.posts import PostsDB, SubcategoriasDB
from typing import Optional
from schemas.posts import (
    PostsCreate,
    PostsRead,
    PostsReadMany,
    PostsUpdate
)
import aiofiles
import os
import uuid

router = APIRouter(prefix='/posts', tags=['POSTS'])

# Diretório onde as imagens serão salvas
UPLOAD_DIR = "static/uploads/posts/"
os.makedirs(UPLOAD_DIR, exist_ok=True)  # Cria o diretório se não existir


# Endpoint para criar um novo post com upload de imagem
@router.post('', response_model=PostsRead)
async def criar_post(
        nome_post: str = Form(...),
        descricao_post: str = Form(...),
        subcategorias_id_subcategoria: int = Form(...),
        imagem: UploadFile = File(None)
):
    # Verifica se a subcategoria existe
    subcategoria = SubcategoriasDB.get_or_none(
        SubcategoriasDB.id_subcategoria == subcategorias_id_subcategoria
    )
    if not subcategoria:
        raise HTTPException(status_code=404, detail="Subcategoria não encontrada")

    # Tratamento do arquivo de imagem
    if imagem:
        filename = f"{uuid.uuid4()}{os.path.splitext(imagem.filename)[1]}"
        file_path = os.path.join(UPLOAD_DIR, filename)

        # Salva o arquivo de imagem de forma assíncrona
        async with aiofiles.open(file_path, 'wb') as out_file:
            content = await imagem.read()
            await out_file.write(content)

        # Caminho da imagem no banco de dados
        imagem_post = file_path
    else:
        imagem_post = None

    # Cria o post no banco de dados
    post = PostsDB.create(
        nome_post=nome_post,
        descricao_post=descricao_post,
        subcategorias_id_subcategoria=subcategorias_id_subcategoria,
        imagem_post=imagem_post
    )
    return post


# Endpoint para listar todos os posts
@router.get('', response_model=PostsReadMany)
def listar_posts():
    posts = PostsDB.select()
    return {'posts': [post for post in posts]}  # Ajuste para garantir que seja serializado corretamente


# Endpoint para listar um post específico
@router.get('/{post_id}', response_model=PostsRead)
def listar_post(post_id: int):
    post = PostsDB.get_or_none(PostsDB.id_post == post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post não encontrado")
    return post


# Endpoint para atualizar um post
@router.patch('/{post_id}', response_model=PostsRead)
async def atualizar_post(
        post_id: int,
        nome_post: Optional[str] = Form(None),
        descricao_post: Optional[str] = Form(None),
        subcategorias_id_subcategoria: Optional[int] = Form(None),
        imagem: UploadFile = File(None)  # Imagem opcional
):
    post = PostsDB.get_or_none(PostsDB.id_post == post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post não encontrado")

    # Atualiza os campos fornecidos
    if nome_post:
        post.nome_post = nome_post
    if descricao_post:
        post.descricao_post = descricao_post
    if subcategorias_id_subcategoria:
        post.subcategorias_id_subcategoria = subcategorias_id_subcategoria

    # Se uma nova imagem for enviada, faz o upload e atualiza o caminho
    if imagem:
        filename = f"{uuid.uuid4()}{os.path.splitext(imagem.filename)[1]}"
        file_path = os.path.join(UPLOAD_DIR, filename)

        async with aiofiles.open(file_path, 'wb') as out_file:
            content = await imagem.read()
            await out_file.write(content)

        post.imagem_post = file_path

    post.save()
    return post


# Endpoint para excluir um post
@router.delete('/{post_id}', response_model=dict)
def excluir_post(post_id: int):
    post = PostsDB.get_or_none(PostsDB.id_post == post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post não encontrado")

    post.delete_instance()
    return {'message': 'Post excluído com sucesso'}
