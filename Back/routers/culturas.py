from fastapi import APIRouter, HTTPException
from models.culturas import CulturaDB
from schemas.culturas import (
    CulturaCreate,
    CulturaRead,
    CulturaReadMany,
    CulturaUpdate
)

router = APIRouter(prefix='/culturas', tags=['CULTURAS'])

@router.post('', response_model=CulturaRead)
def criar_cultura(nova_cultura: CulturaCreate):
    cultura = CulturaDB.create(**nova_cultura.dict())
    return cultura

@router.get('', response_model=CulturaReadMany)
def listar_culturas():
    culturas = CulturaDB.select()
    return {'culturas': culturas}

@router.get('/{cultura_id}', response_model=CulturaRead)
def listar_cultura(cultura_id: int):
    cultura = CulturaDB.get_or_none(CulturaDB.id_cultura == cultura_id)
    if not cultura:
        raise HTTPException(status_code=404, detail="Cultura não encontrada")
    return cultura

@router.patch('/{cultura_id}', response_model=CulturaRead)
def atualizar_cultura(cultura_id: int, cultura_atualizada: CulturaUpdate):
    cultura = CulturaDB.get_or_none(CulturaDB.id_cultura == cultura_id)
    if not cultura:
        raise HTTPException(status_code=404, detail="Cultura não encontrada")

    cultura.nome_cultura = cultura_atualizada.nome_cultura or cultura.nome_cultura
    cultura.save()
    return cultura

@router.delete('/{cultura_id}', response_model=dict)
def excluir_cultura(cultura_id: int):
    cultura = CulturaDB.get_or_none(CulturaDB.id_cultura == cultura_id)
    if not cultura:
        raise HTTPException(status_code=404, detail="Cultura não encontrada")

    cultura.delete_instance()
    return {'message': 'Cultura excluída com sucesso'}
