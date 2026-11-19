from src.database.database import Base, engine

from src.database.SQLAlchemyCardapioRepository import CardapioORM, ItemCardapioORM
from src.database.SQLAlchemyPedidoRepository import PedidoORM, ItemPedidoORM

Base.metadata.create_all(bind=engine)