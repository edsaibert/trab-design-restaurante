from datetime import datetime

from sqlalchemy import Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.database import Base
from src.database.interfaces.PedidoRepository import PedidoRepository as IPedidoRepository

from src.models.Pedido import Pedido
from src.models.ItemPedido import ItemPedido


class PedidoORM(Base):
    __tablename__ = "pedido"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    data: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    data_ate_cancelamento: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    ativo: Mapped[bool] = mapped_column(Boolean, default=True)

    itens: Mapped[list["ItemPedidoORM"]] = relationship(
        back_populates="pedido",
        cascade="all, delete-orphan"
    )


class ItemPedidoORM(Base):
    __tablename__ = "item_pedido"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    pedido_id: Mapped[int] = mapped_column(ForeignKey("pedido.id"))
    idItemCardapio: Mapped[int] = mapped_column(ForeignKey("item_cardapio.id"))
    porcoes: Mapped[int] = mapped_column(Integer, nullable=False)

    pedido: Mapped["PedidoORM"] = relationship(back_populates="itens")


class SQLAlchemyPedidoRepository(IPedidoRepository):
    def __init__(self, db):
        self.db = db

    def salvar(self, pedido: Pedido) -> Pedido:

        orm = PedidoORM(
            data=pedido.data or datetime.now(),
            data_ate_cancelamento=pedido.data_ate_cancelamento,
            ativo=True,
            itens=[
                ItemPedidoORM(
                    idItemCardapio=item.idItemCardapio,
                    porcoes=item.porcoes
                )
                for item in pedido.itens
            ]
        )

        self.db.add(orm)

        try:
            self.db.commit()
            self.db.refresh(orm)
        except Exception:
            self.db.rollback()
            raise

        return self._para_entidade(orm)

    def buscar_pedido(self, id: int) -> Pedido | None:
        orm = self.db.get(PedidoORM, id)

        if orm is None:
            return None

        return self._para_entidade(orm)

    def cancelar_pedido(self, id: int) -> None:
        orm = self.db.get(PedidoORM, id)

        if orm is None:
            return

        orm.ativo = False

        try:
            self.db.commit()
        except Exception:
            self.db.rollback()
            raise

    def _para_entidade(self, orm):
        itens = [
            ItemPedido(
                id=item.id,
                idItemCardapio=item.idItemCardapio,
                porcoes=item.porcoes
            )
            for item in orm.itens
        ]

        pedido = Pedido(itens)

        pedido.id = orm.id
        pedido.data = orm.data
        pedido.data_ate_cancelamento = orm.data_ate_cancelamento
        pedido.ativo = orm.ativo

        return pedido
