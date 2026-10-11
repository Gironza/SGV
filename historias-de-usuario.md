# Historias de usuario y escenarios — SGV

Cada historia se tomó de su hoja del Excel de requisitos (v0.2). El título y los escenarios están tal como aparecen en esa hoja.

## RF-01 Consultar información general del sistema

Hoja del Excel: `HU01U`

**Historia:** Como Usuario deseo acceder a la informacion general del sistema con la finalidad de conocer el las funcionalidades y beneficios del uso de la plataforma

| # | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
|---|---------------------|-----------------|-------------------------------|
| 1 | el usuario ingresa a la pagina de la plataforma | Ingresar por URL o por busqueda en navegador | El navegador cargara la pagina de inicio de la app |
| 2 | el usuario se desplaza por la pagina principal | Desplazamiento por la pagina | La plataforma brinda informacion relacionada a la app |

## RF-02 Registrar administradores y docentes.

Hoja del Excel: `HU02U`

**Historia:** Como usuario necesito registrarme en la plataforma de SGV con la finalidad de poder acceder al sistema y participar en las elecciones

| # | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
|---|---------------------|-----------------|-------------------------------|
| 1 | el usuario ingrese datos válidos | presione el botón registrarse | debe crear la cuenta exitosamente |
| 2 | intente registrarse | intente registrarse | debe mostrar un mensaje de error |
| 3 | envíe el formulario | envíe el formulario | debe solicitar completar la información |
| 4 | intente continuar | intente continuar | debe pedir una contraseña más segura |

## RF-03 Iniciar sesión

Hoja del Excel: `HU03U`

**Historia:** Como Usuario necesito iniciar sesión en la plataforma con la finalidad de acceder a las funciones del sistema según mi rol

| # | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
|---|---------------------|-----------------|-------------------------------|
| 1 | las credenciales sean correctas | el usuario inicie sesión | debe permitir el acceso |
| 2 | la contraseña sea incorrecta | intente ingresar | debe mostrar mensaje de error |
| 3 | el usuario no exista | intente ingresar | debe informar que no está registrado |
| 4 | el usuario cierre sesión | presione salir | debe finalizar la sesión correctamente |

## RF-04 Recuperar contraseña

Hoja del Excel: `HU04U`

**Historia:** Como Usuario necesito recuperar mi contraseña con la finalidad de volver a ingresar al sistema en caso de olvidarla

| # | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
|---|---------------------|-----------------|-------------------------------|
| 1 | el correo exista | solicite recuperación | debe enviar enlace de recuperación |
| 2 | el correo no exista | intente recuperar contraseña | debe mostrar mensaje de error |
| 3 | la nueva contraseña sea válida | el usuario la confirme | debe actualizarla |
| 4 | el enlace expire | el usuario intente usarlo | debe solicitar una nueva solicitud |

## RF-07 Editar Perfil

Hoja del Excel: `HU05U`

**Historia:** Como Usuario necesito administrar mis datos personales con la finalidad de tener mi perfil actualizado

| # | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
|---|---------------------|-----------------|-------------------------------|
| 1 | el usuario desee visualizar su informacion personal | presione el icono de perfil | debe permitir el acceso a su informacion |
| 2 | seleccione un criterio a modificar | presionar un campo | debe permitir la modificacion de la misma y su actualizacion |
| 3 | intente cambiar su contraseña | Accione el campo de cambio de contraseña | debe realizar un mensaje de confirmacion y posteriormente efectuar su cambio |
| 4 | desea borrar su cuenta | Acciona el icono de borrar cuenta | El sistema elimina su cuenta con previa confirmacion y aceptaciom del admin |

## RF-05 Contactar con Soporte

Hoja del Excel: `HU06U`

**Historia:** Como Usuario necesito establecer contacto con Soporte tecnico con la finalidad de obtener asistencia tecnica a los problemas que puedan ocurrir con el sistema

| # | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
|---|---------------------|-----------------|-------------------------------|
| 1 | el usuario desea solicitar soporte | Accionar el icono de soporte | debe de redireccionarlo a la interfaz de soporte |
| 2 | Para digitar informacion basica y relacionada con el problema | llenar los campos necesarios | El sistema guardar la informacion del formulario |
| 3 | el usuario envia la solicitud | Accionar el boton de enviar | E sistema debe recibir la solicitud |

