import logging
from app.config.database import Database

logger = logging.getLogger(__name__)


class Candidato:

    @staticmethod
    def crear(id_usuario, propuesta, foto, id_eleccion):
        db = Database()
        query = """
        INSERT INTO candidatos (id_usuario, propuesta, foto, id_eleccion)
        VALUES (%s, %s, %s, %s)
        RETURNING id_candidato
        """
        resultado = db.ejecutar_query(query, (id_usuario, propuesta, foto, id_eleccion))
        return resultado[0]['id_candidato'] if resultado else None

    @staticmethod
    def ya_inscrito(id_usuario, id_eleccion):
        db = Database()
        query = """
        SELECT 1 FROM candidatos WHERE id_usuario = %s AND id_eleccion = %s
        """
        resultado = db.ejecutar_query(query, (id_usuario, id_eleccion))
        return bool(resultado)

    @staticmethod
    def obtener_por_id(id_candidato):
        db = Database()
        query = """
        SELECT c.id_candidato, c.id_usuario, c.propuesta, c.foto, c.id_eleccion,
               u.nombre, u.apellido
        FROM candidatos c
        INNER JOIN usuarios u ON c.id_usuario = u.id_usuario
        WHERE c.id_candidato = %s
        """
        resultado = db.ejecutar_query(query, (id_candidato,))
        return resultado[0] if resultado else None

    @staticmethod
    def listar_por_eleccion(id_eleccion):
        db = Database()
        query = """
        SELECT c.id_candidato, u.nombre, u.apellido, c.propuesta, c.foto
        FROM candidatos c
        INNER JOIN usuarios u ON c.id_usuario = u.id_usuario
        WHERE c.id_eleccion = %s
        """
        return db.ejecutar_query(query, (id_eleccion,))

    @staticmethod
    def pertenece_a_eleccion(id_candidato, id_eleccion):
        db = Database()
        query = """
        SELECT 1 FROM candidatos WHERE id_candidato = %s AND id_eleccion = %s
        """
        resultado = db.ejecutar_query(query, (id_candidato, id_eleccion))
        return bool(resultado)

    @staticmethod
    def tiene_votos(id_candidato):
        db = Database()
        query = "SELECT 1 FROM votos WHERE id_candidato = %s"
        resultado = db.ejecutar_query(query, (id_candidato,))
        return bool(resultado)

    @staticmethod
    def eliminar(id_candidato):
        db = Database()
        query = "DELETE FROM candidatos WHERE id_candidato = %s"
        resultado = db.ejecutar_query(query, (id_candidato,))
        return resultado is not None and resultado > 0