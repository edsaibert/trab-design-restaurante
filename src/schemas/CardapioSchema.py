from pydantic import BaseModel, Field, model_validator
from typing import Any
from itertools import count
from datetime import datetime

from src.schemas.ItemCardapioSchema import ItemCardapioInputSchema, ItemCardapioResponseSchema

class CardapioInputSchema(BaseModel):
    listaItens: list[ItemCardapioInputSchema]

class CardapioResponseSchema(BaseModel):
    id: int
    data: datetime
    listaItens: list[ItemCardapioResponseSchema]

    @model_validator(mode='before')
    @classmethod
    def mapeiaCardapio(cls, dado: Any) -> Any:
        if not isinstance(dado, dict):
            return {
                "id": dado.id,
                "data": dado.data,
                "listaItens": dado.itens
            }
        return dado