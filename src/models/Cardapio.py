from src.models.Item import Item
import datetime

class Cardapio:
    def __init__(self, cardapio_id, data):
        self.cardapio_id = cardapio_id
        self.data = data.date
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)
        print("item adicionado")

    def remover_item(self, id):
        for indiceItem, item in enumerate(self.itens):
            if item.id == id:
                self.itens.pop(indiceItem)
                print("item removido")
                return

        print("item nao encontrado")

    def atualizar_item(self, id, novoNome, novasPorcoes, novoTamanho, vegano):
        for item in self.itens:
            if item.id == id:
                item.nome = novoNome
                item.porcoes = novasPorcoes
                item.tamanhoPorcao = novoTamanho
                item.vegano = vegano
                print("item atualizado")
                return
        print("item nao encontrado")

    def cardapio_itens(self):
        if not self.itens:
            print("nenhum item no cardapio")
            return []

        print("cardapio:")
        for item in self.itens:
            print(f"- id: {item.item_id} | nome: {item.nome} | porcoes: {item.porcoes}")
        return self.itens