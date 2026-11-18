from src.models.ItemCardapio import ItemCardapio 

class Cardapio:
    def __init__(self, itens: list):
        self.id = None
        self.data = None
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
