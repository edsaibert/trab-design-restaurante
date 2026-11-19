from fastapi import HTTPException

from src.interfaces.ICardapioService import ICardapioService
from src.models.ItemCardapio import ItemCardapio
from src.models.Cardapio import Cardapio

from datetime import datetime

class CardapioService(ICardapioService):
    def __init__(self, cardapioRepository):
        self.cardapioRepository = cardapioRepository

    def consultarCardapio(self):
        cardapio = self.cardapioRepository.buscar_cardapio()

        if cardapio is None: 
            raise HTTPException(status_code=404, detail="Cardápio não encontrado")

        return cardapio

    def criarCardapio(self, listaItens: list[ItemCardapio]): 
        cardapio = Cardapio(
            id = None,
            data=datetime.now(),
            itens=listaItens
        )
        return self.cardapioRepository.salvar(cardapio)

    def atualizarCardapio(self, listaAtualizacoes: list[ItemCardapio]):
        cardapio = self.cardapioRepository.buscar_cardapio()

        if cardapio is None:
            raise HTTPException(status_code=404, detail="Cardápio não encontrado")

        for itemAtualizacao in listaAtualizacoes:
            atualizado = cardapio.atualizarItem(
                itemAtualizacao.id,
                itemAtualizacao.nome,
                itemAtualizacao.porcoes,
                itemAtualizacao.tamanhoPorcao,
                itemAtualizacao.vegano
            )

            if not atualizado:
                raise ValueError(
                    f"Item {itemAtualizacao.id} não encontrado no cardápio"
                )

        return self.cardapioRepository.salvar(cardapio)

    def consultarDisponibilidade(self, idItem, quantidade):
        cardapio = self.cardapioRepository.buscar_cardapio()

        if cardapio is None:
            return False

        return cardapio.consultarDisponibilidade(
            idItem,
            quantidade
        )
