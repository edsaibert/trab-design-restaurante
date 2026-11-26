from abc import ABC, abstractmethod
from src.models.ItemCardapio import ItemCardapio
from src.models.ItemPedido import ItemPedido

class ICardapioService(ABC):

    # @abstractmethod
    # def criarCardapio(self):
    #     pass

    @abstractmethod
    def consultarCardapio(self):
        pass

    @abstractmethod
    def criarCardapio(self, listaItens: list[ItemCardapio]):
        pass

    @abstractmethod
    def atualizarCardapio(self, listaAtualizacoes: list[ItemCardapio]):
        pass

    @abstractmethod
    def consultarDisponibilidade(self, idItem, quantidade) -> bool:
        pass

    @abstractmethod
    def reservarPorcoes(self, itensPedido: list[ItemPedido]) -> bool:
        pass
