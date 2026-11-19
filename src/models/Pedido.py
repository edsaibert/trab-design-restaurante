from src.models.ItemPedido import ItemPedido
from datetime import timedelta

class Pedido:
    def __init__(self, itens: list[ItemPedido]):
        self.id = None
        self.itens = itens
        self.data = None
        self.data_ate_cancelamento = None
        self.ativo = None

    def getItens(self):
        return self.itens

    def adicionarItem(self, item: ItemPedido):
        if item.porcoes <= 0:
            raise ValueError("A quantidade de porções deve ser positiva")

        self.itens.append(item)

    def removerItem(self, idItem):
        item = next(
            (item for item in self.itens if item.id == idItem),
            None
        )

        if item is None:
            return False

        self.itens.remove(item)
        return True

    def estaVazio(self):
        return len(self.itens) == 0

    def podeCancelar(self, dataAtual):
        if self.data is None:
            return False

        return dataAtual <= (self.data + timedelta(seconds=2))