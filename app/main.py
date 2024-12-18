from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.Routes import projetos, tarefas, usuarios
from app import models

app = FastAPI()

# Configuração de CORS
origins = ["*"] 
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registro das rotas
app.include_router(projetos.router, prefix="/projetos", tags=["Projetos"])
app.include_router(tarefas.router, prefix="/tarefas", tags=["Tarefas"])
app.include_router(usuarios.router, prefix="/usuarios", tags=["Usuários"])
