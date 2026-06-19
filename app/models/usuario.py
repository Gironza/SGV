from app.config.database import Database
 
 
class Usuario:
 
    def __init__(self, id_usuario=None, id_institucion=None, documento=None,
                 id_tipo_doc=None, nombre=None, apellido=None, correo=None,
                 contrasena=None, curso=None, id_rol=None):
        self.id_usuario = id_usuario
        self.id_institucion = id_institucion
        self.documento = documento
        self.id_tipo_doc = id_tipo_doc
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.contrasena = contrasena
        self.curso = curso
        self.id_rol = id_rol
        self.rol_nombre = None
 
    def guardar(self):
        db = Database()
        query = """
        INSERT INTO usuarios
            (id_institucion, documento, id_tipo_doc, nombre, apellido,
             correo, contrasena, curso, id_rol)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (
            self.id_institucion, self.documento, self.id_tipo_doc,
            self.nombre, self.apellido, self.correo, self.contrasena,
            self.curso, self.id_rol
        )
 
        resultado = db.ejecutar_query(query, params)
        return resultado is not None
 
    @staticmethod
    def buscar_por_correo(correo):
        db = Database()
        query = """
        SELECT
            u.id_usuario, u.id_institucion, u.documento, u.id_tipo_doc,
            u.nombre, u.apellido, u.correo, u.contrasena, u.curso, u.id_rol,
            r.nombre AS rol_nombre
        FROM usuarios u
        INNER JOIN roles r ON u.id_rol = r.id_rol
        WHERE u.correo = %s
        """
 
        resultado = db.ejecutar_query(query, (correo,))
 
        if resultado and len(resultado) > 0:
            data = resultado[0]
            usuario = Usuario(
                id_usuario=data['id_usuario'],
                id_institucion=data['id_institucion'],
                documento=data['documento'],
                id_tipo_doc=data['id_tipo_doc'],
                nombre=data['nombre'],
                apellido=data['apellido'],
                correo=data['correo'],
                contrasena=data['contrasena'],
                curso=data['curso'],
                id_rol=data['id_rol'],
            )
            usuario.rol_nombre = data['rol_nombre']
            return usuario
        return None
 
    @staticmethod
    def extraer_usuarios(id_institucion=None):
        db = Database()
        query = """
        SELECT
            u.id_usuario, u.documento, u.nombre, u.apellido, u.correo,
            u.curso, r.nombre AS rol_nombre
        FROM usuarios u
        INNER JOIN roles r ON u.id_rol = r.id_rol
        """
        params = None
        if id_institucion is not None:
            query += " WHERE u.id_institucion = %s"
            params = (id_institucion,)
        query += " ORDER BY u.id_usuario"
 
        return db.ejecutar_query(query, params)
 
    @staticmethod
    def usuario_existente(correo):
        db = Database()
        query = "SELECT COUNT(*) as count FROM usuarios WHERE correo = %s"
        resultado = db.ejecutar_query(query, (correo,))
        return resultado[0]['count'] > 0 if resultado else False
 
    @staticmethod
    def documento_existente(documento):
        db = Database()
        query = "SELECT COUNT(*) as count FROM usuarios WHERE documento = %s"
        resultado = db.ejecutar_query(query, (documento,))
        return resultado[0]['count'] > 0 if resultado else False