# from Log import Log (???)

class Pedido:
    def __init__(self, dicioItens: dict, id):
        self.dicioItens = dicioItens
        self.id = id

    def getItemPedido(self, idItem):
        return self.dicioItens[idItem]

    def getDicioItens(self):
        return self.dicioItens

    def adicionarItem(self, item):
        if item.disponibilidade() is True:
            self.dicioItens[item.getId()] = {
                "nome": item.getNome(),
                "porcoes": item.getPorcoes(),
                "tam_porcoes": item.getTamanhoPorcoes(),
                "vegano": item.getVegano()
            }
        else:
            print("Item indisponível no cardápio")

    def removerItem(self, idItem):
        return self.dicioItens.pop(idItem)

    def registrarPedido(self, log):
        log.adicionarLog("Pedido registrado", self.id, self.dicioItens)