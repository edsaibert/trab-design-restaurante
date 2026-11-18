from abc import ABC, abstractmethod

class IPedidoService(ABC):
    @abstractmethod
    def realizarPedido(self, nomesItens):
        pass

    @abstractmethod
    def consultarPedido(self, nomeItem):
        pass

    @abstractmethod
    def cancelarPedido(self, nomeItem):
        pass