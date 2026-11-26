from src.models.ItemCardapio import ItemCardapio 
from src.models.ItemPedido import ItemPedido

class Cardapio:
    def __init__(self, id, data,itens: list):
        self.id = id 
        self.data = data 
        self.itens = itens

    def criaItem(self, itemId, itemNome, itemPorcoes,
                 tamanhoPorcao, itemVegano, itemDisponibilidade):

        novoItem = ItemCardapio(
            id=itemId,
            nome=itemNome,
            porcoes=itemPorcoes,
            tamanhoPorcao=tamanhoPorcao,
            vegano=itemVegano,
            disponibilidade=itemDisponibilidade
        )

        return novoItem

    def adicionarItem(self, item):
        self.itens.append(item)

    def removerItem(self, itemId):
        item = next(
            (item for item in self.itens if item.id == itemId),
            None
        )

        if item is None:
            return False

        self.itens.remove(item)
        return True

    def atualizarItem(self, itemId, novoNome, novasPorcoes, novoTamanho, vegano):

        item = next(
            (item for item in self.itens if item.id == itemId),
            None
        )

        if item is None:
            return False

        item.nome = novoNome
        item.porcoes = novasPorcoes
        item.tamanhoPorcao = novoTamanho
        item.vegano = vegano
        item.atualizar_disponibilidade()

        return True

    def consultarDisponibilidade(self, itemId, quantidade):
        item = next(
            (item for item in self.itens if item.id == itemId),
            None
        )

        if item is None:
            return False

        return (
            item.disponibilidade
            and item.porcoes >= quantidade
        )

    def reservarPorcoes(self, itensPedido: list[ItemPedido]) -> bool:
        itensPorId = {item.id: item for item in self.itens}
        quantidadesPorItem = {}

        for itemPedido in itensPedido:
            quantidadesPorItem[itemPedido.idItemCardapio] = (
                quantidadesPorItem.get(itemPedido.idItemCardapio, 0)
                + itemPedido.porcoes
            )

        # Valida o pedido inteiro antes de alterar qualquer item.
        for itemId, quantidade in quantidadesPorItem.items():
            item = itensPorId.get(itemId)
            if (item is None or not item.disponibilidade
                    or item.porcoes < quantidade):
                return False

        for itemId, quantidade in quantidadesPorItem.items():
            item = itensPorId[itemId]
            item.porcoes -= quantidade
            if item.porcoes == 0:
                item.disponibilidade = False

        return True
