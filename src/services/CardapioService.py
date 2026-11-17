from src.models.Cardapio import Cardapio

class CardapioService:
    def __init__(self, cardapioRepository):
        self.cardapioRepository = cardapioRepository

    def criarCardapio(self, cardapioId, data, dicioItens):
        novoCardapio = Cardapio(
            cardapioId = cardapioId, 
            data = data, 
            dicioItens = dicioItens
        )
        
        return novoCardapio

    def salvarCardapio(self, cardapio):
        self.cardapioRepository.salvar(cardapio)

    def consultarCardapio(self, cardapio):
        return cardapio.dicioItens.values()

    def atualizarCardapio(self, cardapio, listaAtualizacoes):
        for itemId in listaAtualizacoes.dicioItens:
            if itemId in cardapio.dicioItens:
                itemLista = listaAtualizacoes.dicioItens[itemId]
                cardapio.atualizar_item(
                    itemId,
                    itemLista.nome,
                    itemLista.porcoes,
                    itemLista.tamanhoPorcao,
                    itemLista.vegano
                )
    
        self.cardapioRepository.salvar(cardapio)