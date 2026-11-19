from fastapi import APIRouter, Depends, Header, HTTPException

from src.schemas.PedidoSchema import PedidoInputSchema, PedidoResponseSchema
from src.schemas.CardapioSchema import CardapioInputSchema, CardapioResponseSchema
from src.schemas.ItemCardapioSchema import ItemCardapioInputSchema

from src.models.Pedido import Pedido
from src.models.ItemPedido import ItemPedido
from src.models.ItemCardapio import ItemCardapio

from src.database.database import get_db
from src.database.SQLAlchemyCardapioRepository import SQLAlchemyCardapioRepository
from src.database.SQLAlchemyPedidoRepository import SQLAlchemyPedidoRepository

from src.services.PedidoService import PedidoService
from src.services.CardapioService import CardapioService
from src.services.LoginService import LoginService

router = APIRouter()

cardapio_repository = SQLAlchemyCardapioRepository(get_db())
cardapio_service = CardapioService(cardapio_repository)

pedido_service = PedidoService(SQLAlchemyPedidoRepository(), cardapio_service)          
login_service = LoginService

@router.get("/login")
def login():
    return login_service.login()

@router.post("/cardapio", response_model=CardapioResponseSchema)
def criar_cardapio(cardapioInput: CardapioInputSchema):
    itens = [
        ItemCardapio(
            id=None,
            nome=item.nome,
            porcoes=item.porcoes,
            tamanhoPorcao=item.tamanhoPorcao,
            vegano=item.vegano,
            disponibilidade=item.disponibilidade
        )
        for item in cardapioInput.listaItens
    ]

    cardapio = cardapio_service.criarCardapio(itens)

    return cardapio

@router.put("/cardapio", response_model=CardapioResponseSchema, responses={404:{"description":"Cardápio não encontrado"}})
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

@router.get("/cardapio", response_model=CardapioResponseSchema, responses={404:{"description":"Cardápio não encontrado"}})
def consultar_cardapio():
    cardapio = cardapio_service.consultarCardapio()

    return cardapio


@router.post("/pedido", response_model=PedidoResponseSchema)
def criar_pedido(pedido_input: PedidoInputSchema):
    itens = [
        ItemPedido(
            id=None,
            idItemCardapio=item.idItemCardapio,
            porcoes=item.porcoes
        )
        for item in pedido_input.pedidoItens
    ]

    pedido = Pedido(itens)
    return pedido_service.realizarPedido(pedido) 