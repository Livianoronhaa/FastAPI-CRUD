from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Projeto(BaseModel):
    nome: str

class ProjetoResposta(Projeto):
    id: int

projetos = []

@router.post("/", response_model=ProjetoResposta)
def criar_projeto(projeto: Projeto):
    novo_projeto = {"id": len(projetos) + 1, "nome": projeto.nome}
    projetos.append(novo_projeto)
    return novo_projeto

@router.get("/", response_model=List[ProjetoResposta])
def obter_projetos():
    return projetos

@router.get("/{projeto_id}", response_model=ProjetoResposta)
def obter_projeto(projeto_id: int):
    for projeto in projetos:
        if projeto["id"] == projeto_id:
            return projeto
    raise HTTPException(status_code=404, detail="Projeto não encontrado")

@router.put("/{projeto_id}", response_model=ProjetoResposta)
def atualizar_projeto(projeto_id: int, projeto: Projeto):
    for p in projetos:
        if p["id"] == projeto_id:
            p["nome"] = projeto.nome
            return p
    raise HTTPException(status_code=404, detail="Projeto não encontrado")

@router.delete("/{projeto_id}")
def deletar_projeto(projeto_id: int):
    global projetos
    projetos = [p for p in projetos if p["id"] != projeto_id]
    return {"mensagem": "Projeto deletado com sucesso!"}
