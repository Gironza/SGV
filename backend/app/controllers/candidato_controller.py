import logging
from app.models.candidato import Candidato
from app.models.eleccion import Eleccion
from app.models.usuario import Usuario

logger = logging.getLogger(__name__)


class CandidatoController:

    def inscribir(self, id_usuario, id_eleccion, propuesta, foto):
        try:
            eleccion = Eleccion.obtener_por_id(id_eleccion)
            if not eleccion:
                return {'success': False, 'message': 'Elección no encontrada'}

            if eleccion['id_estado_eleccion'] == 2:
                return {'success': False, 'message': 'No puedes inscribirte en una elección finalizada'}

            id_institucion_usuario = Usuario.obtener_institucion(id_usuario)
            if id_institucion_usuario != eleccion['id_institucion']:
                return {'success': False, 'message': 'No perteneces a la institución de esta elección'}

            if Candidato.ya_inscrito(id_usuario, id_eleccion):
                return {'success': False, 'message': 'Ya estás inscrito como candidato en esta elección'}

            id_candidato = Candidato.crear(id_usuario, propuesta, foto, id_eleccion)
            if id_candidato is None:
                return {'success': False, 'message': 'Error al inscribir la candidatura'}

            return {'success': True, 'message': 'Candidatura inscrita exitosamente', 'id_candidato': id_candidato}
        except Exception as e:
            logger.error(f"Error al inscribir candidato: {e}")
            return {'success': False, 'message': 'Error en el sistema, intenta más tarde'}

    def listar_por_eleccion(self, id_eleccion):
        try:
            if not Eleccion.obtener_por_id(id_eleccion):
                return {'success': False, 'message': 'Elección no encontrada'}
            return {'success': True, 'candidatos': Candidato.listar_por_eleccion(id_eleccion) or []}
        except Exception as e:
            logger.error(f"Error al listar candidatos: {e}")
            return {'success': False, 'message': 'Error en el sistema, intenta más tarde'}

    def retirar_candidatura(self, id_candidato, id_usuario_solicitante):
        try:
            candidato = Candidato.obtener_por_id(id_candidato)
            if not candidato:
                return {'success': False, 'message': 'Candidatura no encontrada'}

            if candidato['id_usuario'] != id_usuario_solicitante:
                return {'success': False, 'message': 'No puedes retirar la candidatura de otro estudiante'}

            if Candidato.tiene_votos(id_candidato):
                return {'success': False, 'message': 'No se puede retirar: la candidatura ya tiene votos registrados'}

            if not Candidato.eliminar(id_candidato):
                return {'success': False, 'message': 'Error al retirar la candidatura'}

            return {'success': True, 'message': 'Candidatura retirada exitosamente'}
        except Exception as e:
            logger.error(f"Error al retirar candidatura: {e}")
            return {'success': False, 'message': 'Error en el sistema, intenta más tarde'}