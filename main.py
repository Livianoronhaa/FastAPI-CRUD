from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Dados simulados em memória
projetos = []
tarefas = []

# Modelo Pydantic para Projetos
class Projeto(BaseModel):
    nome: str

# Modelo Pydantic para Tarefas
class Tarefa(BaseModel):
    nome: str
    descricao: str
    projeto_id: int 
    status: str 

# Rotas para Projetos
@app.post("/projetos")
def criar_projeto(projeto: Projeto):
    novo_projeto = {"id": len(projetos) + 1, "nome": projeto.nome}
    projetos.append(novo_projeto)
    return novo_projeto

@app.get("/projetos")
def obter_projetos():
    return projetos

@app.put("/projetos/{projeto_id}")
def atualizar_projeto(projeto_id: int, projeto: Projeto):
    for p in projetos:
        if p["id"] == projeto_id:
            p["nome"] = projeto.nome
            return p
    return {"erro": "Projeto não encontrado"}

@app.delete("/projetos/{projeto_id}")
def deletar_projeto(projeto_id: int):
    global projetos
    projetos = [p for p in projetos if p["id"] != projeto_id]
    return {"mensagem": "Projeto deletado com sucesso!"}

# Rotas para Tarefas
@app.post("/tarefas")
def criar_tarefa(tarefa: Tarefa):
    nova_tarefa = {
        "id": len(tarefas) + 1,
        "nome": tarefa.nome,
        "descricao": tarefa.descricao,
        "projeto_id": tarefa.projeto_id,
        "status": tarefa.status
    }
    tarefas.append(nova_tarefa)
    return nova_tarefa

@app.get("/tarefas/{projeto_id}")
def obter_tarefas_por_projeto(projeto_id: int):
    tarefas_projeto = [tarefa for tarefa in tarefas if tarefa["projeto_id"] == projeto_id]
    return tarefas_projeto

@app.put("/tarefas/{tarefa_id}")
def atualizar_tarefa(tarefa_id: int, tarefa: Tarefa):
    for t in tarefas:
        if t["id"] == tarefa_id:
            t["nome"] = tarefa.nome
            t["descricao"] = tarefa.descricao
            t["status"] = tarefa.status
            t["projeto_id"] = tarefa.projeto_id
            return t
    return {"erro": "Tarefa não encontrada"}

@app.delete("/tarefas/{tarefa_id}")
def deletar_tarefa(tarefa_id: int):
    global tarefas
    tarefas = [tarefa for tarefa in tarefas if tarefa["id"] != tarefa_id]
    return {"mensagem": "Tarefa deletada com sucesso!"}
