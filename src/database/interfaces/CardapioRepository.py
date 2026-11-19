from abc import ABC, abstractmethod
from src.models.Cardapio import Cardapio
from src.models.ItemCardapio import ItemCardapio
from typing import Optional

class CardapioRepository(ABC):
    # Busca sempre pelo cardápio mais recente
    @abstractmethod
    def buscar_cardapio(self) -> Optional[Cardapio]:
        pass

    # CardapioRepository salva tanto Cardapio quanto ItemCardapio
    @abstractmethod
    def salvar(self, Cardapio: Cardapio) -> None:
        pass