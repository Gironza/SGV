from app.models.usuario import Usuario
 
 
class AuthController:
 
    def login(self, correo, password):
        try:
            usuario = Usuario.buscar_por_correo(correo)
            if not usuario:
                return {'success': False, 'message': 'Usuario no encontrado'}
 
            if usuario.contrasena == password:
                return {
                    'success': True,
                    'user': {
                        'id_usuario': usuario.id_usuario,
                        'correo': usuario.correo,
                        'nombre': usuario.nombre,
                        'apellido': usuario.apellido,
                        'curso': usuario.curso,
                        'id_rol': usuario.id_rol,
                        'rol_nombre': usuario.rol_nombre
                    }
                }
            else:
                return {'success': False, 'message': 'Contraseña incorrecta'}
 
        except Exception as e:
            return {'success': False, 'message': f'Error en el sistema: {str(e)}'}
 
    def registro(self, nombres, apellidos, documento, id_tipo_doc,
                 curso, correo, password, id_institucion):
 
        if len(password) < 8:
            return {'success': False, 'message': 'La contraseña debe tener al menos 8 caracteres'}
 
        if Usuario.usuario_existente(correo):
            return {'success': False, 'message': 'Ya existe un usuario con este correo'}
 
        if Usuario.documento_existente(documento):
            return {'success': False, 'message': 'Ya existe un usuario con este documento'}
 
        nuevo_usuario = Usuario(
            id_institucion=id_institucion,
            documento=documento,
            id_tipo_doc=id_tipo_doc,
            nombre=nombres,
            apellido=apellidos,
            correo=correo,
            contrasena=password,
            curso=curso,
            id_rol=3  
        )
 
        if nuevo_usuario.guardar():
            return {'success': True, 'message': 'Usuario registrado exitosamente'}
        else:
            return {'success': False, 'message': 'Error al registrar usuario'}