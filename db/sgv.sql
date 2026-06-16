CREATE DATABASE SGV;
USE SGV;

CREATE TABLE institucion(
    id_institucion SERIAL PRIMARY KEY,
    nombre varchar(256) NOT NULL,
    NIT varchar(15) UNIQUE,
    direccion varchar(50) NOT NULL,
    telefono varchar(15),
    correo varchar(256), 
    descripcion text 
);

INSERT INTO institucion (nombre, NIT, direccion, telefono, correo, descripcion) VALUES 
('Colegio Feliz', 0000000, 'Cll de la Felicidad', 00000, null, null),
('SENA', 0000001, 'Cll 52', 00000, null, 'Servicio Nacional de Aprendizaje');

CREATE TABLE estado_eleccion (
    id_estado_eleccion INT PRIMARY KEY,
    nombre varchar(35)
);

INSERT INTO estado_eleccion (id_estado_eleccion, nombre) VALUES
(01, 'Activa'),
(02, 'Finalizada'),
(03, 'Pendiente');


CREATE TABLE roles (
    id_rol INT PRIMARY KEY,
    nombre VARCHAR(30) NOT NULL,
    descripcion VARCHAR(256)
);

INSERT INTO roles (id_rol, nombre, descripcion) VALUES
(1, 'Administrador', 'Control total del sistema de votación'),
(2, 'Docente', 'Usuario con permisos de visualización y jurado de votación'),
(3, 'Estudiante', 'Usuario habilitado para ejercer el derecho al voto');


CREATE TABLE tipo_documento(
    id_tipo_doc INT PRIMARY KEY,
    nombre VARCHAR(35) NOT NULL,
    descripcion VARCHAR(256)
);

INSERT INTO tipo_documento (id_tipo_doc, nombre, descripcion) VALUES 
(1, 'CC', 'Cédula de Ciudadanía'),
(2, 'TI', 'Tarjeta de Identidad'),
(3, 'CE', 'Cédula de Extranjería'),
(4, 'PPT', 'Permiso por Protección Temporal');


CREATE TABLE usuarios (
    id_usuario SERIAL PRIMARY KEY,
    id_institucion INT NOT NULL,
    documento VARCHAR(20) UNIQUE NOT NULL,
    id_tipo_doc INT NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    correo VARCHAR(100) UNIQUE NOT NULL,
    contrasena VARCHAR(255) NOT NULL,
    curso VARCHAR(20),
    id_rol INT NOT NULL,
    FOREIGN KEY (id_institucion) REFERENCES institucion(id_institucion),
    FOREIGN KEY (id_rol) REFERENCES roles(id_rol),
    FOREIGN KEY (id_tipo_doc) REFERENCES tipo_documento(id_tipo_doc)
);


INSERT INTO usuarios (documento, id_institucion, id_tipo_doc, nombre, apellido, correo, contrasena, curso, id_rol) VALUES
('1000111222', 1, 1, 'Santiago', 'Peña', 'admin@colegio.edu.co', 'admin_123', NULL, 1), 
('79888999', 2, 1, 'Alberto', 'Gómez', 'alberto.gomez@colegio.edu.co', '0000', NULL, 1),  
('52333444', 1,1, 'Alejandra', 'Pinzón', 'aleja.pinzon@colegio.edu.co', '0000', NULL, 2),   
('1010444555', 2,1, 'Camilo', 'Sanz', 'camilo.sanz@colegio.edu.co', '0000', NULL, 2),     
('1020304050', 1,2, 'Daniela', 'Rojas', 'daniela.rojas@colegio.edu.co', '0000', '1101', 3), 
('1020304051', 1,2, 'Esteban', 'Quito', 'esteban.quito@colegio.edu.co', '0000', '1101', 3), 
('1020304052', 1,2, 'Fabián', 'Niño', 'fabian.nino@colegio.edu.co', '0000', '1102', 3),  
('1020304053', 1,3, 'Gabriela', 'Mistral', 'gabriela.mistral@colegio.edu.co', '00000', '1102', 3), 
('1020304054', 1,2, 'Hugo', 'Sánchez', 'hugo.sanchez@colegio.edu.co', '00000', '1001', 3),  
('1020304055', 2,4, 'Isabela', 'Santo', 'isabela.santo@colegio.edu.co', '0000', '1001', 3),  
('1020304056', 2,2, 'Juan', 'Valdez', 'juan.valdez@colegio.edu.co', '0000', '1002', 3),    
('1020304057', 2,1, 'Kevin', 'Flórez', 'kevin.florez@colegio.edu.co', '0000', '1002', 3);   


CREATE TABLE elecciones (
    id_eleccion SERIAL PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    descripcion TEXT,
    fecha_inicio TIMESTAMP NOT NULL,
    fecha_fin TIMESTAMP NOT NULL,
    id_estado_eleccion INT DEFAULT 01 NOT NULL,
    id_institucion INT NOT NULL,
    FOREIGN KEY (id_institucion) REFERENCES institucion(id_institucion)
);

INSERT INTO elecciones (titulo, descripcion, fecha_inicio, fecha_fin, id_estado_eleccion, id_institucion) VALUES
('Contralor', 'Elección del Contralor Estudiantil para el periodo vigente', '2026-03-01 08:00:00', '2026-03-01 16:00:00', '01', '01'), 
('Cabildante', 'Elección del Cabildante Estudiantil ante la localidad', '2026-03-01 08:00:00', '2026-03-01 16:00:00', '01', '01'),
('Personero', 'Elección del Personero Estudiantil del colegio', '2026-03-01 08:00:00', '2026-03-01 16:00:00', '02', '01');   


