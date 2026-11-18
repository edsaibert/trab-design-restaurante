from src.models.Cardapio import Cardapio

class CardapioRepository:
    def __init__(self, db):
        self.db = db
        self.teste = None

    # def salvar(self, cardapio):
    #     self.db.merge(cardapio)
    #     self.db.commit()
    #     return cardapio

    # def buscar_cardapio(self, cardapioId):
    #     return self.db.get(Cardapio, cardapioId)

    def salvar(self, cardapio):
        self.teste = cardapio
        return cardapio

    def buscar_cardapio(self):
        return self.teste
