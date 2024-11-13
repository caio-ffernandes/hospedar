from fastapi import APIRouter, HTTPException, Depends
from models.usuarios import UsuariosDB
from schemas.usuarios import UsuariosCreate, UsuariosRead, UsuariosReadMany, UsuariosUpdate
from auth.jwt_handler import verificar_token

router = APIRouter(prefix='/usuarios', tags=['USUARIOS'])

# Rota protegida para administradores
@router.get('/admin', response_model=UsuariosRead)
def rota_protegida(token: dict = Depends(verificar_token)):
    if token['tipo'] != 'admin':
        raise HTTPException(status_code=403, detail="Acesso negado")
    return {"message": "Bem-vindo ao painel administrativo"}

# Criar novo usuário
@router.post('', response_model=UsuariosRead)
def criar_usuario(novo_usuario: UsuariosCreate):
    usuario = UsuariosDB.create(**novo_usuario.dict())
    return UsuariosRead.from_orm(usuario)

# Listar todos os usuários
@router.get('', response_model=UsuariosReadMany)
def listar_usuarios():
    usuarios = UsuariosDB.select()
    usuarios_list = [UsuariosRead.from_orm(usuario) for usuario in usuarios]
    return {'usuarios': usuarios_list}

# Listar um usuário por ID
@router.get('/{usuario_id}', response_model=UsuariosRead)
def listar_usuario(usuario_id: int):
    usuario = UsuariosDB.get_or_none(UsuariosDB.id == usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return UsuariosRead.from_orm(usuario)

# Atualizar um usuário
@router.patch('/{usuario_id}', response_model=UsuariosRead)
def atualizar_usuario(usuario_id: int, usuario_atualizado: UsuariosUpdate):
    usuario = UsuariosDB.get_or_none(UsuariosDB.id == usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    usuario_data = usuario_atualizado.dict(exclude_unset=True)
    for key, value in usuario_data.items():
        setattr(usuario, key, value)

    usuario.save()
    return UsuariosRead.from_orm(usuario)

# Excluir um usuário
@router.delete('/{usuario_id}', response_model=dict)
def excluir_usuario(usuario_id: int):
    usuario = UsuariosDB.get_or_none(UsuariosDB.id == usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    usuario.delete_instance()
    return {'message': 'Usuário excluído com sucesso'}
