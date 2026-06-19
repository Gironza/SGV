# SGV - Sistema de Gestión de Votaciones

## Made by: Aéquipe
1. Santiago Peña Gironza: Coordinador del Proyecto 
2. Sandy Suaza Ramos: Equipo de Desarrollo 
3. Laura Gomez Melo: Documentacion 
4. Suset Redondo Aguiar: Investigación

## Estructura del proyecto

```
SGV/
├── app/
│   ├── main.py                  ← Entrada principal de FastAPI
│   ├── controllers/
│   │   └── auth_controller.py   ← Lógica de login y registro
│   ├── models/
│   │   └── usuario.py           ← Modelo y queries de usuario
│   ├── config/
│   │   └── database.py          ← Conexión a MySQL
│   └── views/
│       ├── templates/           ← HTMLs (Jinja2)
│       └── css/                 ← Estilos
├── db/
│   └── sgv.sql                  ← Script de base de datos
├── docs/
│   └── SRS.pdf
├── requirements.txt
└── README.md
```

## Cómo iniciar

1. Crear y activar entorno virtual:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate        
   ```

2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Configurar base de datos en `app/config/database.py`

4. Importar `db/sgv.sql` en PostgreSQL

5. Ejecutar el servidor:
   ```bash
   uvicorn app.main:app --reload
   ```

6. Abrir en el navegador: http://localhost:8000

7. Usuarios de Prueba: Admin: U: `admin@colegio.edu.co` C: `admin_123`
                       Docente: U: `aleja.pinzon@colegio.edu.co` C: `0000`
                       Estudiante (Votante): U: `daniela.rojas@colegio.edu.co` C: `0000`