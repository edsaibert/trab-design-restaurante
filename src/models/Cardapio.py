from src.models.Item import Item
import datetime

class Cardapio:
    def __init__(self, cardapioId, data, dicioItens: dict):
        self.cardapioId = cardapioId
        self.data = data.date() 
        self.dicioItens = dicioItens

    def cria_item(self, itemId, itemNome, itemPorcoes, 
                    tamanhoPorcao, itemVegano, itemDisponibilidade):
        novoItem = Item(id = itemId, nome = itemNome, porcoes = itemPorcoes,
                            tamanhoPorcao = tamanhoPorcao, vegano = itemVegano, disponibilidade = itemDisponibilidade)

        return novoItem
        
    def adicionar_item(self, item):
        self.dicioItens[item.id] = item

    def remover_item(self, itemId):
        self.dicioItens.pop(itemId)

    def atualizar_item(self, itemId, novoNome, novasPorcoes, novoTamanho, vegano):
        self.dicioItens[itemId].nome = novoNome
        self.dicioItens[itemId].porcoes = novasPorcoes
        self.dicioItens[itemId].tamanhoPorcao = novoTamanho
        self.dicioItens[itemId].vegano = getVegano
        self.dicioItens[itemId].atualizar_disponibilidade()

    def consultar_disponibilidade(self, cardapio, itemId, quantidade):
        return self.dicioItens[itemId].disponibilidade