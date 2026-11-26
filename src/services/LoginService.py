from datetime import datetime, timedelta, timezone
from fastapi import HTTPException
import jwt
import bcrypt

CHAVE = "ch4v3"
ALGORITHM = "HS256"
TEMPO_TOKEN = 60

class LoginService:
    def __init__(self):
        pass


    def hash_senha(self, plain_password: str) -> str:
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(plain_password.encode("utf-8"), salt)
        return hashed.decode("utf-8")


    def verify_password(self, plain_password: str, senha_hashed: str) -> bool:
        return bcrypt.checkpw(
            plain_password.encode("utf-8"), senha_hashed.encode("utf-8")
        )


    def cria_token(self, user_id: str, usuario: str) -> str:
        validade = datetime.now(timezone.utc) + timedelta(
            minutes=TEMPO_TOKEN
        )
        payload = {"sub": str(user_id), "usuario": usuario, "exp": validade}
        return jwt.encode(payload, CHAVE, algorithm="HS256")


    def autenticar(self, usuario: str, senha: str) -> dict:
        # mock para simular auth externa
        user = self.get_user_mock(usuario)

        if not user or not self.verify_password(senha, user["senha_hashed"]):
            raise HTTPException(
                status_code=401,
                detail="Usuário ou senha incorretos."
            )

        # gera token
        token = self.cria_token(user_id=user["id"], usuario=user["usuario"])

        return {
            "token": token,
            "token_tipo": "bearer",
            "user": {"id": user["id"], "usuario": user["usuario"]},
        }


    # mock db
    def get_user_mock(self, usuario: str):
        if usuario == "admin":
            return {
                "id": 0,
                "usuario": "admin",
                "senha_hashed": self.hash_senha("admin"),
            }

        if usuario == "usuario":
            return {
                "id": 0,
                "usuario": "usuario",
                "senha_hashed": self.hash_senha("usuario"),
            }

        return None