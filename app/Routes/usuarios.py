from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    email: str

usuarios = []

@router.post("/", response_model=Usuario)
def criar_usuario(usuario: Usuario):
    novo_usuario = {
        "id": len(usuarios) + 1,
        "nome": usuario.nome,
        "email": usuario.email,
    }
    usuarios.append(novo_usuario)
    return novo_usuario

@router.get("/", response_model=List[Usuario])
def listar_usuarios():
    return usuarios

@router.get("/{usuario_id}", response_model=Usuario)
def consultar_usuario(usuario_id: int):
    usuario = next((u for u in usuarios if u["id"] == usuario_id), None)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario

@router.put("/{usuario_id}", response_model=Usuario)
def editar_usuario(usuario_id: int, usuario: Usuario):
    usuario_existente = next((u for u in usuarios if u["id"] == usuario_id), None)
    if not usuario_existente:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    usuario_existente["nome"] = usuario.nome
    usuario_existente["email"] = usuario.email
    return usuario_existente

@router.delete("/{usuario_id}")
def excluir_usuario(usuario_id: int):
    usuario_existente = next((u for u in usuarios if u["id"] == usuario_id), None)
    if not usuario_existente:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    usuarios.remove(usuario_existente)
    return {"message": f"Usuário com ID {usuario_id} excluído com sucesso"}

