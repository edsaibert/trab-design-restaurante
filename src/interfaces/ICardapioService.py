from abc import ABC, abstractmethod

class ICardapioService(ABC):

    # @abstractmethod
    # def criarCardapio(self):
    #     pass

    @abstractmethod
    def consultarCardapio(self):
        pass

    @abstractmethod
    def criarCardapio(self, listaItens: list):
        pass

    @abstractmethod
    def atualizarCardapio(self, listaAtualizacoes):
        pass

    @abstractmethod
    def consultarDisponibilidade(self, idItem, quantidade) -> bool:
        pass