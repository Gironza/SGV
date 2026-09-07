import logging
from app.models.usuario import Usuario
from app.models.institucion import Institucion
from app.utils.security import hashear_password, verificar_password
from app.utils.jwt_handler import crear_token

logger = logging.getLogger(__name__)
 
class AuthController:


# LOGIN -----------------
    def login(self, correo, password):
        try:
            usuario = Usuario.buscar_por_correo(correo)
            if not usuario:
                return {'success': False, 'message': 'Usuario no encontrado'}

            if not verificar_password(password, usuario.contrasena):
                return{'success': False, 'message': 'Contraseña Incorrecta'}

            token = crear_token({
                "sub": str(usuario.id_usuario),
                "rol": usuario.id_rol
            })

            return {
                'success': True,
                'access_token': token,
                'token_type': 'bearer',
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
        except Exception as e:
            logger.error(f"Error en registro: {str(e)}")
            return {'success': False, 'message': f'Error en el sistema: {str(e)}'}


#REGISTRO ----------------------
    def registro(self, nombres, apellidos, documento, id_tipo_doc,
                 correo, password, codigo_institucion, curso=None):
        try:
    
            if len(password) < 8:
                return {'success': False, 'message': 'La contraseña debe tener al menos 8 caracteres'}
    
            if Usuario.usuario_existente(correo):
                return {'success': False, 'message': 'Ya existe un usuario con este correo'}
    
            if Usuario.documento_existente(documento):
                return {'success': False, 'message': 'Ya existe un usuario con este documento'}

            institucion_data = Institucion.buscar_por_codigo(codigo_institucion)
            if institucion_data is None:
                return {'success': False, 'message': 'Código de institución inválido'}

            password_hasheado = hashear_password(password)
            nuevo_usuario = Usuario(
                id_institucion=institucion_data['id_institucion'],
                documento=documento,
                id_tipo_doc=id_tipo_doc,
                nombre=nombres,
                apellido=apellidos,
                correo=correo,
                contrasena=password_hasheado,
                curso=curso,
                id_rol=institucion_data['id_rol']
            )
    
            if nuevo_usuario.guardar():
                return {'success': True, 'message': 'Usuario registrado exitosamente'}
            else:
                return {'success': False, 'message': 'Error al registrar usuario'}
        except Exception as e:
            logger.error(f"Error en registro: {str(e)}")
            return {'success': False, 'message': 'Error en el sistema, intenta más tarde'}

