from abc import ABC, abstractmethod
from src.models.Pedido import Pedido
from typing import Optional

class PedidoRepository(ABC):
    @abstractmethod
    def salvar(self, pedido: Pedido) -> None:
        pass

    @abstractmethod
    def buscar_pedido(self, id) -> Optional[Pedido]:
        pass

    @abstractmethod
    def cancelar_pedido(self, id) -> None:
        pass
        
