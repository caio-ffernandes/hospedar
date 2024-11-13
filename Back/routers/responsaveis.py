from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from models.responsaveis import ResponsaveisDB
from models.tipo_responsavel import Tipo_RespDB
from models.posts import PostsDB
from schemas.responsaveis import ResponsaveisCreate, ResponsaveisRead, ResponsaveisReadMany, ResponsaveisUpdate
import shutil
import os

router = APIRouter(prefix='/responsaveis', tags=['RESPONSAVEIS'])

# Define o caminho para salvar as imagens
UPLOAD_DIR = "static/uploads/responsaveis/"

# Função para salvar imagens
def save_image(foto: UploadFile):
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)
    foto_path = os.path.join(UPLOAD_DIR, foto.filename)
    with open(foto_path, "wb") as buffer:
        shutil.copyfileobj(foto.file, buffer)
    return foto_path

@router.post('', response_model=ResponsaveisRead)
async def criar_responsavel(
    nome: str = Form(...),
    tipos_resps_id_tipos_resps: int = Form(...),
    posts_id_post: int = Form(...),
    foto: UploadFile = File(...),
    data_in: str = Form(None),
    data_out: str = Form(None),
    biografia: str = Form(None)
):
    # Validação de tipos_resps e post
    tipos_resps = Tipo_RespDB.get_or_none(Tipo_RespDB.id_tipos_resps == tipos_resps_id_tipos_resps)
    if not tipos_resps:
        raise HTTPException(status_code=404, detail="Tipo de responsável não encontrado")

    post = PostsDB.get_or_none(PostsDB.id_post == posts_id_post)
    if not post:
        raise HTTPException(status_code=404, detail="Post não encontrado")

    # Salvar a imagem
    foto_path = save_image(foto)

    # Criar novo responsável
    responsavel = ResponsaveisDB.create(
        nome=nome,
        data_in=data_in,
        data_out=data_out,
        biografia=biografia,
        foto=foto_path,
        tipos_resps_id_tipos_resps=tipos_resps_id_tipos_resps,
        posts_id_post=posts_id_post
    )
    return ResponsaveisRead(**responsavel.__data__)

@router.get('', response_model=ResponsaveisReadMany)
def listar_responsaveis():
    responsaveis = ResponsaveisDB.select()
    responsaveis_list = [ResponsaveisRead(**responsavel.__data__) for responsavel in responsaveis]
    return {'responsaveis': responsaveis_list}

@router.get('/{responsavel_id}', response_model=ResponsaveisRead)
def listar_responsavel(responsavel_id: int):
    responsavel = ResponsaveisDB.get_or_none(ResponsaveisDB.id_resposaveis == responsavel_id)
    if not responsavel:
        raise HTTPException(status_code=404, detail="Responsável não encontrado")
    return ResponsaveisRead(**responsavel.__data__)

@router.patch('/{responsavel_id}', response_model=ResponsaveisRead)
async def atualizar_responsavel(
    responsavel_id: int,
    nome: str = Form(None),
    tipos_resps_id_tipos_resps: int = Form(None),
    posts_id_post: int = Form(None),
    foto: UploadFile = File(None),
    data_in: str = Form(None),
    data_out: str = Form(None),
    biografia: str = Form(None)
):
    responsavel = ResponsaveisDB.get_or_none(ResponsaveisDB.id_resposaveis == responsavel_id)
    if not responsavel:
        raise HTTPException(status_code=404, detail="Responsável não encontrado")

    # Atualiza a imagem, se fornecida
    if foto:
        foto_path = save_image(foto)
        responsavel.foto = foto_path

    # Atualiza outros campos
    if nome:
        responsavel.nome = nome
    if tipos_resps_id_tipos_resps:
        responsavel.tipos_resps_id_tipos_resps = tipos_resps_id_tipos_resps
    if posts_id_post:
        responsavel.posts_id_post = posts_id_post
    if data_in:
        responsavel.data_in = data_in
    if data_out:
        responsavel.data_out = data_out
    if biografia:
        responsavel.biografia = biografia

    responsavel.save()
    return ResponsaveisRead(**responsavel.__data__)

@router.delete('/{responsavel_id}', response_model=dict)
def excluir_responsavel(responsavel_id: int):
    responsavel = ResponsaveisDB.get_or_none(ResponsaveisDB.id_resposaveis == responsavel_id)
    if not responsavel:
        raise HTTPException(status_code=404, detail="Responsável não encontrado")

    responsavel.delete_instance()
    return {'message': 'Responsável excluído com sucesso'}
