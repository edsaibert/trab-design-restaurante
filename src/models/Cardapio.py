from src.models.Item import Item
import datetime

class Cardapio:
    def __init__(self, cardapioId, data):
        self.cardapioId = cardapioId
        self.data = data.date() 
        self.itens = []

    def cria_item(self, itemId, itemNome, itemPorcoes, 
                    tamanhoPorcao, itemVegano, itemDisponibilidade):
        novoItem = Item(id = itemId, nome = itemNome, porcoes = itemPorcoes,
                            tamanhoPorcao = tamanhoPorcao, vegano = itemVegano, disponibilidade = itemDisponibilidade)

        return novoItem
        
    def adicionar_item(self, cardapio, item):
        cardapio.itens.append(item)

    def remover_item(self, cardapio, itemId):
        for indiceItem, item in enumerate(cardapio.itens):
            if item.id == itemId:
                cardapio.itens.pop(indiceItem)
                return
    
    def atualizar_item(self, itemId, novoNome, novasPorcoes, novoTamanho, vegano):
        for item in self.itens:
            if item.id == itemId:
                item.nome = novoNome
                item.porcoes = novasPorcoes
                item.tamanhoPorcao = novoTamanho
                item.vegano = vegano
                return

    def consultar_disponibilidade(self, cardapio, itemId, quantidade):
        for item in cardapio.itens:
            if item.id == itemId:
                return item.disponibilidade(quantidade)
        return False