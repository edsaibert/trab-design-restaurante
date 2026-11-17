from fastapi import APIRouter, Depends, Header, HTTPException

from src.database.database import get_db
from src.database.CardapioRepository import CardapioRepository

from src.services.PedidoService import PedidoService
from src.services.CardapioService import CardapioService
from src.services.LoginService import LoginService

router = APIRouter()

cardapio_service = CardapioService
pedido_service = PedidoService
login_service = LoginService

@router.get("/login")
def login():
    return login_service.login()

@router.get("/cardapio/{cardapioId}")
def consultar_cardapio(cardapioId):
    return cardapio_service.consultarCardapio()

@router.post("/pedido")
def criar_pedido():
    return cardapio_service.criar_pedido()