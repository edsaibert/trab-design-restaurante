from src.models.Cardapio import Cardapio

class CardapioService:
    def criarCardapio(self, cardapioId, data, dicioItens):
        novoCardapio = Cardapio(
            cardapioId = cardapioId, 
            data = data, 
            dicioItens = dicioItens
        )
        
        return novoCardapio

    def consultarCardapio(self, cardapio):
        return cardapio.itens

    def atualizarCardapio(self, cardapio, listaAtualizacoes):
        for itemLista in listaAtualizacoes:
            for itemCardapio in cardapio:
                if itemLista.id == itemCardapio.id:
                    cardapio.atualizar_item(itemLista.id, itemLista.nome, itemLista.porcoes,
                        itemLista.tamanhoPorcao, itemLista.vegano)
        
        return cardapio