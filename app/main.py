from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

projetos_lista = []
tarefas_lista = []
usuarios_lista = []

@app.get("/")
async def root():
    return {"message": "Hello world"}

@app.get("/projetos")
def listar_projetos(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "projetos": projetos_lista, "tarefas": tarefas_lista, "usuarios": usuarios_lista},
    )

@app.get("/projetos/novo")
def novo_projeto(request: Request):
    return templates.TemplateResponse("form_projetos.html", {"request": request, "titulo": "Adicionar Projeto", "projeto": None})

@app.post("/projetos/novo")
def criar_projeto(nome: str = Form(...)):
    novo_projeto = {"id": len(projetos_lista) + 1, "nome": nome}
    projetos_lista.append(novo_projeto)
    return RedirectResponse("/projetos", status_code=303)

@app.get("/projetos/{projeto_id}/editar")
def editar_projeto(request: Request, projeto_id: int):
    projeto = next((p for p in projetos_lista if p["id"] == projeto_id), None)
    return templates.TemplateResponse("form_projetos.html", {"request": request, "titulo": "Editar Projeto", "projeto": projeto})

@app.post("/projetos/{projeto_id}/editar")
def atualizar_projeto(projeto_id: int, nome: str = Form(...)):
    for p in projetos_lista:
        if p["id"] == projeto_id:
            p["nome"] = nome
            break
    return RedirectResponse("/projetos", status_code=303)

@app.get("/projetos/{projeto_id}/excluir")
def excluir_projeto(projeto_id: int):
    global projetos_lista
    projetos_lista = [p for p in projetos_lista if p["id"] != projeto_id]
    return RedirectResponse("/projetos", status_code=303)

# Rotas de Tarefas
@app.get("/tarefas/novo")
def nova_tarefa(request: Request):
    return templates.TemplateResponse(
        "form_tarefas.html",
        {"request": request, "titulo": "Adicionar Tarefa", "tarefa": None, "projetos": projetos_lista},
    )

@app.post("/tarefas/novo")
def criar_tarefa(nome: str = Form(...), projeto_id: int = Form(...)):
    nova_tarefa = {"id": len(tarefas_lista) + 1, "nome": nome, "projeto_id": projeto_id}
    tarefas_lista.append(nova_tarefa)
    return RedirectResponse("/projetos", status_code=303)

@app.get("/tarefas/{tarefa_id}/editar")
def editar_tarefa(request: Request, tarefa_id: int):
    tarefa = next((t for t in tarefas_lista if t["id"] == tarefa_id), None)
    return templates.TemplateResponse(
        "form_tarefas.html",
        {"request": request, "titulo": "Editar Tarefa", "tarefa": tarefa, "projetos": projetos_lista},
    )

@app.post("/tarefas/{tarefa_id}/editar")
def atualizar_tarefa(tarefa_id: int, nome: str = Form(...), projeto_id: int = Form(...)):
    for t in tarefas_lista:
        if t["id"] == tarefa_id:
            t["nome"] = nome
            t["projeto_id"] = projeto_id
            break
    return RedirectResponse("/projetos", status_code=303)

@app.get("/tarefas/{tarefa_id}/excluir")
def excluir_tarefa(tarefa_id: int):
    global tarefas_lista
    tarefas_lista = [t for t in tarefas_lista if t["id"] != tarefa_id]
    return RedirectResponse("/projetos", status_code=303)

@app.get("/usuarios/novo")
def novo_usuario(request: Request):
    return templates.TemplateResponse("form_usuarios.html", {"request": request, "titulo": "Adicionar Usuário", "usuario": None})

@app.post("/usuarios/novo")
def criar_usuario(nome: str = Form(...)):
    novo_usuario = {"id": len(usuarios_lista) + 1, "nome": nome}
    usuarios_lista.append(novo_usuario)
    return RedirectResponse("/projetos", status_code=303)

@app.get("/usuarios/{usuario_id}/editar")
def editar_usuario(request: Request, usuario_id: int):
    usuario = next((u for u in usuarios_lista if u["id"] == usuario_id), None)
    return templates.TemplateResponse(
        "form_usuarios.html",
        {"request": request, "titulo": "Editar Usuário", "usuario": usuario},
    )

@app.post("/usuarios/{usuario_id}/editar")
def atualizar_usuario(usuario_id: int, nome: str = Form(...)):
    for u in usuarios_lista:
        if u["id"] == usuario_id:
            u["nome"] = nome
            break
    return RedirectResponse("/projetos", status_code=303)

@app.get("/usuarios/{usuario_id}/excluir")
def excluir_usuario(usuario_id: int):
    global usuarios_lista
    usuarios_lista = [u for u in usuarios_lista if u["id"] != usuario_id]
    return RedirectResponse("/projetos", status_code=303)
