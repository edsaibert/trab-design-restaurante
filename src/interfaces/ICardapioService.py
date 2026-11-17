from abc import ABC, abstractmethod

class ICardapioService(ABC):
    @abstractmethod
    def alterarCardapio(self, useCase):
        pass