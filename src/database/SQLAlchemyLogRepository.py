from src.database.interfaces.LogRepository import LogRepository
from datetime import datetime


class SQLAlchemyLogRepository(LogRepository):
    ## não implementado, mockado
    def __init__(self):
        self.logs = []

    def salvar(self, msg: dict):
        msg["data"] = datetime.now()
        self.logs.append(msg)

    def buscar_log(self) -> list:
        return self.logs
        