## RF-06 Unirse a institución con código

Hoja del Excel: `HU07U`

**Historia:** Como Usuario Necesito vincularme a una institucion Con el fin de ejercer mi rol dentro del sistema

| # | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
|---|---------------------|-----------------|-------------------------------|
| 1 | el usuario ingrese un codigo de la institucion | presiona el boton "vincularse a una institucion" | debe verificar y validar el codigo y dar el posterior acceso |
| 2 | Mediante un enlace de invitacion | presione el enlace | previamente loggeado informa y confirma el ingreso |

## RF-06 Unirse a institución con código

Hoja del Excel: `HU08U`

**Historia:** Como Usuario Necesito vincularme a una institucion Con el fin de ejercer mi rol dentro del sistema

| # | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
|---|---------------------|-----------------|-------------------------------|
| 1 | Usuario autenticado con sesión activa en la plataforma | Presionar el ícono de usuario y seleccionar 'Cerrar sesión' | Sesión finalizada y redirigido a la pantalla de inicio de sesión |
| 2 | Opción de cerrar sesión seleccionada | Confirmar la acción en el diálogo de confirmación que aparece | Sesión cerrada correctamente tras confirmar; datos de sesión eliminados del dispositivo |
| 3 | Diálogo de confirmación de cierre de sesión visible | Presionar 'Cancelar' en el diálogo | Diálogo cerrado y sesión activa sin cambios, permaneciendo en la misma pantalla |
| 4 | Usuario en sesión activa desde un dispositivo móvil | Presionar el ícono de usuario y seleccionar 'Cerrar sesión' | Sesión cerrada y redirigido al login; token de sesión invalidado correctamente |

## RF-10 Gestionar Usuarios

Hoja del Excel: `HU09A`

**Historia:** Como Administrador necesito gestionar los datos de los usuarios vinculados a la plataforma con el fin de ejercer una administracion de los usuarios dentro de la institucion

| # | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
|---|---------------------|-----------------|-------------------------------|
| 1 | accede al módulo de gestión de usuarios | selecciona la opción 'Ver usuarios' | mostrar la lista de todos los usuarios vinculados a la institución con sus roles |
| 2 | visualiza un usuario existente en el sistema | selecciona 'Editar' sobre el usuario y modifica sus datos | actualizar la información del usuario y muestra confirmación del cambio |
| 3 | identifica un usuario que debe ser removido de la plataforma | selecciona 'Eliminar' sobre el usuario y confirma la acción | eliminar al usuario, revoca su acceso y notifica la operación exitosa |
| 4 | necesita encontrar un usuario específico entre muchos registros | ingresa el nombre o selecciona un filtro por rol en el buscador | filtrar y mostrar únicamente los usuarios que coinciden con el criterio ingresado |

## RF-18 Gestionar codigos de Invitacion

Hoja del Excel: `HU10A`

**Historia:** Como Administrador necesito generar codigos y enlaces de invitacion a la institucion de acuerdo con sus roles con el fin de que los usuarios ingresen a la institucion de acuerdo con su rol especifico

| # | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
|---|---------------------|-----------------|-------------------------------|
| 1 | accede al módulo de generación de códigos y selecciona el rol 'Votante' | selecciona el curso e indica generar código | generar un código de 6 dígitos único asociado al curso |
| 2 | necesita vincular a un docente a la institución | selecciona el rol 'Docente' e indica generar código para esa persona | generar un código de 6 dígitos único e individual para que el docente ingrese con su rol específico |
| 3 | necesita agregar otro administrador a la plataforma | selecciona el rol 'Administrador' e indica generar código | genera un código de 6 dígitos único para ese administrador, garantizando acceso con privilegios completos |
| 4 | El administrador ha generado uno o varios códigos de invitación | accede al listado de códigos activos y selecciona 'Copiar' en el deseado | mostrar todos los códigos vigentes con su rol asociado y permite copiarlos o compartirlos fácilmente |

## RF-11 Gestionar docentes

Hoja del Excel: `HU11A`

