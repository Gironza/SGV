import psycopg2
from psycopg2.extras import RealDictCursor
 
class Database:
    def __init__(self):
        self.host = "localhost"
        self.user = "postgres"
        self.password = "1234"      
        self.database = "SGV"     
        self.port = 5432            
 
    def get_connection(self):
        try:
            connection = psycopg2.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                dbname=self.database,
                port=self.port
            )
            return connection
        except Exception as e:
            print(f"Error al conectar a PostgreSQL: {e}")
            return None
 
    def ejecutar_query(self, query, params=None):
        connection = self.get_connection()
        if not connection:
            return None
        try:
            cursor = connection.cursor(cursor_factory=RealDictCursor)
            cursor.execute(query, params or ())
            if query.strip().upper().startswith("SELECT"):
                resultado = [dict(row) for row in cursor.fetchall()]
            else:
                connection.commit()
                resultado = cursor.rowcount
            return resultado
        except Exception as e:
            print(f"Error ejecutando query: {e}")
            connection.rollback()
            return None
        finally:
            cursor.close()
            connection.close()
 