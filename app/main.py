from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
 
from app.controllers.auth_controller import AuthController
 
 
app = FastAPI()
 

auth_controller = AuthController()
 

app.mount(
    "/static",
    StaticFiles(directory="app/views"),
    name="static"
)
 

templates = Jinja2Templates(directory="app/views/templates")
 
 

@app.get("/", response_class=HTMLResponse)
def inicio(request: Request):
    return templates.TemplateResponse(
        "inicio.html",
        {"request": request}
    )
 
 

 
@app.get("/login", response_class=HTMLResponse)
def mostrar_login(request: Request, error: str = None):
    return templates.TemplateResponse(
        "login.html",
        {"request": request, "error": error}
    )
 
 
@app.post("/login")
def login(
    request: Request,
    correo: str = Form(...),
    password: str = Form(...)
):
    resultado = auth_controller.login(correo, password)
 
    if resultado["success"]:
        rol = resultado["user"]["rol_nombre"].lower()

        destinos = {
            "administrador": "/admin",
            "docente": "/docente",
            "estudiante": "/estudiante"
        }
        destino = destinos.get(rol, "/login")
 
        return RedirectResponse(url=destino, status_code=303)
 
    return templates.TemplateResponse(
        "login.html",
        {"request": request, "error": resultado["message"]}
    )
 
 
@app.get("/registro", response_class=HTMLResponse)
def mostrar_registro(request: Request, error: str = None):
    return templates.TemplateResponse(
        "registro.html",
        {"request": request, "error": error}
    )
 
 
@app.post("/registro")
def registro(
    request: Request,
    nombres: str = Form(...),
    apellidos: str = Form(...),
    documento: str = Form(...),
    id_tipo_doc: int = Form(...),
    correo: str = Form(...),
    password: str = Form(...),
    confirmar_password: str = Form(...),
    curso: str = Form(...),
    id_institucion: int = Form(1)  
):
    if password != confirmar_password:
        return templates.TemplateResponse(
            "registro.html",
            {"request": request, "error": "Las contraseñas no coinciden"}
        )
 
    resultado = auth_controller.registro(
        nombres, apellidos, documento, id_tipo_doc,
        curso, correo, password, id_institucion
    )
 
    if resultado["success"]:
        return RedirectResponse(url="/login", status_code=303)
 
    return templates.TemplateResponse(
        "registro.html",
        {"request": request, "error": resultado["message"]}
    )
 
 
@app.get("/admin", response_class=HTMLResponse)
def panel_admin(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request})
 
 
@app.get("/docente", response_class=HTMLResponse)
def panel_docente(request: Request):
    return templates.TemplateResponse("docente.html", {"request": request})
 
 
@app.get("/estudiante", response_class=HTMLResponse)
def panel_estudiante(request: Request):
    return templates.TemplateResponse("estudiante.html", {"request": request})