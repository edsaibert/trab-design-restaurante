from abc import ABC, abstractmethod

class IPedidoService(ABC):
    @abstractmethod
    def realizarPedido(nomesItens):
        pass

    @abstractmethod
    def consultarCardapio(nomeItem):
        pass