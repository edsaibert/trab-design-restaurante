from src.interfaces.IPedidoService import IPedidoService
from src.models.Pedido import Pedido

class PedidoService(IPedidoService):
    def __init__(self, repository=None, cardapioService=None) -> None:
        self.repository = repository
        self.cardapioService = cardapioService

    def realizarPedido(self, Pedido: Pedido):
        pass

    def consultarPedido(self, id: int):
        pass

    def cancelarPedido(self, id: int):
        pass