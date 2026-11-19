from pydantic import BaseModel, Field
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