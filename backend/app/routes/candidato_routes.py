from typing import List
from fastapi import APIRouter, HTTPException, Depends
from app.schemas.candidato_schema import (
    CandidatoCreate, CandidatoOut, CandidatoCreadoResponse, MensajeResponse
)
from app.controllers.candidato_controller import CandidatoController
from app.middleware.auth_middleware import obtener_usuario_actual, requerir_rol

router = APIRouter(prefix="/candidatos", tags=["Candidatos"])
candidato_controller = CandidatoController()


@router.post("/", response_model=CandidatoCreadoResponse)
def inscribir_candidato(datos: CandidatoCreate, usuario_actual: dict = Depends(requerir_rol(3))):
    resultado = candidato_controller.inscribir(
        usuario_actual['id_usuario'], datos.id_eleccion, datos.propuesta, datos.foto
    )
    if not resultado['success']:
        raise HTTPException(status_code=400, detail=resultado['message'])
    return resultado


@router.get("/eleccion/{id_eleccion}", response_model=List[CandidatoOut])
def listar_candidatos(id_eleccion: int, usuario_actual: dict = Depends(obtener_usuario_actual)):
    resultado = candidato_controller.listar_por_eleccion(id_eleccion)
    if not resultado['success']:
        raise HTTPException(status_code=404, detail=resultado['message'])
    return resultado['candidatos']


@router.delete("/{id_candidato}", response_model=MensajeResponse)
def retirar_candidatura(id_candidato: int, usuario_actual: dict = Depends(requerir_rol(3))):
    resultado = candidato_controller.retirar_candidatura(id_candidato, usuario_actual['id_usuario'])
    if not resultado['success']:
        raise HTTPException(status_code=400, detail=resultado['message'])
    return resultado