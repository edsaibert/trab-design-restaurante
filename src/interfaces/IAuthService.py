from abc import ABC, abstractmethod

class IAuthService(ABC):
    @abstractmethod
    def autenticar(self, usuario, senha):
        pass