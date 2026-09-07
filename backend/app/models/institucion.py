from app.config.database import Database


class Institucion:

#constructora

    def __init__(self, id_institucion=None, nombre=None, nit=None,
                 direccion=None, telefono=None, correo=None,
                 descripcion=None, codigo_admin=None, codigo_docente=None):
        self.id_institucion = id_institucion
        self.nombre = nombre
        self.nit = nit
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.descripcion = descripcion
        self.codigo_admin = codigo_admin
        self.codigo_docente = codigo_docente


#Busca la intitucion concorde al codigo dado puede ser de admin o docente
#devulve un dict con id_institucion e id_rol, None si no coincide
    @staticmethod
    def buscar_por_codigo(codigo):
        db = Database()
        query = """
        SELECT id_institucion, codigo_admin, codigo_docente
        FROM instituciones
        WHERE codigo_admin = %s OR codigo_docente = %s
        """
        resultado = db.ejecutar_query(query, (codigo, codigo))

        #Comprueba si el resultado es vacio o no
        if not resultado or len(resultado) == 0:
            return None

        #variable que toma resultado de la lista
        data = resultado[0]

        if data['codigo_admin'] == codigo:
            id_rol = 1  # Administrador
        else:
            id_rol = 2  # Docente

        #retornos
        return {
            'id_institucion': data['id_institucion'],
            'id_rol': id_rol
        }