**Historia:** Como Administrador necesito gestionar la informacion del Personal Docente con el fin de asegurar los permisos y accesos de modificacion dentro de la plataforma

| # | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
|---|---------------------|-----------------|-------------------------------|
| 1 | accede al perfil de un docente registrado en la plataforma | selecciona los permisos que desea habilitar (ej: gestionar votaciones, ver resultados) | guarda la configuración y el docente obtiene acceso a las funciones asignadas |
| 2 | detecta que un docente ya no debe tener ciertos privilegios de moderación | desmarca los permisos correspondientes y confirma el cambio | actualiza el perfil del docente y restringe las funciones revocadas de forma inmediata |
| 3 | corregir o actualizar datos del perfil de un docente | selecciona 'Editar' en el perfil del docente y modifica los campos necesarios | actualiza los datos del docente y confirma los cambios realizados |
| 4 | remover a un docente que ya no pertenece a la institución | selecciona la opción 'Eliminar' en el perfil del docente y confirma la acción | elimina al docente, revoca todos sus permisos y accesos |

## RF-12 Gestionar Elecciones

Hoja del Excel: `HU12A`

**Historia:** Como Administrador necesito crear y configurar elecciones con la finalidad de administrar los procesos electorales del sistema

| # | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
|---|---------------------|-----------------|-------------------------------|
| 1 | los datos sean válidos | el administrador guarde la información | debe guardar la información |
| 2 | la fecha final sea menor a la inicial | intente guardar | debe mostrar error |
| 3 | la elección esté activa | los usuarios ingresen | debe permitir votaciones |
| 4 | la elección finalice | llegue la fecha límite | debe cerrar las votaciones automáticamente |

## RF-13 Ver estadísticas de las Elecciones.

Hoja del Excel: `HU13A`

**Historia:** Como Administrador necesito consultar los resultados de las elecciones con la finalidad de conocer el número de votos obtenidos por cada candidato

| # | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
|---|---------------------|-----------------|-------------------------------|
| 1 | la votación haya finalizado | el administrador consulte resultados | debe mostrar el conteo de votos |
| 2 | existan empates | se visualicen los resultados | debe indicarlo claramente |
| 3 | no existan votos | se consulte el reporte | debe mostrar valores en cero |
| 4 | el administrador exporte resultados | presione descargar | debe generar el archivo correctamente |

## RF-14 Exportar resultados (administrador)

Hoja del Excel: `HU14A`

**Historia:** Como Administrador necesito Exportar los resultados de las elecciones con la finalidad de descargar y generar consolidados de las elecciones

| # | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
|---|---------------------|-----------------|-------------------------------|
| 1 | El admin desea resultados en formato Excel | Selecciona formato Excel y presiona "Descargar" | Se descarga archivo .xlsx con todos los datos |
| 2 | Se requiere formato PDF para acta oficial | Selecciona PDF y presiona "Exportar" | Se genera PDF con formato profesional y datos completos |
| 3 | Se necesita certeza de los resultados | Marca opción "Incluir certificados" | El documento incluye códigos de verificación de votos |
| 4 | El admin desea customizar el reporte | Marca/desmarca datos (nombres, votos, porcentajes) | El reporte incluye solo los datos seleccionados |

## RF-16 Enviar notificaciones (administrador)

Hoja del Excel: `HU15A`

**Historia:** Como Administrador enviar notificaciones acerca de las elecciones, estados, y observaciones a los usuarios de la plataforma con la finalidad de informar y dar aviso sobre asuntos importantes de la eleccion y del sistema

**Estado:** Pendiente

| # | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
|---|---------------------|-----------------|-------------------------------|
| 1 | El admin debe notificar sobre una elección | Redacta mensaje y selecciona "Enviar a todos" | Todos los usuarios reciben la notificación por correo y en el sistema |
| 2 | Solo docentes deben recibir una notificación | Selecciona rol "Docente" y envía | Solo los docentes reciben la notificación |
| 3 | Desea que se envíe en fecha específica | Selecciona fecha/hora y presiona "Programar" | La notificación se envía automáticamente en la fecha indicada |
| 4 | Necesita revisar qué se comunicó | Accede a "Historial de notificaciones" | Ve registro completo de todas las notificaciones enviadas |

