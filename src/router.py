from fastapi import APIRouter, Depends, Header, HTTPException
from services.PedidoService import PedidoService
from services.CardapioService import CardapioService
from services.LoginService import LoginService

router = APIRouter()

cardapio_service = CardapioService
pedido_service = PedidoService
login_service = LoginService

@router.get("/login")
def login():
    return login_service.login()

@router.get("/cardapio")
def consultar_cardapio():
    return cardapio_service.consultar_cardapio()

@router.post("/pedido")
def criar_pedido():
    return cardapio_service.criar_pedido()