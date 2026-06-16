from models.usuario import Usuario
import re

class AuthController:
    
    def login(self, usuario_usuario, password):    
        try:
            
            usuario = Usuario.buscar_por_usuario(usuario_usuario)
            if not usuario:
                return {'success': False, 'message': 'Usuario no encontrado'}
        
            print(f"Debug Login - Usuario: {usuario_usuario}")
            print(f"Debug Login - Contraseña Ingresada: {password}")
            print(f"Debug Login - Contraseña en base de datos: {usuario.usuario_contrasena}")
            print(f"Debug Login - Coincide: {usuario.usuario_contrasena == password}")
            
            if usuario.usuario_contrasena == password:
                return {
                    'success': True,
                    'user': {
                        'usuario_id': usuario.usuario_id,
                        'usuario_usuario': usuario.usuario_usuario,
                        'usuario_nombre': usuario.usuario_nombre,
                        'usuario_apellido': usuario.usuario_apellido,
                        'usuario_estado_id': usuario.usuario_estado_id,
                        'rol_nombre': usuario.rol_nombre,
                        'usuario_curso': usuario.usuario_curso
                    }
                }
            else:
                return {'success': False, 'message': 'Contraseña incorrecta'}
                
        except Exception as e:
            print(f"Error en login: {str(e)}")
            return {'success': False, 'message': f'Error en el sistema: {str(e)}'}

    
    def registro(self, nombres, apellidos, curso, jornada, email, password):

        if len(password) < 8:
            return {'success': False, 'message': 'La contraseña debe tener al menos 6 caracteres'}   
        
        if Usuario.usuario_existente(email):
            return {'success': False, 'message': 'Ya existe un usuario con este email'}
        
        nuevo_usuario = Usuario(
            usuario_nombre=nombres,
            usuario_apellido=apellidos,
            usuario_curso=(curso + jornada),
            usuario_usuario=email,
            usuario_contrasena=password,
            usuario_documento=None,
            usuario_estado_id=1,
            rol_id=2  
        )
        
        
        if nuevo_usuario.guardar():
            return {'success': True, 'message': 'Usuario registrado exitosamente'}
        else:
            return {'success': False, 'message': 'Error al registrar usuario'}
    
