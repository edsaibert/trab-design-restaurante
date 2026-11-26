from pydantic import BaseModel

from fastapi import APIRouter, Depends, Header, HTTPException
from fastapi.responses import JSONResponse

from src.schemas.PedidoSchema import PedidoInputSchema, PedidoResponseSchema
from src.schemas.CardapioSchema import CardapioInputSchema, CardapioResponseSchema
from src.schemas.ItemCardapioSchema import ItemCardapioUpdateSchema

from src.models.Pedido import Pedido
from src.models.ItemPedido import ItemPedido
from src.models.ItemCardapio import ItemCardapio

from src.database.SQLAlchemyCardapioRepository import SQLAlchemyCardapioRepository
from src.database.SQLAlchemyPedidoRepository import SQLAlchemyPedidoRepository

from src.services.PedidoService import PedidoService
from src.services.CardapioService import CardapioService
from src.services.LoginService import LoginService

from sqlalchemy.orm import Session

from src.database.database import get_db
from src.database.SQLAlchemyCardapioRepository import SQLAlchemyCardapioRepository
from src.database.SQLAlchemyPedidoRepository import SQLAlchemyPedidoRepository


router = APIRouter()

class LoginRequest(BaseModel):
    usuario: str
    senha: str

def get_login_service(db: Session = Depends(get_db)):
    return LoginService()

def get_cardapio_service(db: Session = Depends(get_db)):
    repository = SQLAlchemyCardapioRepository(db)
    return CardapioService(repository)


def get_pedido_service(db: Session = Depends(get_db)):
    cardapio_repository = SQLAlchemyCardapioRepository(db)
    pedido_repository = SQLAlchemyPedidoRepository(db)

    cardapio_service = CardapioService(cardapio_repository)

    return PedidoService(pedido_repository, cardapio_service)


@router.post("/login", response_model=None)
def login(credenciais: LoginRequest, login_service: LoginService = Depends(get_login_service)):
    
    return login_service.autenticar(credenciais.usuario, credenciais.senha)

@router.post("/cardapio", response_model=CardapioResponseSchema)
def criar_cardapio(cardapioInput: CardapioInputSchema, cardapio_service: CardapioService = Depends(get_cardapio_service)):
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
def atualizar_cardapio(atualizacoes: list[ItemCardapioUpdateSchema], cardapio_service: CardapioService = Depends(get_cardapio_service)):
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
def consultar_cardapio(cardapio_service: CardapioService = Depends(get_cardapio_service)):
    cardapio = cardapio_service.consultarCardapio()

    return cardapio


@router.post("/pedido", response_model=PedidoResponseSchema)
def criar_pedido(pedido_input: PedidoInputSchema, pedido_service: PedidoService = Depends(get_pedido_service)):
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

@router.post("/pedido/{pedido_id}/cancelar", response_model=PedidoResponseSchema)
def cancelar_pedido(pedido_id: int, pedido_service: PedidoService = Depends(get_pedido_service)):
    pedido_service.cancelarPedido(pedido_id)
    return pedido_service.consultarPedido(pedido_id)

@router.get("/pedido", response_model=PedidoResponseSchema)
def consultar_pedido(pedido_id: int, pedido_service: PedidoService = Depends(get_pedido_service)):
    pedido = pedido_service.consultarPedido(pedido_id)

    return pedido
