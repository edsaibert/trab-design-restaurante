from pydantic import BaseModel, Field
from itertools import count
from datetime import datetime

from src.schemas.ItemCardapio import ItemCardapioInputSchema, ItemCardapioResponseSchema

class CardapioInputSchema(BaseModel):
    #id: int = Field(default_factory=count(1).__next__) definido pelo repository
    #data: datetime                                     definido pelo repository
    listaItens: list[ItemCardapioInputSchema]

class CardapioResponseSchema(BaseModel):
    id: int
    data: datetime
    listaItens: list[ItemCardapioResponseSchema]