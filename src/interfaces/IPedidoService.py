from abc import ABC, abstractmethod

class IPedidoService(ABC):
    @abstractmethod
    def realizarPedido(self, nomesItens):
        pass

    @abstractmethod
    def consultarCardapio(self, nomeItem):
        pass

    @abstractmethod
    def cancelarCardapio(self, nomeItem):
        pass