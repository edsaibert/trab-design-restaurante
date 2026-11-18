from pydantic import BaseModel, Field
from itertools import count

class ItemCardapioInputSchema(BaseModel):
    id: int = Field(default_factory=count(1).__next__)
    nome: str 
    porcoes: int = Field(default=1)
    tamanhoPorcao: int = Field(default=1)
    vegano: bool = Field(default=False)
    disponibilidade: bool


class ItemCardapioResponseSchema(BaseModel):
    id: int 
    nome: str 
    porcoes: int = Field(default=1)
    tamanhoPorcao: int = Field(default=1)
    vegano: bool = Field(default=False)
    disponibilidade: bool