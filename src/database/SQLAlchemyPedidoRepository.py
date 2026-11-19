from src.database.interfaces.PedidoRepository import PedidoRepository
from src.models.Pedido import Pedido

from fastapi import HTTPException, status
from datetime import datetime
from typing import Optional

#Nas tabelas, o Pedido tem a data em que foi realizado, a data até seu cancelamento e se está ativo ou não

class SQLAlchemyPedidoRepository(PedidoRepository):
    # Não implementado, apenas Mock
    def __init__(self):
        self.pedidos = []
        self.next_pedido_id = 1
        self.next_item_id = 1

    def salvar(self, pedido):
        pedido.id = self.next_pedido_id
        self.next_pedido_id += 1

        for item in pedido.itens:
            item.id = self.next_item_id
            self.next_item_id += 1

        pedido.data = datetime.now()
        pedido.ativo = True

        self.pedidos.append(pedido)
        return pedido

    def buscar_pedido(self, id) -> Optional[Pedido]:
        for item in self.teste:
            if item.id == id:
                return item

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Pedido não encontrado."
        )

    def cancelar_pedido(self, id) -> None:
        item = self.buscar_pedido(id)
        if (item):
            item.ativo = False