## RF-17 Gestionar candidatos (administrador)

Hoja del Excel: `HU16A`

**Historia:** Como Administrador necesito Gestionar los candidatos en el sistema con la finalidad de habilitar su participación en las elecciones

| # | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
|---|---------------------|-----------------|-------------------------------|
| 1 | los datos sean válidos | el administrador guarde la información | debe registrar el candidato |
| 2 | falte información obligatoria | intente registrar | debe solicitar completar los campos |
| 3 | el candidato ya exista | intente registrarlo nuevamente | debe impedir el registro duplicado |
| 4 | se cargue una foto válida | se guarde el formulario | debe almacenar la imagen correctamente |

## RF-15 Configurar parámetros del sistema.

Hoja del Excel: `HU17A`

**Historia:** Como Administrador quiero personalizar el Panel de mi organizacion (aspecto, detalles, informacion)

| # | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
|---|---------------------|-----------------|-------------------------------|
| 1 | accede a la sección de personalización del panel de su organización | sube una imagen como logo oficial de la institución | almacena el logo y lo muestra en el encabezado del panel y en las pantallas de votación |
| 2 | Al ingresar a personalización visual | selecciona los colores primario y secundario de la institución mediante un selector de color | aplica la paleta de colores elegida en toda la interfaz del panel de la organización |
| 3 | deseo enriquecer visualmente la pantalla de inicio del panel | sube una o más imágenes de banner y define su posición en el panel | despliega las imágenes cargadas en la sección correspondiente del panel institucional |
| 4 | Necesita reflejar datos actualizados de la institución en el panel | edita campos como nombre de la institución, descripción y datos de contacto, luego guarda | actualiza la información y la muestra correctamente en el panel público e interno |

## RF-12 Cargar estudiantes masivamente

Hoja del Excel: `HU18A`

**Historia:** Como Administrador deseo cargar masivamente estudiantes mediante un archivo Excel o CSV con la finalidad de registrar a los estudiantes de la institución de forma rápida, sin tener que crearlos uno por uno

| # | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
|---|---------------------|-----------------|-------------------------------|
| 1 | El administrador se encuentra en el módulo de gestión de estudiantes | Selecciona la opción “Cargar estudiantes masivamente” | El sistema muestra la pantalla de carga con las instrucciones, los formatos permitidos (Excel/CSV) y la opción de descargar una plantilla de ejemplo |
| 2 | El administrador está en la pantalla de carga masiva | Selecciona un archivo Excel o CSV con la estructura correcta y presiona “Cargar” | El sistema recibe el archivo y comienza la validación del formato y de los datos de cada fila |
| 3 | El administrador está en la pantalla de carga masiva | Intenta subir un archivo que no es Excel ni CSV (por ejemplo PDF o imagen) | El sistema rechaza el archivo y muestra un mensaje indicando que solo se aceptan los formatos .xlsx, .xls y .csv |
| 4 | El administrador sube un archivo al que le faltan columnas obligatorias (nombres, documento, curso, etc.) | Presiona “Cargar” | El sistema cancela la carga e indica cuáles columnas obligatorias no se encontraron, sin registrar ningún estudiante |

## RF-23 Gestionar Candidaturas (docente)

Hoja del Excel: `HU19D`

**Historia:** Como Docente quiero administrar los candidatos registrados, asi como su informacion especifica con el fin de auditar y administrar el procesos electoral de la intitucion

| # | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
|---|---------------------|-----------------|-------------------------------|
| 1 | Accede al módulo de gestión de candidatos dentro del proceso electoral activo | completa el formulario con los datos del candidato (nombre, curso, propuesta, foto) y confirma | registra al candidato, lo hace visible en la lista y lo habilita para recibir votos |
| 2 | Detecta un error o cambio en los datos de un candidato ya registrado | selecciona el candidato, modifica los campos necesarios y guarda los cambios | actualiza la información del candidato y refleja los cambios de forma inmediata en la plataforma |
| 3 | El docente necesita retirar a un candidato que no cumple los requisitos del proceso electoral | selecciona la opción 'Eliminar' sobre el candidato y confirma la acción | elimina al candidato del proceso, remueve su perfil de la votación y registra la operación |
| 4 | Al revisar el estado y la información de todos los candidatos inscritos | accede al listado de candidatos y aplica filtros por curso, estado o nombre si lo necesita | muestra la lista actualizada de candidatos con su información y estado dentro del proceso |

