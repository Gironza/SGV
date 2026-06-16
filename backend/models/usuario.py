from config.database import Database

#Parametros del usuario
class Usuario:
    def __init__(self, usuario_id=None, usuario_usuario=None, usuario_contrasena=None, usuario_documento=None,
        usuario_nombre=None, usuario_apellido=None, 
        usuario_estado_id=None, rol_id=None, usuario_curso=None) :
        self.usuario_id=usuario_id
        self.usuario_usuario=usuario_usuario 
        self.usuario_contrasena=usuario_contrasena
        self.usuario_documento=usuario_documento
        self.usuario_nombre=usuario_nombre
        self.usuario_apellido=usuario_apellido
        self.usuario_estado_id=usuario_estado_id
        self.rol_id=rol_id
        self.usuario_curso=usuario_curso
        

    def guardar(self):
        db = Database()
        query = """
        INSERT INTO usuario(usuario_usuario, usuario_contrasena, usuario_documento, usuario_nombre,
        usuario_apellido, usuario_estado_id, rol_id, usuario_curso) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        
        params=(self.usuario_usuario, self.usuario_contrasena, self.usuario_documento,
                self.usuario_nombre,  self.usuario_apellido,
                self.usuario_estado_id, self.rol_id, self.usuario_curso)
        
        print(f"Debug - Parámetros antes de insertar: {params}")
        print(f"Debug - Tipo de rol_id: {type(self.rol_id)}")
        
        resultado= db.ejecutar_query(query, params)
        return resultado is not None
    
    @staticmethod
    def buscar_por_usuario(usuario_usuario):
        db = Database()
        query = """
        SELECT 
        u.usuario_id, u.usuario_usuario, u.usuario_contrasena, u.usuario_documento,
        u.usuario_nombre, u.usuario_apellido, u.usuario_estado_id, u.rol_id, u.usuario_curso,
        r.rol_nombre as rol_nombre
        FROM usuario u
        INNER JOIN rol r ON u.rol_id = r.rol_id
        WHERE u.usuario_usuario = %s """
        
        resultado = db.ejecutar_query(query, (usuario_usuario,))
        
        if resultado and len(resultado) > 0:
            user_data = resultado[0]
            usuario = Usuario(
                usuario_id=user_data['usuario_id'],
                usuario_usuario=user_data['usuario_usuario'],
                usuario_contrasena=user_data['usuario_contrasena'],
                usuario_documento=user_data['usuario_documento'],
                usuario_nombre=user_data['usuario_nombre'],
                usuario_apellido=user_data['usuario_apellido'],
                usuario_estado_id=user_data['usuario_estado_id'],
                rol_id=user_data['rol_id'],
                usuario_curso=user_data['usuario_curso'],
            )
            usuario.rol_nombre = user_data['rol_nombre']
            return usuario
        return None
    
    @staticmethod
    def extraer_usuario():
        db = Database()
        query= """SELECT u.usuario_id, u.usuario_usuario, u.usuario_contrasena, u.usuario_documento,
        u.usuario_nombre, u.usuario_apellido, u.usuario_estado_id, u.rol_id, u.usuario_curso,
        r.rol_nombre as rol_nombre
        FROM usuario u
        INNER JOIN rol r ON u.rol_id = r.rol_id
        ORDER BY u.usuario_id """
        return db.ejecutar_query(query)
    

    @staticmethod
    def usuario_existente(email):

        db = Database()
        query = "SELECT COUNT(*) as count FROM usuario WHERE usuario_usuario = %s"
        resultado = db.ejecutar_query(query, (email,))
        return resultado[0]['count'] > 0 if resultado else False
