from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.utils.jwt_handler import verificar_token

security_scheme = HTTPBearer()


def obtener_usuario_actual(credenciales: HTTPAuthorizationCredentials = Depends(security_scheme)) -> dict:
    """
    Verifica el JWT del header Authorization.
    Devuelve el payload (id_usuario, rol) si es válido.
    Lanza 401 si el token falta, es inválido o expiró.
    """
    token = credenciales.credentials
    payload = verificar_token(token)

    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )

    try:
        return {
            "id_usuario": int(payload["sub"]),
            "id_rol": payload["rol"]
        }
    except (KeyError, ValueError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token con formato inválido",
            headers={"WWW-Authenticate": "Bearer"},
        )

def requerir_rol(*roles_permitidos: int):
    """
    Fábrica de dependencias: exige que el usuario autenticado
    tenga uno de los roles indicados. Uso: Depends(requerir_rol(1))
    """
    def verificar_rol(usuario: dict = Depends(obtener_usuario_actual)) -> dict:
        if usuario["id_rol"] not in roles_permitidos:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="No tienes permisos para acceder a este recurso"
            )
        return usuario
    return verificar_rol