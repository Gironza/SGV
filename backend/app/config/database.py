import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # sube a app/
load_dotenv(os.path.join(BASE_DIR, ".env"))

class Database:
    def __init__(self):
        self.host = os.getenv("DB_HOST", "localhost")
        self.user = os.getenv("DB_USER", "postgres")
        self.password = os.getenv("DB_PASSWORD")
        self.database = os.getenv("DB_NAME", "SGV")
        self.port = os.getenv("DB_PORT", 5432)

    def obtener_conexion(self):
        try:
            conexion = psycopg2.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                dbname=self.database,
                port=self.port
            )
            return conexion
        except Exception as e:
            print(f"Error al conectar a PostgreSQL: {e}")
            return None

    def ejecutar_query(self, query, params=None):
        conexion = self.obtener_conexion()
        if not conexion:
            return None
        cursor = None
        try:
            cursor = conexion.cursor(cursor_factory=RealDictCursor)
            cursor.execute(query, params or ())

            if cursor.description is not None:
                resultado = [dict(row) for row in cursor.fetchall()]
                conexion.commit()
            else:
                conexion.commit()
                resultado = cursor.rowcount
            return resultado
        except Exception as e:
            print(f"Error ejecutando query: {e}")
            conexion.rollback()
            return None
        finally:
            if cursor:
                cursor.close()
            conexion.close()