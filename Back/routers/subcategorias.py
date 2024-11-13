from fastapi import APIRouter, HTTPException
from models.subcategorias import SubcategoriasDB, CulturaDB
from schemas.subcategorias import (
    SubcategoriasCreate,
    SubcategoriasRead,
    SubcategoriasReadMany,
    SubcategoriasUpdate
)

router = APIRouter(prefix='/subcategorias', tags=['SUBCATEGORIAS'])


@router.post('', response_model=SubcategoriasRead)
def criar_subcategoria(nova_subcategoria: SubcategoriasCreate):
    cultura = CulturaDB.get_or_none(CulturaDB.id_cultura == nova_subcategoria.culturas_id_cultura)
    if not cultura:
        raise HTTPException(status_code=404, detail="Cultura não encontrada")

    subcategoria = SubcategoriasDB.create(**nova_subcategoria.dict())
    return subcategoria


@router.get('', response_model=SubcategoriasReadMany)
def listar_subcategorias():
    subcategorias = SubcategoriasDB.select()
    return {'subcategorias': subcategorias}


@router.get('/{subcategoria_id}', response_model=SubcategoriasRead)
def listar_subcategoria(subcategoria_id: int):
    subcategoria = SubcategoriasDB.get_or_none(SubcategoriasDB.id_subcategoria == subcategoria_id)
    if not subcategoria:
        raise HTTPException(status_code=404, detail="Subcategoria não encontrada")
    return subcategoria


@router.patch('/{subcategoria_id}', response_model=SubcategoriasRead)
def atualizar_subcategoria(subcategoria_id: int, subcategoria_atualizada: SubcategoriasUpdate):
    subcategoria = SubcategoriasDB.get_or_none(SubcategoriasDB.id_subcategoria == subcategoria_id)
    if not subcategoria:
        raise HTTPException(status_code=404, detail="Subcategoria não encontrada")

    if subcategoria_atualizada.culturas_id_cultura:
        cultura = CulturaDB.get_or_none(CulturaDB.id_cultura == subcategoria_atualizada.culturas_id_cultura)
        if not cultura:
            raise HTTPException(status_code=404, detail="Cultura não encontrada")

    subcategoria.nome_subcategoria = subcategoria_atualizada.nome_subcategoria or subcategoria.nome_subcategoria
    subcategoria.culturas_id_cultura = subcategoria_atualizada.culturas_id_cultura or subcategoria.culturas_id_cultura
    subcategoria.save()
    return subcategoria


@router.delete('/{subcategoria_id}', response_model=dict)
def excluir_subcategoria(subcategoria_id: int):
    subcategoria = SubcategoriasDB.get_or_none(SubcategoriasDB.id_subcategoria == subcategoria_id)
    if not subcategoria:
        raise HTTPException(status_code=404, detail="Subcategoria não encontrada")

    subcategoria.delete_instance()
    return {'message': 'Subcategoria excluída com sucesso'}
