from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

tarefas = []

class Tarefa(BaseModel):
    nome: str
    descricao: Optional[str] = None
    projeto_id: int
    usuario_id: int
    status: Optional[str] = "pendente"

class TarefaResposta(Tarefa):
    id: int

@router.post("/", response_model=TarefaResposta)
def criar_tarefa(tarefa: Tarefa):
    nova_tarefa = {
        "id": len(tarefas) + 1,
        "nome": tarefa.nome,
        "descricao": tarefa.descricao,
        "projeto_id": tarefa.projeto_id,
        "usuario_id": tarefa.usuario_id,
        "status": tarefa.status,
    }
    tarefas.append(nova_tarefa)
    return nova_tarefa


@router.get("/", response_model=List[TarefaResposta])
def listar_tarefas():
    return tarefas


@router.get("/{projeto_id}", response_model=List[TarefaResposta])
def obter_tarefas_por_projeto(projeto_id: int):
    tarefas_projeto = [tarefa for tarefa in tarefas if tarefa["projeto_id"] == projeto_id]
    if not tarefas_projeto:
        raise HTTPException(status_code=404, detail="Nenhuma tarefa encontrada para o projeto especificado.")
    return tarefas_projeto


@router.put("/{tarefa_id}", response_model=TarefaResposta)
def atualizar_tarefa(tarefa_id: int, tarefa: Tarefa):
    for t in tarefas:
        if t["id"] == tarefa_id:
            t["nome"] = tarefa.nome
            t["descricao"] = tarefa.descricao
            t["status"] = tarefa.status
            t["projeto_id"] = tarefa.projeto_id
            t["usuario_id"] = tarefa.usuario_id
            return t
    raise HTTPException(status_code=404, detail="Tarefa não encontrada.")


@router.delete("/{tarefa_id}")
def deletar_tarefa(tarefa_id: int):
    global tarefas
    tarefas_filtradas = [tarefa for tarefa in tarefas if tarefa["id"] != tarefa_id]
    if len(tarefas) == len(tarefas_filtradas):
        raise HTTPException(status_code=404, detail="Tarefa não encontrada.")
    tarefas = tarefas_filtradas
    return {"mensagem": "Tarefa deletada com sucesso!"}
