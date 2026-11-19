from datetime import datetime

from src.models.Cardapio import Cardapio
from src.database.interfaces.CardapioRepository import CardapioRepository

class SQLAlchemyCardapioRepository(CardapioRepository):
    # Não implementado, apenas Mock
    def __init__(self, db):
        self.db = db
        self.teste = None
        self.next_id = 1
        self.next_item_id = 1

    # def salvar(self, cardapio):
    #     self.db.merge(cardapio)
    #     self.db.commit()
    #     return cardapio

    # def buscar_cardapio(self, cardapioId):
    #     return self.db.get(Cardapio, cardapioId)

    def salvar(self, cardapio: Cardapio) -> Cardapio:
        if cardapio.id is None:
            cardapio.id = self.next_id
            self.next_id += 1

        for item in cardapio.itens:
            if item.id is None:
                item.id = self.next_item_id
                self.next_item_id += 1

        cardapio.data = datetime.now()
        self.teste = cardapio

        return cardapio

    def buscar_cardapio(self) -> Cardapio:
        return self.teste


