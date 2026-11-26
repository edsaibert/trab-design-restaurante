from pydantic import BaseModel, Field

class ItemCardapioInputSchema(BaseModel):
    nome: str 
    porcoes: int = Field(default=1)
    tamanhoPorcao: int = Field(default=1)
    vegano: bool = Field(default=False)
    disponibilidade: bool

class ItemCardapioUpdateSchema(BaseModel):
    id: int
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
