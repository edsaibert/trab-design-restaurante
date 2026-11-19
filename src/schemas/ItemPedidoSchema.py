from pydantic import BaseModel, Field
from itertools import count

class ItemPedidoInputSchema(BaseModel):
    # id: int = Field(default_factory=count(1).__next__)
    idItemCardapio: int
    porcoes: int = Field(default=1)

