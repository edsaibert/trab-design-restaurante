from src.models.Cardapio import Cardapio

class CardapioRepository:
    def __init__(self, db):
        self.db = db

    def salvar(self, cardapio):
        self.db.merge(cardapio)
        self.db.commit()
        return cardapio

    def buscar_cardapio(self, cardapioId):
        return self.db.get(Cardapio, cardapioId)