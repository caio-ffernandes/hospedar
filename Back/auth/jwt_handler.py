import jwt
from datetime import datetime, timedelta
from fastapi import HTTPException, Depends, Header
from models.usuarios import UsuariosDB

SECRET_KEY = "seu_secret_key"
ALGORITHM = "HS256"


def criar_token(usuario_id: int, tipo: str):
    exp = datetime.utcnow() + timedelta(days=1)  # Token válido por 1 dia
    return jwt.encode({"sub": usuario_id, "tipo": tipo, "exp": exp}, SECRET_KEY, algorithm=ALGORITHM)


def verificar_token(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Token não encontrado")

    token = authorization.split(" ")[1]  # Espera o formato "Bearer <token>"

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token inválido")
