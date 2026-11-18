from pydantic import BaseModel, Field
from itertools import count
from datetime import datetime

from src.schemas.ItemCardapioSchema import ItemCardapioInputSchema, ItemCardapioResponseSchema

class CardapioInputSchema(BaseModel):
    #id: int = Field(default_factory=count(1).__next__)
    data: datetime = Field(default_factory=datetime.now)
    listaItens: list[ItemCardapioInputSchema]

class CardapioResponseSchema(BaseModel):
    id: int
    data: datetime
    listaItens: list[ItemCardapioResponseSchema]