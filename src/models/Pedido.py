from src.models.ItemPedido import ItemPedido

class Pedido:
    def __init__(self, itens: list[ItemPedido], id: int) -> None:
        self.itens = itens
        self.id = id

    def getItemPedido(self, idItem):
        return next(
            (item for item in self.itens if item.id == idItem),
            None
        )

    def getItens(self):
        return self.itens

    def adicionarItem(self, item):
        if item.disponibilidade is True:
            self.itens.append(item)
            return True

        print("Item indisponível no cardápio")
        return False

    def removerItem(self, idItem):
        item = self.getItemPedido(idItem)

        if item is None:
            return False

        self.itens.remove(item)
        return True

    #def registrarPedido(self, log):
        #log.adicionarLog("Pedido registrado", self.id, self.itens)
        #log é adicionado pelo service

        #pass