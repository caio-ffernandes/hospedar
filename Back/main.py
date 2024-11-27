from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

from Back.config.database import shutdown_db, startup_db
from routers.culturas import router as culturas_router
from routers.posts import router as posts_router
from routers.subcategorias import router as subcategorias_router
from routers.tipo_responsavel import router as tipo_responsavel_router
from routers.responsaveis import router as responsaveis_router
from routers.usuarios import router as usuarios_router
from routers.usuariospost import router as usuarios_posts_router
from auth.login import router as auth_router  # Importando a rota de autenticação

app = FastAPI(title='SITE CULTURAL BRASILEIRO')

# Montagem de arquivos estáticos
app.mount("/static", StaticFiles(directory="static/uploads"), name="static")

# Inicialização e fechamento do banco de dados
app.add_event_handler("startup", startup_db)
app.add_event_handler("shutdown", shutdown_db)

# Middleware CORS para permitir conexões de outros domínios
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rota para verificar status da API
@app.get("/")
def status():
    return {"message": "Hello World"}

# Rota para servir imagens
@app.get("/images/{image_name}")
async def serve_image(image_name: str):
    image_path = f"static/uploads/{image_name}"
    if os.path.exists(image_path):
        return FileResponse(image_path)
    return {"error": "Image not found"}

# Rota para servir imagens de posts
@app.get("/postsimg/{image_name}")
async def post_image(image_name: str):
    image_path = f"static/uploads/posts/{image_name}"
    if os.path.exists(image_path):
        return FileResponse(image_path)
    return {"error": "Image not found"}

# Rota para servir imagens de responsáveis
@app.get("/responsaveisimg/{image_name}")
async def responsaveis_image(image_name: str):
    image_path = f"static/uploads/responsaveis/{image_name}"
    if os.path.exists(image_path):
        return FileResponse(image_path)
    return {"error": "Image not found"}

# Inclusão dos roteadores (rotas)
app.include_router(culturas_router)
app.include_router(posts_router)
app.include_router(subcategorias_router)
app.include_router(tipo_responsavel_router)
app.include_router(responsaveis_router)
app.include_router(usuarios_router)
app.include_router(usuarios_posts_router)
app.include_router(auth_router)