CREATE TABLE candidatos (
    id_candidato SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    propuesta TEXT,
    foto VARCHAR(255),
    id_eleccion INT NOT NULL,
    FOREIGN KEY (id_eleccion) REFERENCES elecciones(id_eleccion) ON DELETE CASCADE
);

INSERT INTO candidatos (nombre, apellido, propuesta, foto, id_eleccion) VALUES
('Andrés', 'Perez', 'N/A.', 'candidato1.jpg', 1),        
('Blanca', 'aurora', 'Transparencia total...', 'candidato2.jpg', 1),
('César', 'alonso', 'Auditoría mensual...', 'candidato3.jpg', 1),   
('Johan', 'Garcia', 'N/A.', 'candidato4.jpg', 1),         
('Laura', 'Gomez', 'Poner piscina en el colegio', 'blanco.jpg', 1),
('Fernando', 'Fernandez', 'N/A.', 'candidato5.jpg', 2),   
('Gloria', 'Valencia', 'Gestionar mejoras...', 'candidato6.jpg', 2),
('Hernán', 'Peláez', 'N/A', 'candidato7.jpg', 2),        
('Jaime', 'Duque', 'N/A.', 'candidato8.jpg', 2),          
('Jorge', 'Barón', 'Ennnnntusiaaasmo.', 'blanco.jpg', 2),  
('Armando', 'Casas', 'N/A.', 'candidato9.jpg', 3),   
('Felipe', 'Díaz', 'Torneos de fútbol', 'candidato10.jpg', 3),   
('María', 'Cano', 'Defensa de los derechos', 'candidato11.jpg', 3),
('Santiago', 'Mateus', 'N/A.', 'candidato12.jpg', 3),     
('Hernesto', 'hernandez', 'N/A', 'blanco.jpg', 3);       


CREATE TABLE votos (
    id_voto SERIAL PRIMARY KEY,
    id_usuario INT NOT NULL,
    id_eleccion INT NOT NULL,
    id_candidato INT NOT NULL,
    fecha_voto TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_eleccion) REFERENCES elecciones(id_eleccion),
    FOREIGN KEY (id_candidato) REFERENCES candidatos(id_candidato),
    UNIQUE (id_usuario, id_eleccion)
);

INSERT INTO votos (id_usuario, id_eleccion, id_candidato) VALUES
(5, 1, 1), (5, 2, 6), (5, 3, 11),
(6, 1, 2), (6, 2, 7), (6, 3, 12),
(7, 1, 3), (7, 2, 5), (7, 3, 13),
(8, 1, 4), (8, 2, 9), (8, 3, 14),
(9, 1, 5), (9, 2, 10), (9, 3, 5),
(10, 1, 1), (10, 2, 7), (10, 3, 13),
(11, 1, 5), (11, 2, 6), (11, 3, 11),
(12, 1, 2), (12, 2, 9), (12, 3, 14);

--SELECTS 
select * from estado_eleccion;
select * from roles; 

--Mostrar infromacion de los usuarios con su rol 
SELECT 
    u.id_usuario,
    i.nombre AS institucion, ---Es Opcional ver la institucion, ya que el Administrador solo manejara una institucion, en discucion
    td.nombre AS tipo_documento, 
    u.documento,
    u.nombre,
    u.apellido,
    u.correo,
    u.curso,
    r.nombre AS rol_sistema       
FROM 
    usuarios AS u 
INNER JOIN 
    tipo_documento AS td ON u.id_tipo_doc = td.id_tipo_doc
INNER JOIN 
    roles AS r ON u.id_rol = r.id_rol
INNER JOIN 
    institucion AS i ON u.id_institucion = i.id_institucion
WHERE 
    u.id_institucion = 1 ------> Se Puede filtrar de acuerdo al colegio en el que este 
ORDER BY
    u.id_usuario ASC;

---Mostrar las elecciones de acuerdo con su estado
SELECT
    e.id_eleccion,
    e.titulo,
    e.fecha_inicio,
    e.fecha_fin,
    es.nombre AS estado
FROM 
    elecciones AS e 
INNER JOIN
    estado_eleccion AS es ON e.id_estado_eleccion = es.id_estado_eleccion
WHERE 
    e.id_institucion = 1 ------> Filtro de Institucion 
ORDER BY 
    e.id_eleccion ASC;


---Mostrar la informacion de las candidatos y el numero de votos efectuados 
SELECT 
    c.id_candidato, 
    c.nombre,
    c.apellido,
    c.propuesta,
    c.foto, 
    e.titulo AS Eleccion_inscrita,
    COUNT(v.id_voto) AS total_votos 
FROM 
    candidatos AS c
INNER JOIN 
    elecciones AS e ON c.id_eleccion = e.id_eleccion
LEFT JOIN 
    votos AS v ON c.id_candidato = v.id_candidato
GROUP BY 
    c.id_candidato, c.nombre, c.apellido, e.titulo
WHERE 
    e.id_institucion = 1  ------> Filtro de Institucion
ORDER BY 
    e.titulo, total_votos DESC;
