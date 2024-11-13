from fastapi import APIRouter, HTTPException
from models.tipo_responsavel import Tipo_RespDB
from schemas.tipo_responsavel import (
    ResponsavelCreate,
    ResponsavelRead,
    ResponsavelReadMany,
    ResponsavelUpdate
)

router = APIRouter(prefix='/tipos-responsaveis', tags=['TIPOS-RESPONSAVEIS'])

@router.post('', response_model=ResponsavelRead)
def criar_responsavel(novo_responsavel: ResponsavelCreate):
    responsavel = Tipo_RespDB.create(**novo_responsavel.dict())
    return responsavel

@router.get('', response_model=ResponsavelReadMany)
def listar_responsaveis():
    responsaveis = Tipo_RespDB.select()
    return {'responsaveis': list(responsaveis)}

@router.get('/{responsavel_id}', response_model=ResponsavelRead)
def listar_responsavel(responsavel_id: int):
    responsavel = Tipo_RespDB.get_or_none(Tipo_RespDB.id_tipos_resps == responsavel_id)
    if not responsavel:
        raise HTTPException(status_code=404, detail="Responsável não encontrado")
    return responsavel


@router.patch('/{responsavel_id}', response_model=ResponsavelRead)
def atualizar_responsavel(responsavel_id: int, responsavel_atualizado: ResponsavelUpdate):
    responsavel = Tipo_RespDB.get_or_none(Tipo_RespDB.id_tipos_resps == responsavel_id)
    if not responsavel:
        raise HTTPException(status_code=404, detail="Responsável não encontrado")

    if responsavel_atualizado.nome_resp:
        responsavel.nome = responsavel_atualizado.nome_resp

    responsavel.save()
    return responsavel


@router.delete('/{responsavel_id}', response_model=dict)
def excluir_responsavel(responsavel_id: int):
    responsavel = Tipo_RespDB.get_or_none(Tipo_RespDB.id_tipos_resps == responsavel_id)
    if not responsavel:
        raise HTTPException(status_code=404, detail="Responsável não encontrado")

    responsavel.delete_instance()
    return {"detail": "Responsável excluído com sucesso"}

