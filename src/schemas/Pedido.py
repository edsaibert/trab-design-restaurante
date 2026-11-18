from pydantic import BaseModel, Field
from itertools import count
from src.schemas.ItemPedido import ItemPedidoInputSchema

class PedidoInputSchema(BaseModel):
    id: int = Field(default_factory=count(1).__next__)
    pedidoItens: list[ItemPedidoInputSchema]

class PedidoResponseSchema(BaseModel):
    response: str
