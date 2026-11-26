from src.interfaces.IPedidoService import IPedidoService
from src.interfaces.ICardapioService import ICardapioService
from src.database.interfaces.PedidoRepository import PedidoRepository

from fastapi import HTTPException
from datetime import datetime
from src.models.Pedido import Pedido

class PedidoService(IPedidoService):
    def __init__(self, repository: PedidoRepository,
                 cardapioService: ICardapioService):
        self.repository = repository
        self.cardapioService = cardapioService

    def realizarPedido(self, pedido: Pedido):
        if pedido.estaVazio():
            raise HTTPException(
                status_code=422,
                detail="O pedido não possui itens"
            )

        if not self.cardapioService.reservarPorcoes(pedido.getItens()):
            raise HTTPException(status_code=422, detail="Um ou mais itens estão indisponíveis")

        return self.repository.salvar(pedido)

    def consultarPedido(self, id: int):
        pedido = self.repository.buscar_pedido(id)

        if pedido is None:
            raise HTTPException(
                status_code=404,
                detail="Pedido não encontrado"
            )

        return pedido

    def cancelarPedido(self, id: int):
        pedido = self.repository.buscar_pedido(id)

        if pedido is None:
            raise HTTPException(status_code=404, detail="Pedido não encontrado")

        if not pedido.podeCancelar(datetime.now()):
            raise HTTPException(status_code=422, detail="Pedido não pode ser cancelado")

        self.repository.cancelar_pedido(id)
