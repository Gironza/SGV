import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.auth_routes import router as auth_router
from app.routes.voto_routes import router as voto_router
from app.routes.voto_routes import router as voto_router
from app.routes.eleccion_routes import router as eleccion_router
from app.routes.candidato_routes import router as candidato_router
from app.routes.resultado_routes import router as resultado_router


# --- Logging ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
 
#app
app = FastAPI(title="SGV", version="1.0.0")


#cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # el origen exacto de Vite (React - Frontend)
    allow_credentials=False,  # No se necesitan cookies, porque esta el header
    allow_methods=["*"],
    allow_headers=["*"],
)

#routers
app.include_router(auth_router)
app.include_router(voto_router)
app.include_router(eleccion_router)
app.include_router(candidato_router)
app.include_router(resultado_router)


@app.get("/")
def api():
    return {"mensaje":" SGV API activa"}