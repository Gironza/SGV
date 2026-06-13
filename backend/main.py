from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# CREAR APP
app = FastAPI()

# CONECTAR CARPETA ARCHIVOS
app.mount(
    "/static",
    StaticFiles(directory="app/views"),
    name="static"
)

# CARPETA DE VISTAS
templates = Jinja2Templates(directory="app/views/templates")

# PAGINA PRINCIPAL
@app.get("/")
def inicio():

    return {
        "mensaje": "Sistema funcionando"
    }

# MOSTRAR LOGIN
@app.get("/login", response_class=HTMLResponse)
def mostrar_login(request: Request):

    return templates.TemplateResponse(
        "login.html",
        {"request": request}
    )

# PROCESAR LOGIN
@app.post("/login")
def login(
    usuario: str = Form(...),
    password: str = Form(...)
):

    # VALIDACION SIMPLE
    if usuario == "admin" and password == "1234":

        return {
            "mensaje": "Login correcto"
        }

    return {
        "mensaje": "Usuario o contraseña incorrectos"
    }