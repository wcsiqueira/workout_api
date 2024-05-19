from typing import List, Optional
from pydantic import BaseModel, Field, UUID4
from typing_extensions import (
    Annotated,
)

#  Devo me Certificar  de que o pacote `typing_extensions` está instalado
from workout_api.contrib.schemas import BaseSchema


class CentroTreinamentoIn(BaseSchema):
    nome: Annotated[
        str,
        Field(
            description="Nome do centro de treinamento",
            example="CT King",
            max_length=20,
        ),
    ]
    endereco: Annotated[
        str,
        Field(
            description="Endereço do centro de treinamento",
            example="Rua X, Q02",
            max_length=60,
        ),
    ]
    proprietario: Annotated[
        str,
        Field(
            description="Proprietario do centro de treinamento",
            example="Marcos",
            max_length=30,
        ),
    ]


class CentroTreinamentoAtleta(BaseSchema):
    nome: Annotated[
        str,
        Field(
            description="Nome do centro de treinamento",
            example="CT King",
            max_length=20,
        ),
    ]


class CentroTreinamentoOut(CentroTreinamentoIn):
    id: Annotated[UUID4, Field(description="Identificador do centro de treinamento")]


class AtletaCentroTreinamentoOut(BaseModel):
    nome: str
    centro_treinamento: str
    categoria: Optional[
        str
    ]  # Adicione este campo ao modelo AtletaModel Apenas uma ideia caso não exista o campo categoria no modelo AtletaModel


# o que alterei aqui foi para adicionar o campo categoria que é um campo que não existe no modelo AtletaModel


class CentroTreinamentoOutCustom(BaseModel):
    id: UUID4
    nome: str
    endereco: str
    proprietario: str
    atletas: List[AtletaCentroTreinamentoOut]
