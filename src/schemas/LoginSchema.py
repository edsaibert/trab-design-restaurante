from pydantic import BaseModel, Field, model_validator
from typing import Any
from itertools import count
from datetime import datetime

class LoginSchema(BaseModel):
    usuario: str
    senha: str