## RF-21 Ver Resultados (docente)

Hoja del Excel: `HU20D`

**Historia:** Como Docente necesito visualizar los resultados y obtener certificados y consolidados

| # | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
|---|---------------------|-----------------|-------------------------------|
| 1 | accede al módulo de resultados durante una votación en curso | selecciona la opción 'Ver resultados en tiempo real' | muestra un dashboard actualizado con los votos acumulados por candidato en tiempo real |
| 2 | La votación ha finalizado y el docente necesita un informe oficial del proceso | selecciona 'Exportar consolidado' y elige el formato PDF | generar y descargar un archivo PDF con las estadísticas completas, totales y resultados finales |
| 3 | necesita analizar o archivar los datos de la votación en una hoja de cálculo | selecciona 'Exportar consolidado' y elige el formato Excel (.xlsx) | genera y descarga un archivo Excel con todos los datos estadísticos del proceso electoral |
| 4 | El proceso electoral ha concluido y la institución requiere un documento certificado | selecciona la opción 'Generar certificado' al finalizar la votación | genera un certificado descargable con los resultados oficiales, fecha, institución y firma digital del proceso |

## RF-023 Gestionar estudiantes votantes

Hoja del Excel: `HU21D`

**Historia:** Como docente quiero gestionar a los estudiantes con respecto a sus cursos inscritos

| # | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
|---|---------------------|-----------------|-------------------------------|
| 1 | Panel de gestión de estudiantes con la lista cargada | Seleccionar un estudiante y elegir el nuevo curso en el desplegable disponible | Registro actualizado con el nuevo curso asignado y cambio reflejado en la lista |
| 2 | Estudiante activo visible en el listado del docente | Seleccionar el estudiante y activar la opción 'Inhabilitar' | Estudiante marcado como inactivo, impedido de votar hasta ser habilitado nuevamente |
| 3 | Perfil de estudiante abierto en el panel de gestión | Seleccionar el campo de observaciones, ingresar el texto y guardar | Observación almacenada y visible en el perfil del estudiante para consulta posterior |
| 4 | Módulo de gestión con múltiples cursos disponibles | Seleccionar un curso en el filtro para ver solo sus estudiantes inscritos | Lista filtrada mostrando únicamente los estudiantes del curso seleccionado |

## RF-19 Gestionar Votaciones (docente)

Hoja del Excel: `HU22D`

**Historia:** Como docente quiero editar y administrar las votaciones creadas de la institucion

| # | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
|---|---------------------|-----------------|-------------------------------|
| 1 | El docente completa el formulario con datos válidos | Presiona "Crear elección" | Se crea la elección y aparece en el listado |
| 2 | El docente asigna fechas a la elección | Selecciona fecha y hora de inicio/cierre | Las fechas se guardan y el sistema respeta los límites |
| 3 | El docente desea modificar datos de la elección | Abre elección existente y modifica campos | Los cambios se guardan correctamente |
| 4 | El admin desea eliminar una elección | Presiona "Eliminar" y confirma la acción | La elección se elimina después de confirmación |

## RF-020 Ver Votaciones activas (docente)

Hoja del Excel: `HU23D`

**Historia:** Como docente Deseo ver las votaciones activas

| # | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
|---|---------------------|-----------------|-------------------------------|
| 1 | El Docente accede al sistema | Ingresa a su dashboard | Ve listado de elecciones activas en las que puede administrar |
| 2 | Visualizar tarjetones | Selecciona una votación y ve candidatos | Se muestran candidatos, fotos y propuestas de forma clara |

## RF-024 Exportar Resultados (docente

Hoja del Excel: `HU24D`

**Historia:** Como docente Necesito Exportar los resultados de las elecciones

| # | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
|---|---------------------|-----------------|-------------------------------|
| 1 | El admin desea resultados en formato Excel | Selecciona formato Excel y presiona "Descargar" | Se descarga archivo .xlsx con todos los datos |
| 2 | Se requiere formato PDF para acta oficial | Selecciona PDF y presiona "Exportar" | Se genera PDF con formato profesional y datos completos |
| 3 | Se necesita certeza de los resultados | Marca opción "Incluir certificados" | El documento incluye códigos de verificación de votos |
| 4 | El admin desea customizar el reporte | Marca/desmarca datos (nombres, votos, porcentajes) | El reporte incluye solo los datos seleccionados |

## RF-025 Exportar resultados (docente)

Hoja del Excel: `HU25D`

**Historia:** Como docente Enviar y Recibir notificaciones acerca de las elecciones y observaciones a los usuarios de la plataforma

| # | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
|---|---------------------|-----------------|-------------------------------|
| 1 | Debe comunicar sobre una votación | Redacta mensaje y presiona "Enviar" | Todos los estudiantes del curso reciben la notificación |
| 2 | El admin envía una circular | El sistema recibe la notificación | Se muestra en la bandeja de notificaciones del docente |
| 3 | Necesita revisar lo enviado | Accede a historial | Ve registro de todas las notificaciones enviadas y recibidas |
| 4 | Leer una notificación recibida | Abre y lee la notificación | Se marca como leída automáticamente |

## RF-032 Ver información y propuestas de candidatos

Hoja del Excel: `HU26-E`

**Historia:** Como Estudiante Necesito visualizar la información de los candidatos

| # | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
|---|---------------------|-----------------|-------------------------------|
| 1 | existan candidatos registrados | el usuario ingrese al módulo | debe mostrar la lista de candidatos |
| 2 | el usuario seleccione un candidato | abra el perfil | debe mostrar información detallada |
| 3 | no existan candidatos | ingrese al módulo | debe mostrar un mensaje informativo |
| 4 | la información sea actualizada | el usuario consulte nuevamente | debe reflejar los cambios |

## RF-027 Participar en votaciones

Hoja del Excel: `HU27-E`

**Historia:** Como Estudiante Necesito realizar mi voto de manera digital

| # | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
|---|---------------------|-----------------|-------------------------------|
| 1 | el usuario seleccione un candidato | confirme su voto | debe registrar el voto correctamente |
| 2 | el usuario ya haya votado | intente votar nuevamente | debe impedir un segundo voto |
| 3 | el voto sea exitoso | finalice el proceso | debe mostrar mensaje de confirmación |
| 4 | envíe el voto | envíe el voto | debe informar el problema |

## RF-028 Participar en votaciones

Hoja del Excel: `HU28-E`

**Historia:** Como Estudiante Necesito Obtener mi certificado Electoral

| # | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
|---|---------------------|-----------------|-------------------------------|
| 1 | Mensaje de confirmación 'Su votación fue enviada exitosamente' visible en pantalla | Presionar el botón 'Imprimir certificado electoral' | Generado y descargado un PDF con el comprobante oficial de participación electoral |
| 2 | Confirmación de voto exitosa en pantalla | Seleccionar la opción de vista previa antes de descargar | Desplegada una previsualización del certificado con los datos del votante y la elección |
| 3 | PDF del certificado descargado exitosamente | Abrir el archivo generado y revisar los datos | Certificado muestra nombre, fecha, institución y nombre de la elección sin errores |
| 4 | Mensaje de voto exitoso con botón de certificado visible | Cerrar la pantalla sin presionar el botón de imprimir | Sesión continúa normalmente sin generar el certificado; opción disponible desde el historial |

## RF-031 Ver historial de participación

Hoja del Excel: `HU-29E`

**Historia:** Como Estudiante Necesito acceder a mi historias de Elecciones realizadas

| # | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
|---|---------------------|-----------------|-------------------------------|
| 1 | Usuario autenticado en la plataforma con elecciones previas registradas | Navegar a la sección 'Historial de elecciones' desde el menú | Listado de todas las elecciones anteriores en las que se participó, con fecha y nombre |
| 2 | Historial de elecciones cargado en pantalla | Seleccionar una elección del listado para ver su detalle | Vista detallada con los candidatos, resultados y datos del proceso electoral seleccionado |
| 3 | Detalle de una elección pasada abierto | Presionar 'Imprimir certificado electoral' de esa elección | PDF del certificado de participación de esa elección generado y descargado correctamente |
| 4 | Usuario sin elecciones previas registradas accede al historial | Ingresar a la sección de historial de elecciones | Mensaje indicando que aún no se ha participado en ninguna elección |

