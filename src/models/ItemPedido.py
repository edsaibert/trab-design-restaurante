
class ItemPedido:
    def __init__(self, id: int, idItemCardapio: int, porcoes: int) -> None:
        self.id = id
        self.idItemCardapio = idItemCardapio
        self.porcoes = porcoes
