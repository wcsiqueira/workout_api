from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status, Query
from pydantic import UUID4
from sqlalchemy.exc import IntegrityError
from workout_api.centro_treinamento.schemas import CentroTreinamentoOut, CentroTreinamentoIn, CentroTreinamentoOutCustom, AtletaCentroTreinamentoOut
from workout_api.centro_treinamento.models import CentroTreinamentoModel
from workout_api.atleta.models import AtletaModel
from workout_api.contrib.dependencies import DatabaseDependency
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from sqlalchemy import or_
from fastapi_pagination import Page, paginate, add_pagination

router = APIRouter()
# Aqui trato as excessões de erro de integridade, como o cpf duplicado, e retorno o status 303_SEE_OTHER
@router.post(
    '/', 
    summary='Criar um novo Centro de treinamento',
    status_code=status.HTTP_201_CREATED,
    response_model=CentroTreinamentoOut,
)
async def post(
    db_session: DatabaseDependency, 
    centro_treinamento_in: CentroTreinamentoIn = Body(...)
) -> CentroTreinamentoOut:
    centro_treinamento_out = CentroTreinamentoOut(id=uuid4(), **centro_treinamento_in.model_dump())
    centro_treinamento_model = CentroTreinamentoModel(**centro_treinamento_out.model_dump())
    
    db_session.add(centro_treinamento_model)
    
    try:
        await db_session.commit()
    except IntegrityError as e:
        await db_session.rollback()
        if "atletas.cpf" in str(e.orig):
            raise HTTPException(
                status_code=status.HTTP_303_SEE_OTHER,
                detail=f'Já existe um atleta cadastrado com o cpf: {centro_treinamento_in.cpf}'
            )
        raise

    return centro_treinamento_out

@router.get(
    '/', 
    summary='Consultar todos os centros de treinamento',
    status_code=status.HTTP_200_OK,
    response_model=Page[CentroTreinamentoOutCustom],
)
async def query(
    db_session: DatabaseDependency,
    nome: str = Query(None, description="Nome do atleta"),
    cpf: str = Query(None, description="CPF do atleta"),
    limit: int = Query(10, description="Limite de itens por página"),
    offset: int = Query(0, description="Deslocamento para paginação")
) -> Page[CentroTreinamentoOutCustom]:
    query = select(CentroTreinamentoModel).options(joinedload(CentroTreinamentoModel.atleta))
    
    if nome or cpf:
        query = query.filter(
            or_(
                AtletaModel.nome == nome if nome else True,
                AtletaModel.cpf == cpf if cpf else True
            )
        )

    centros_treinamento = (await db_session.execute(query)).scalars().all()

    response = []
    for centro in centros_treinamento:
        atletas = []
        for atleta in centro.atleta:
            atletas.append(AtletaCentroTreinamentoOut(
                nome=atleta.nome,
                centro_treinamento=centro.nome,
                categoria=atleta.categoria  # Certifique-se de que `categoria` existe em AtletaModel
            ))

        response.append(CentroTreinamentoOutCustom(
            id=centro.pk_id,
            nome=centro.nome,
            endereco=centro.endereco,
            proprietario=centro.proprietario,
            atletas=atletas
        ))
    
    return paginate(response)

@router.get(
    '/{id}', 
    summary='Consulta um centro de treinamento pelo id',
    status_code=status.HTTP_200_OK,
    response_model=CentroTreinamentoOut,
)
async def get(id: UUID4, db_session: DatabaseDependency) -> CentroTreinamentoOut:
    centro_treinamento_out: CentroTreinamentoOut = (
        await db_session.execute(select(CentroTreinamentoModel).filter_by(id=id))
    ).scalars().first()

    if not centro_treinamento_out:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f'Centro de treinamento não encontrado no id: {id}'
        )
    
    return centro_treinamento_out

add_pagination(router)
