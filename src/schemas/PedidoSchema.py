from pydantic import BaseModel, Field, model_validator
from typing import Any
from itertools import count
from datetime import datetime
from src.schemas.ItemPedidoSchema import ItemPedidoInputSchema

class PedidoInputSchema(BaseModel):
    # id: int = Field(default_factory=count(1).__next__)
    pedidoItens: list[ItemPedidoInputSchema]
    

class PedidoResponseSchema(BaseModel):
    id: int
    itens: list[ItemPedidoInputSchema]
    data: datetime
    ativo: bool


    @model_validator(mode='before')
    @classmethod
    def mapeiaPedido(cls, dado: Any) -> Any:
        if not isinstance(dado, dict):
            return {
                "id": dado.id,
                "data": dado.data,
                "itens": dado.itens,
                "ativo": dado.ativo
            }
        return dado