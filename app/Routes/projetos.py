from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

# Modelo para representar um projeto
class Projeto(BaseModel):
    nome: str

class ProjetoResposta(Projeto):
    id: int

# Lista de projetos (armazenamento em memória, apenas para fins de exemplo)
projetos = []

# Rota para criar um projeto
@router.post("/", response_model=ProjetoResposta)
def criar_projeto(projeto: Projeto):
    novo_projeto = {"id": len(projetos) + 1, "nome": projeto.nome}
    projetos.append(novo_projeto)
    return novo_projeto

# Rota para listar todos os projetos
@router.get("/", response_model=List[ProjetoResposta])
def obter_projetos():
    return projetos

# Rota para obter um projeto específico pelo ID
@router.get("/{projeto_id}", response_model=ProjetoResposta)
def obter_projeto(projeto_id: int):
    for projeto in projetos:
        if projeto["id"] == projeto_id:
            return projeto
    raise HTTPException(status_code=404, detail="Projeto não encontrado")

# Rota para atualizar um projeto pelo ID
@router.put("/{projeto_id}", response_model=ProjetoResposta)
def atualizar_projeto(projeto_id: int, projeto: Projeto):
    for p in projetos:
        if p["id"] == projeto_id:
            p["nome"] = projeto.nome
            return p
    raise HTTPException(status_code=404, detail="Projeto não encontrado")

# Rota para deletar um projeto pelo ID
@router.delete("/{projeto_id}")
def deletar_projeto(projeto_id: int):
    global projetos
    projetos = [p for p in projetos if p["id"] != projeto_id]
    return {"mensagem": "Projeto deletado com sucesso!"}
