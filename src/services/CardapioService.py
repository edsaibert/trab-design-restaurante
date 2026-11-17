from src.models.Cardapio import Cardapio

class CardapioService:
    def __init__(self, ):

    def criar_cardapio(self, cardapioId, data):
        novoCardapio = Cardapio(cardapioId = cardapioId, data = data, itens = [])
        return novoCardapio

    def consultar_cardapio(self, cardapio):
        return cardapio.itens

    def atualizar_cardapio(self, cardapio, listaAtualizacoes):
        for itemLista in listaAtualizacoes:
            for itemCardapio in cardapio:
                if itemLista.id == itemCardapio.id:
                    cardapio.atualizar_item(itemLista.id, itemLista.nome, itemLista.porcoes,
                        itemLista.tamanhoPorcao, itemLista.vegano)
        
        return cardapio