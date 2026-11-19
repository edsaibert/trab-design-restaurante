from datetime import datetime

from sqlalchemy import Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.database import Base
from src.database.interfaces.CardapioRepository import CardapioRepository as ICardapioRepository

from src.models.Cardapio import Cardapio
from src.models.ItemCardapio import ItemCardapio


class CardapioORM(Base):
    __tablename__ = "cardapio"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    data: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    itens: Mapped[list["ItemCardapioORM"]] = relationship(
        back_populates="cardapio",
        cascade="all, delete-orphan"
    )


class ItemCardapioORM(Base):
    __tablename__ = "item_cardapio"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    cardapio_id: Mapped[int] = mapped_column(ForeignKey("cardapio.id"))

    nome: Mapped[str] = mapped_column(String(100))
    porcoes: Mapped[int] = mapped_column(Integer)
    tamanhoPorcao: Mapped[int] = mapped_column(Integer)
    vegano: Mapped[bool] = mapped_column(Boolean)
    disponibilidade: Mapped[bool] = mapped_column(Boolean)

    cardapio: Mapped["CardapioORM"] = relationship(back_populates="itens")


# Repository

class SQLAlchemyCardapioRepository(ICardapioRepository):
    def __init__(self, db):
        self.db = db

    def salvar(self, cardapio: Cardapio) -> Cardapio:

        if cardapio.id is None:
            orm = CardapioORM(data=cardapio.data)
            self.db.add(orm)
            self.db.flush()
        else:
            orm = self.db.get(CardapioORM, cardapio.id)

            if orm is None:
                raise ValueError("Cardápio não encontrado")

            orm.data = cardapio.data

        itens_existentes = {item.id: item for item in orm.itens}
        novos_itens = []

        for item in cardapio.itens:
            if item.id is not None and item.id in itens_existentes:
                item_orm = itens_existentes[item.id]
                item_orm.nome = item.nome
                item_orm.porcoes = item.porcoes
                item_orm.tamanhoPorcao = item.tamanhoPorcao
                item_orm.vegano = item.vegano
                item_orm.disponibilidade = item.disponibilidade
                novos_itens.append(item_orm)
            else:
                novos_itens.append(
                    ItemCardapioORM(
                        nome=item.nome,
                        porcoes=item.porcoes,
                        tamanhoPorcao=item.tamanhoPorcao,
                        vegano=item.vegano,
                        disponibilidade=item.disponibilidade
                    )
                )

        # Remove itens que não estão mais no cardápio
        orm.itens = novos_itens

        try:
            self.db.commit()
            self.db.refresh(orm)
        except Exception:
            self.db.rollback()
            raise

        return self._para_entidade(orm)

    def buscar_cardapio(self) -> Cardapio | None:
        orm = (
            self.db.query(CardapioORM)
            .order_by(CardapioORM.data.desc())
            .first()
        )

        if orm is None:
            return None

        return self._para_entidade(orm)

    def _para_entidade(self, orm):
        itens = [
            ItemCardapio(
                id=item.id,
                nome=item.nome,
                porcoes=item.porcoes,
                tamanhoPorcao=item.tamanhoPorcao,
                vegano=item.vegano,
                disponibilidade=item.disponibilidade
            )
            for item in orm.itens
        ]

        return Cardapio(
            id=orm.id,
            data=orm.data,
            itens=itens
        )