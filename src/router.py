from fastapi import APIRouter, Depends, Header, HTTPException

from src.schemas.Pedido import PedidoInputSchema, PedidoResponseSchema
from src.schemas.Cardapio import CardapioInputSchema, CardapioResponseSchema
from src.schemas.ItemCardapio import ItemCardapioInputSchema

from src.models.ItemCardapio import ItemCardapio

from src.database.database import get_db
from src.database.CardapioRepository import CardapioRepository

from src.services.PedidoService import PedidoService
from src.services.CardapioService import CardapioService
from src.services.LoginService import LoginService

router = APIRouter()

cardapio_repository = CardapioRepository(get_db())
cardapio_service = CardapioService(cardapio_repository)

pedido_service = PedidoService          # precisa refletir nova implementação
login_service = LoginService

@router.get("/login")
def login():
    return login_service.login()

@router.post("/cardapio", response_model=CardapioResponseSchema)
def criar_cardapio(cardapioInput: CardapioInputSchema):
    itens = [
        ItemCardapio(
            id=item.id,
            nome=item.nome,
            porcoes=item.porcoes,
            tamanhoPorcao=item.tamanhoPorcao,
            vegano=item.vegano,
            disponibilidade=item.disponibilidade
        )
        for item in cardapioInput.listaItens
    ]

    cardapio = cardapio_service.criarCardapio(
        cardapioInput.data,
        itens
    )

    return cardapio

@router.put("/cardapio", response_model=CardapioResponseSchema)
def atualizar_cardapio(atualizacoes: list[ItemCardapioInputSchema]):
    itens = [
        ItemCardapio(
            id=item.id,
            nome=item.nome,
            porcoes=item.porcoes,
            tamanhoPorcao=item.tamanhoPorcao,
            vegano=item.vegano,
            disponibilidade=item.disponibilidade
        )
        for item in atualizacoes
    ]

    cardapio = cardapio_service.atualizarCardapio(itens)

    return cardapio

@router.post("/pedido")
def criar_pedido(Pedido: PedidoInputSchema) -> PedidoResponseSchema:
    return pedido_service.realizar_pedido()