## RF-026 Ver votaciones disponibles

Hoja del Excel: `HU-30E`

**Historia:** Como Estudiante Necesito ver las Elecciones disponibles en mi institucion

| # | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
|---|---------------------|-----------------|-------------------------------|
| 1 | El estudiante accede al sistema | Ingresa a su dashboard | Ve listado de elecciones activas en las que puede votar |
| 2 | Antes de emitir voto | Selecciona una votación y ve candidatos | Se muestran candidatos, fotos y propuestas de forma clara |
| 3 | Selecciona un candidato | Presiona "Votar" y confirma | El voto se registra de forma segura y anónima |
| 4 | El estudiante revisa su selección | Ve resumen de su voto | Muestra confirmación visual antes de enviar |

## RF-030 Recibir notificaciones (estudiante)

Hoja del Excel: `HU30E`

**Historia:** Como Estudiante Necesito ver Resultados de las Elecciones (cuando finalicen)

| # | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
|---|---------------------|-----------------|-------------------------------|
| 1 | La elección ha cerrado | Accede a sección de resultados | Ve gráficos con resultados y porcentajes |
| 2 | Hay múltiples cargos en la elección | Selecciona un cargo | Muestra ganador/ganadora del cargo con mayor de votos |
| 3 | Quiere saber cantidad de votantes | Accede a estadísticas | Muestra total de votos, abstenciones y porcentaje de participación |
| 4 | El admin aún no ha publicado resultados | Intenta ver resultados antes del cierre | Muestra mensaje "Resultados no disponibles aún" |

## RF-031 Ver historial de participación

Hoja del Excel: `HU31E`

**Historia:** Como Estudiante Quiero Recibir notificaciones del Sistema, Administrador o Docente

| # | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
|---|---------------------|-----------------|-------------------------------|
| 1 | Una votación es abierta | Sistema notifica automáticamente | Recibe alerta en el sistema y por correo |
| 2 | Falta poco para cerrar | A 1 hora del cierre | Recibe notificación de urgencia |
| 3 | Los resultados están listos | Admin publica resultados | Recibe notificación con enlace a resultados |
| 4 | Quiere personalizar avisos | Accede a configuración | Puede elegir qué notificaciones recibir |

## RF-032 Ver información y propuestas de candidatos

Hoja del Excel: `HU32E`

**Historia:** Como Estudiante Necesito Registrarme en un curso

| # | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
|---|---------------------|-----------------|-------------------------------|
| 1 | El docente proporciona código | Ingresa código y presiona "Registrarse" | Se añade al curso y puede participar en sus votaciones |
| 2 | Código no es válido | Intenta con código incorrecto | Sistema muestra error "Código inválido" |
| 3 | Ya está en el curso | Intenta registrarse de nuevo | Muestra "Ya está registrado en este curso" |
| 4 | Quiere revisar en qué está | Accede a "Mis cursos" | Muestra lista de todos los cursos en que está matriculado |

## RF-033 Registrar candidatura

Hoja del Excel: `HU33C`

**Historia:** Como Candidato Deseo postularme mi candidatura a una eleccion proxima

| # | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
|---|---------------------|-----------------|-------------------------------|
| 1 | Hay convocatoria abierta | Completa formulario y presiona "Postularme" | Su candidatura queda registrada en estado pendiente |
| 2 | Hay múltiples cargos disponibles | Elige cargo (personero, contralor, etc.) | Se asigna el cargo seleccionado a su candidatura |
| 3 | Se piden requisitos | Sube archivos solicitados | La documentación se adjunta a su candidatura |
| 4 | Sistema verifica cumplimiento | Sistema evalúa automáticamente | Se indica si cumple o le falta documentación |

## RF-034 Editar perfil de candidatura

Hoja del Excel: `HU34C`

**Historia:** Como Candidato Necestio Editar mi perfil de Candidatura

| # | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
|---|---------------------|-----------------|-------------------------------|
| 1 | El candidato necesita cambiar datos | Presiona "Editar perfil" y modifica | Los cambios se guardan correctamente |
| 2 | Desea incluir imagen de campaña | Carga imagen y presiona "Guardar" | La imagen se guarda y se muestra en su perfil |
| 3 | Quiere mejorar sus propuestas | Accede a sección de propuestas y edita | Las propuestas se actualizan (si aún está en plazo) |
| 4 | Pasó la fecha límite | Intenta editar después de cerrada la convocatoria | Sistema muestra "Plazo de edición cerrado" |

## RF-035 Retirar candidatura

Hoja del Excel: `HU35C`

**Historia:** Como Candidato Deseo Retirarme de mi candidatura

| # | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
|---|---------------------|-----------------|-------------------------------|
| 1 | Desiste de participar | Presiona "Retirarme" y confirma | Su candidatura se cancela y se notifica al admin |
| 2 | Debe confirmar la acción | Confirma retiro en diálogo | El retiro es irreversible, candidatura eliminada |
| 3 | Pasó la fecha de retiro | Intenta retirarse después del cierre | Sistema muestra "No se puede retirar a esta hora" |
| 4 | Admin y docentes deben saber | Se procesa el retiro | Se notifica automáticamente a admin y docentes |

## RF-036 Ver estado de candidatura

Hoja del Excel: `HU36C`

**Historia:** Como Candidato Deseo vizualizar el estado de mi candidatura

| # | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
|---|---------------------|-----------------|-------------------------------|
| 1 | Acaba de postularse | Accede a su perfil de candidato | Muestra estado "Pendiente de revisión" |
| 2 | El admin aprobó | Accede a su perfil | Muestra estado "Aprobado" en color verde |
| 3 | El admin rechazó | Accede a su perfil | Muestra estado "Rechazado" con motivo del rechazo |
| 4 | Quiere ver cambios | Ve sección de historial | Muestra registro de cambios de estado con fechas |

## RF-037 Recibir notificaciones (candidato)

Hoja del Excel: `HU37C`

**Historia:** Como Candidato Quiero Recibir notificaciones del Sistema, Administrador o Docente

| # | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
|---|---------------------|-----------------|-------------------------------|
| 1 | Su candidatura fue aprobada | Sistema envía notificación | Recibe aviso de aprobación por correo y en el sistema |
| 2 | Su candidatura fue rechazada | Sistema envía notificación | Recibe aviso con motivo del rechazo |
| 3 | Admin cambió fechas o datos | Sistema notifica | Recibe alerta de cambios importantes |
| 4 | Quiere personalizar | Accede a configuración | Puede elegir qué notificaciones recibir |

## RF-038 Consultar resultados (candidato)

Hoja del Excel: `HU38C`

**Historia:** Como Candidato Necesito ver Resultados de las Elecciones (cuando finalicen)

| # | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
|---|---------------------|-----------------|-------------------------------|
| 1 | La votación finalizó | Accede a "Ver resultados" | Muestra votos obtenidos y posición en el ranking |
| 2 | Quiere conocer el total | Consulta sus resultados | Muestra número exacto de votos recibidos |
| 3 | Analiza representatividad | Ve estadísticas | Muestra % de votos respecto al total de votantes |
| 4 | Análisis competitivo | Ve ranking completo | Muestra posición y votos de todos los candidatos |

## RF-039 Ver calendario electoral

Hoja del Excel: `HU39C`

**Historia:** Como Candidato necesito Vizualizar mi Calendario electoral

| # | Dado que (contexto) | Cuando (evento) | Entonces (resultado esperado) |
|---|---------------------|-----------------|-------------------------------|
| 1 | El candidato accede | Selecciona "Ver calendario electoral" | Muestra calendario con todas las fechas importantes |
| 2 | Solo elecciones en que participa | Filtra "Mis elecciones" | Muestra solo fechas de sus candidaturas |
| 3 | No olvide fechas importantes | Sistema envía recordatorios | Recibe notificaciones antes de fechas clave |
| 4 | Quiere tener en su dispositivo | Presiona "Descargar calendario" | Se descarga archivo .ics compatible con calendarios |
